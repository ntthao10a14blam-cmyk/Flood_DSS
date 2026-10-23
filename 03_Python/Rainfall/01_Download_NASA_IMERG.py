
import os
import json
import time
import requests

from pathlib import Path
from urllib.parse import urlparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# ============================================================
# 1. CAU HINH NASA
# ============================================================

CMR_BASE_URL = "https://cmr.earthdata.nasa.gov"

SHORT_NAME = "GPM_3IMERGDF"
VERSION = "07"

# Tai thu du lieu thang 09/2023
FILTER_TEMPORAL = (
    "2023-09-01T00:00:00.000Z,"
    "2023-09-30T23:59:59.999Z"
)

# Bounding box: West, South, East, North
# TP.HCM va khu vuc lan can
FILTER_BBOX = "106.3,10.3,107.3,11.3"

# ============================================================
# 2. DUONG DAN DU AN
# ============================================================

ROOT = Path(r"D:\Kho_du_lieu\Flood_DSS")

DOWNLOAD_DIR = (
    ROOT
    / "01_Raw"
    / "Rainfall"
    / "NASA_IMERG_Final_V07"
)

LOG_DIR = ROOT / "07_Logs"

DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

REPORT_FILE = LOG_DIR / "NASA_IMERG_Download_Report.json"

# ============================================================
# 3. CAU HINH TAI
# ============================================================

MAX_WORKERS = 2
PAGE_SIZE = 2000
TIMEOUT = 180
MAX_RETRIES = 3

# Gioi han tai thu de tranh tai qua nhieu du lieu
MAX_FILES = 35

# ============================================================
# 4. HAM TRUY VAN NASA CMR
# ============================================================

def query_cmr_granules(search_after=None):

    url = (
        f"{CMR_BASE_URL}"
        "/search/granules.umm_json"
    )

    params = {
        "short_name": SHORT_NAME,
        "version": VERSION,
        "temporal": FILTER_TEMPORAL,
        "bounding_box": FILTER_BBOX,
        "page_size": PAGE_SIZE,
    }

    headers = {
        "Accept": "application/json"
    }

    if search_after:
        headers["CMR-Search-After"] = search_after

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=60
    )

    response.raise_for_status()

    return response, response.json()


# ============================================================
# 5. LAY DANH SACH FILE
# ============================================================

def get_download_urls():

    print("\n===== TIM DU LIEU NASA =====")

    search_after = None
    download_urls = []
    total_granules = None

    while True:

        response, data = query_cmr_granules(
            search_after=search_after
        )

        if total_granules is None:
            total_granules = data.get("hits", 0)
            print("Total granules:", total_granules)

        items = data.get("items", [])

        if not items:
            break

        for item in items:

            related_urls = (
                item.get("umm", {})
                .get("RelatedUrls", [])
            )

            for related in related_urls:

                if related.get("Type") != "GET DATA":
                    continue

                url = related.get("URL")

                if not url:
                    continue

                # Chi lay du lieu NetCDF/HDF
                filename = unquote(
                    Path(urlparse(url).path).name
                )

                if filename.lower().endswith(
                    (".nc4", ".nc", ".hdf5", ".h5")
                ):
                    download_urls.append(url)

        search_after = response.headers.get(
            "CMR-Search-After"
        )

        if not search_after:
            break

    # Loai bo URL trung
    download_urls = list(
        dict.fromkeys(download_urls)
    )

    print("So URL tim duoc:", len(download_urls))

    if len(download_urls) > MAX_FILES:
        print(
            f"Vuot gioi han thu nghiem {MAX_FILES} file."
        )
        print("Dung tai de tranh dung luong qua lon.")
        return []

    return download_urls


# ============================================================
# 6. TAI TUNG FILE
# ============================================================

def download_file(url):

    filename = unquote(
        Path(urlparse(url).path).name
    )

    if not filename:
        return {
            "filename": "",
            "status": "failed",
            "error": "Khong co ten file"
        }

    final_path = DOWNLOAD_DIR / filename
    temp_path = DOWNLOAD_DIR / (filename + ".part")

    # Khong tu dong tin rang file da co la hop le.
    # Can kiem tra kich thuoc va dinh dang.
    if final_path.exists():

        size = final_path.stat().st_size

        if size > 0:
            return {
                "filename": filename,
                "status": "existing_review",
                "size_bytes": size,
                "error": (
                    "File da ton tai. "
                    "Can kiem tra tinh hop le."
                )
            }

        final_path.unlink()

    last_error = ""

    for attempt in range(1, MAX_RETRIES + 1):

        try:

            if temp_path.exists():
                temp_path.unlink()

            token = os.environ.get("EARTHDATA_TOKEN", "").strip()

            if not token:
                raise ValueError("Chua cau hinh EARTHDATA_TOKEN")

            session = requests.Session()
            session.headers.update({
                "Authorization": f"Bearer {token}"
            })

            with session.get(
                url,
                stream=True,
                timeout=TIMEOUT,
                allow_redirects=True
            ) as response:

                response.raise_for_status()

                content_type = response.headers.get(
                    "Content-Type", ""
                ).lower()

                if "text/html" in content_type:
                    raise ValueError(
                        "NASA tra ve trang HTML. "
                        "Co the can dang nhap Earthdata."
                    )

                expected_size = response.headers.get(
                    "Content-Length"
                )

                with open(temp_path, "wb") as file:

                    for chunk in response.iter_content(
                        chunk_size=1024 * 1024
                    ):

                        if chunk:
                            file.write(chunk)

            actual_size = temp_path.stat().st_size

            if actual_size == 0:
                raise ValueError("File rong")

            if expected_size is not None:

                if actual_size != int(expected_size):
                    raise ValueError(
                        "Dung luong file khong khop"
                    )

            # Kiem tra chu ky file NetCDF4/HDF5
            # Hoac NetCDF classic
            with open(temp_path, "rb") as file:
                signature = file.read(8)

            valid_signature = (
                signature.startswith(b"\x89HDF\r\n\x1a\n")
                or signature.startswith(b"CDF")
            )

            if not valid_signature:
                raise ValueError(
                    "File khong co chu ky NetCDF/HDF hop le"
                )

            temp_path.replace(final_path)

            return {
                "filename": filename,
                "status": "success",
                "size_bytes": actual_size,
                "error": ""
            }

        except Exception as error:

            last_error = str(error)

            if temp_path.exists():
                temp_path.unlink()

            print(
                f"\nLoi {filename} "
                f"(lan {attempt}/{MAX_RETRIES}): "
                f"{last_error}"
            )

            # Loi xac thuc: khong thu lai lien tuc
            if (
                "401" in last_error
                or "403" in last_error
                or "trang HTML" in last_error
            ):
                break

            if attempt < MAX_RETRIES:
                time.sleep(2 * attempt)

    return {
        "filename": filename,
        "status": "failed",
        "size_bytes": 0,
        "error": last_error
    }


# ============================================================
# 7. TAI DU LIEU SONG SONG
# ============================================================

def download_all(urls):

    print("\n===== BAT DAU TAI =====")
    print("So file:", len(urls))
    print("Thu muc:", DOWNLOAD_DIR)

    results = []

    with ThreadPoolExecutor(
        max_workers=MAX_WORKERS
    ) as executor:

        futures = [
            executor.submit(download_file, url)
            for url in urls
        ]

        for future in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="Downloading",
            unit="file"
        ):

            results.append(future.result())

    return results


# ============================================================
# 8. BAO CAO KET QUA
# ============================================================

def save_report(results):

    success = sum(
        r["status"] == "success"
        for r in results
    )

    failed = sum(
        r["status"] == "failed"
        for r in results
    )

    existing = sum(
        r["status"] == "existing_review"
        for r in results
    )

    report = {
        "source": "NASA GES DISC",
        "product": SHORT_NAME,
        "version": VERSION,
        "temporal": FILTER_TEMPORAL,
        "bounding_box": FILTER_BBOX,
        "download_directory": str(DOWNLOAD_DIR),
        "success": success,
        "failed": failed,
        "existing_review": existing,
        "files": results
    }

    REPORT_FILE.write_text(
        json.dumps(
            report,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )

    print("\n===== KET QUA =====")
    print("Tai thanh cong:", success)
    print("Tai that bai:", failed)
    print("File da ton tai can kiem tra:", existing)
    print("Bao cao:", REPORT_FILE)


# ============================================================
# 9. MAIN
# ============================================================

def main():

    print("=" * 55)
    print("NASA GPM IMERG FINAL DAILY V07")
    print("=" * 55)

    print("Thoi gian:", FILTER_TEMPORAL)
    print("Bounding box:", FILTER_BBOX)
    print("Luu tai:", DOWNLOAD_DIR)

    try:

        urls = get_download_urls()

        if not urls:
            print(
                "\nKhong co URL phu hop "
                "hoac vuot gioi han tai thu."
            )
            return

        results = download_all(urls)

        save_report(results)

        print("\n===== HOAN THANH =====")

        print(
            "Luu y: File NASA co the la du lieu "
            "toan cau, chua duoc cat theo TP.HCM."
        )

    except Exception as error:

        print("\nCHUONG TRINH GAP LOI:")
        print(type(error).__name__)
        print(error)


if __name__ == "__main__":
    main()
