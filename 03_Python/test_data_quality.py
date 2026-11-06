"""
================================================================================
HỆ THỐNG KIỂM THỬ CHẤT LƯỢNG DỮ LIỆU TỰ ĐỘNG (AUTOMATED DATA QUALITY TEST SUITE)
DỰ ÁN: KHO DỮ LIỆU VÀ HỆ THỐNG HỖ TRỢ RA QUYẾT ĐỊNH ỨNG PHÓ NGẬP ĐÔ THỊ (FLOOD-DSS)
Tác giả: Nhóm Đồ án Tốt nghiệp - UTH
================================================================================
Mục đích:
  Kiểm tra, đánh giá toàn diện tính toàn vẹn, độ đầy đủ, tính duy nhất,
  miền giá trị nghiệp vụ và tính hợp lệ không gian GIS của các tập dữ liệu
  trước và sau quy trình ETL.
================================================================================
"""

import sys
import os
import json
import unittest
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np

# Thiết lập đường dẫn thư mục gốc dự án
CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent
STAGING_DIR = ROOT_DIR / "02_Staging_CSV"
LOGS_DIR = ROOT_DIR / "07_Logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Danh mục các tệp dữ liệu kiểm thử
DATA_FILES = {
    "Flood_Staging": STAGING_DIR / "Flood" / "Flood_Staging_Final.csv",
    "Flood_Integrated": STAGING_DIR / "Integrated" / "Flood_Water_Population_Roads.csv",
    "Population": STAGING_DIR / "Population" / "Population_Clean.csv",
    "Roads": STAGING_DIR / "Roads" / "Roads_Clean.csv",
    "Area": STAGING_DIR / "Boundaries" / "Area_Boundaries_Clean.csv",
    "Water": STAGING_DIR / "Water" / "Flood_Water_Distance.csv"
}

# Biến toàn cục lưu kết quả kiểm thử phục vụ xuất báo cáo
TEST_RESULTS = []


def record_result(test_id, suite_name, description, status, details=""):
    """Ghi nhận kết quả của từng Test Case vào danh sách tổng hợp."""
    TEST_RESULTS.append({
        "Test_ID": test_id,
        "Suite": suite_name,
        "Description": description,
        "Status": status,
        "Details": details,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


class TestDataQualitySuite(unittest.TestCase):
    """Bộ kiểm thử chất lượng dữ liệu đề tài Flood-DSS gồm 18 Test Cases chuẩn hóa."""

    @classmethod
    def setUpClass(cls):
        """Khởi tạo và tải trước các DataFrame dữ liệu dùng chung cho toàn bộ test suite."""
        cls.data = {}
        for name, path in DATA_FILES.items():
            if path.exists():
                try:
                    cls.data[name] = pd.read_csv(path, encoding="utf-8-sig", low_memory=False)
                except Exception as e:
                    cls.data[name] = None
            else:
                cls.data[name] = None

    # =========================================================================
    # SUITE 1: KIỂM TRA SỰ TỒN TẠI TỆP TIN VÀ LƯỢC ĐỒ (SCHEMA & FILE EXISTENCE)
    # =========================================================================

    def test_01_source_files_existence(self):
        """TC01: Đảm bảo đầy đủ 6 tệp CSV nguồn và dữ liệu tích hợp đều tồn tại trên đĩa."""
        missing_files = [name for name, df in self.data.items() if df is None]
        status = "PASSED" if not missing_files else "FAILED"
        details = "Đầy đủ 6/6 tệp dữ liệu tồn tại trên đĩa" if status == "PASSED" else f"Thiếu tệp: {missing_files}"
        record_result("TC01", "Schema & Files", "Kiểm tra tồn tại đầy đủ các tệp nguồn CSV", status, details)
        self.assertEqual(len(missing_files), 0, f"Các tệp sau không tồn tại: {missing_files}")

    def test_02_baseline_record_counts(self):
        """TC02: Kiểm tra số lượng bản ghi khớp chính xác với thiết kế kiến trúc."""
        flood_rows = len(self.data["Flood_Staging"])
        integ_rows = len(self.data["Flood_Integrated"])
        pop_rows = len(self.data["Population"])
        roads_rows = len(self.data["Roads"])
        area_rows = len(self.data["Area"])

        passed = (flood_rows == 425 and integ_rows == 425 and pop_rows == 24 and roads_rows == 9 and area_rows == 24)
        status = "PASSED" if passed else "FAILED"
        details = f"Flood: {flood_rows}/425 | Integ: {integ_rows}/425 | Pop: {pop_rows}/24 | Roads: {roads_rows}/9 | Area: {area_rows}/24"
        record_result("TC02", "Schema & Files", "Đối soát số lượng bản ghi (Row Counts) theo Baseline", status, details)
        self.assertTrue(passed, f"Số lượng bản ghi không khớp baseline: {details}")

    def test_03_essential_columns_present(self):
        """TC03: Kiểm tra các cột thuộc tính cốt lõi của bảng sự kiện ngập lụt hiện diện đầy đủ."""
        required_cols = [
            'Obs_id', 'Date', 'Year', 'Location_name', 'Water_height_max_cm',
            'Cause', 'Source_id', 'Longitude', 'Latitude'
        ]
        cols = self.data["Flood_Staging"].columns.tolist()
        missing_cols = [c for c in required_cols if c not in cols]
        status = "PASSED" if not missing_cols else "FAILED"
        details = f"Đầy đủ {len(required_cols)} thuộc tính cốt lõi của bảng sự kiện ngập"
        record_result("TC03", "Schema & Files", "Kiểm tra cấu trúc thuộc tính cốt lõi bảng Flood", status, details)
        self.assertEqual(len(missing_cols), 0, f"Thiếu cột cốt lõi: {missing_cols}")

    # =========================================================================
    # SUITE 2: KIỂM TRA TÍNH DUY NHẤT VÀ KHÓA TỰ NHIÊN (UNIQUENESS & KEYS)
    # =========================================================================

    def test_04_no_full_duplicate_rows(self):
        """TC04: Đảm bảo không có dòng dữ liệu nào trùng lặp 100% thuộc tính trên toàn bộ các tệp."""
        dup_counts = {name: int(df.duplicated().sum()) for name, df in self.data.items() if df is not None}
        total_dups = sum(dup_counts.values())
        status = "PASSED" if total_dups == 0 else "FAILED"
        details = f"0 dòng trùng lặp 100% trên cả {len(dup_counts)} dataset"
        record_result("TC04", "Uniqueness", "Kiểm tra trùng lặp 100% trên toàn bộ các dòng", status, details)
        self.assertEqual(total_dups, 0, f"Phát hiện dòng trùng lặp hoàn toàn: {dup_counts}")

    def test_05_obs_id_deduplication_audit(self):
        """TC05: Phát hiện chính xác 2 dòng trùng Obs_id (Obs_239) và xác nhận khử trùng thành công."""
        flood_df = self.data["Flood_Staging"]
        dup_obs = flood_df[flood_df.duplicated("Obs_id", keep=False)]
        dup_count = len(dup_obs)
        dup_ids = dup_obs["Obs_id"].unique().tolist()

        # Kiểm tra sau khi khử trùng theo MaxDepth: mỗi Obs_id là duy nhất
        dedup_df = flood_df.sort_values("Water_height_max_cm", ascending=False).drop_duplicates(subset=["Obs_id"], keep="first")
        unique_obs_count = dedup_df["Obs_id"].nunique()

        passed = (dup_count == 2 and "Obs_239" in dup_ids and unique_obs_count == 424)
        status = "PASSED" if passed else "FAILED"
        details = f"Phát hiện đúng 2 dòng trùng mã {dup_ids}; khử trùng thành công còn {unique_obs_count} sự kiện duy nhất (QR_06)"
        record_result("TC05", "Uniqueness", "Kiểm tra phát hiện và khử trùng mã sự kiện Obs_id", status, details)
        self.assertTrue(passed, f"Sai lệch kiểm tra trùng Obs_id: count={dup_count}, ids={dup_ids}")

    def test_06_dimension_natural_keys_unique(self):
        """TC06: Đảm bảo 100% khóa tự nhiên của các danh mục Dimension đạt tính duy nhất tuyệt đối."""
        pop_unique = self.data["Population"]["Area_ID"].nunique() == 24
        roads_unique = self.data["Roads"]["Road_ID"].nunique() == 9
        area_unique = self.data["Area"]["Area_ID"].nunique() == 24

        passed = pop_unique and roads_unique and area_unique
        status = "PASSED" if passed else "FAILED"
        details = "Area_ID (24/24), Road_ID (9/9), Boundary Area_ID (24/24) đều duy nhất 100%"
        record_result("TC06", "Uniqueness", "Kiểm tra tính duy nhất của Khóa tự nhiên Dimension", status, details)
        self.assertTrue(passed, "Khóa tự nhiên của các bảng Dimension bị trùng lặp!")

    # =========================================================================
    # SUITE 3: KIỂM TRA ĐỘ ĐẦY ĐỦ VÀ DỮ LIỆU THIẾU (COMPLETENESS & NULLS)
    # =========================================================================

    def test_07_mandatory_attributes_no_null(self):
        """TC07: Các thuộc tính định danh và không gian bắt buộc tuyệt đối không được chứa giá trị NULL."""
        mandatory_cols = ['Obs_id', 'Year', 'Location_name', 'Cause', 'Source_id', 'Longitude', 'Latitude']
        flood_df = self.data["Flood_Staging"]
        null_counts = {col: int(flood_df[col].isna().sum()) for col in mandatory_cols}
        total_mandatory_nulls = sum(null_counts.values())

        status = "PASSED" if total_mandatory_nulls == 0 else "FAILED"
        details = "0 giá trị NULL trên 7 cột bắt buộc (Obs_id, Year, Location, Cause, Source, Long, Lat)"
        record_result("TC07", "Completeness", "Kiểm tra 0 giá trị NULL trên các thuộc tính bắt buộc", status, details)
        self.assertEqual(total_mandatory_nulls, 0, f"Có giá trị NULL trên cột bắt buộc: {null_counts}")

    def test_08_missing_date_audit(self):
        """TC08: Kiểm tra tỷ lệ khuyết ngày quan sát (Date IS NULL) đúng 63 dòng (14.82%) nằm trong ngưỡng."""
        flood_df = self.data["Flood_Staging"]
        missing_date_count = int(flood_df['Date'].isna().sum())
        missing_date_pct = (missing_date_count / len(flood_df)) * 100

        passed = (missing_date_count == 63 and missing_date_pct < 20.0)
        status = "PASSED" if passed else "FAILED"
        details = f"Khuyết ngày: {missing_date_count} dòng ({missing_date_pct:.2f}% <= ngưỡng 20.0%); gán TimeKey = -1"
        record_result("TC08", "Completeness", "Kiểm tra tỷ lệ khuyết Ngày quan sát (Date IS NULL)", status, details)
        self.assertTrue(passed, f"Số lượng khuyết ngày sai lệch: {missing_date_count}")

    def test_09_missing_depth_flag_consistency(self):
        """TC09: Phân loại chính xác 257 dòng cờ Missing_Depth và 278 dòng khuyết độ sâu số học."""
        flood_df = self.data["Flood_Staging"]
        actual_numeric_nulls = int(flood_df['Water_height_max_cm'].isna().sum())
        flagged_missing_depth = int((flood_df['Missing_Depth'] == True).sum())
        qualitative_depth_nulls = int(
            (flood_df['Water_height_max_cm'].isna() & (flood_df['Depth_class'].isin(['Severe', 'Heavy']))).sum()
        )

        # 278 dòng thiếu số cm = 257 dòng thiếu hoàn toàn (Missing_Depth=True) + 21 dòng có phân lớp định tính (16 Severe + 5 Heavy)
        passed = (actual_numeric_nulls == 278 and flagged_missing_depth == 257 and qualitative_depth_nulls == 21)
        status = "PASSED" if passed else "FAILED"
        details = (f"Khuyết độ sâu số học: {actual_numeric_nulls} dòng (65.41%); "
                   f"cờ Missing_Depth: {flagged_missing_depth} dòng (60.47%); "
                   f"21 dòng có nhãn định tính (16 Severe, 5 Heavy)")
        record_result("TC09", "Completeness", "Kiểm tra tính nhất quán của cờ kiểm định Missing_Depth", status, details)
        self.assertTrue(passed, f"Sai lệch kiểm tra độ sâu: numeric={actual_numeric_nulls}, flag={flagged_missing_depth}")

    # =========================================================================
    # SUITE 4: KIỂM TRA MIỀN GIÁ TRỊ VÀ LOGIC NGHIỆP VỤ (DOMAIN & LOGIC - QR_01, QR_02)
    # =========================================================================

    def test_10_non_negative_depth(self):
        """TC10 [QR_01]: Độ sâu ngập lớn nhất và nhỏ nhất phải lớn hơn hoặc bằng 0."""
        flood_df = self.data["Flood_Staging"]
        max_depth_valid = flood_df['Water_height_max_cm'].dropna()
        min_depth_valid = flood_df['Water_height_min_cm'].dropna()

        negative_max = int((max_depth_valid < 0).sum())
        negative_min = int((min_depth_valid < 0).sum())

        passed = (negative_max == 0 and negative_min == 0)
        status = "PASSED" if passed else "FAILED"
        details = f"0 dòng độ sâu âm (MaxDepth min: {max_depth_valid.min()} cm, MinDepth min: {min_depth_valid.min()} cm)"
        record_result("TC10", "Domain & Business Logic", "Kiểm tra quy tắc QR_01: Độ sâu ngập không âm (>= 0)", status, details)
        self.assertTrue(passed, f"Phát hiện độ sâu âm: max={negative_max}, min={negative_min}")

    def test_11_non_negative_duration(self):
        """TC11 [QR_02]: Thời lượng ngập phải lớn hơn hoặc bằng 0 giờ."""
        flood_df = self.data["Flood_Staging"]
        duration_valid = flood_df['Duration_hours'].dropna()
        negative_duration = int((duration_valid < 0).sum())

        passed = (negative_duration == 0)
        status = "PASSED" if passed else "FAILED"
        details = f"0 dòng thời lượng ngập âm (Thời lượng min: {duration_valid.min()} giờ, max: {duration_valid.max()} giờ)"
        record_result("TC11", "Domain & Business Logic", "Kiểm tra quy tắc QR_02: Thời lượng ngập không âm (>= 0)", status, details)
        self.assertTrue(passed, f"Phát hiện thời lượng ngập âm: {negative_duration}")

    def test_12_valid_cause_domain(self):
        """TC12: Danh mục nguyên nhân ngập (Cause) chỉ được chứa các giá trị hợp lệ theo thiết kế."""
        flood_df = self.data["Flood_Staging"]
        causes = flood_df['Cause'].dropna().unique().tolist()
        valid_causes = ['High tide', 'Rain', 'Combined', 'Triều cường', 'Mưa lớn', 'Mưa kết hợp triều cường']
        invalid_causes = [c for c in causes if c not in valid_causes]

        passed = (len(invalid_causes) == 0)
        status = "PASSED" if passed else "FAILED"
        details = f"100% nguyên nhân hợp lệ trong danh mục chuẩn: {causes}"
        record_result("TC12", "Domain & Business Logic", "Kiểm tra miền giá trị danh mục nguyên nhân ngập (Cause)", status, details)
        self.assertTrue(passed, f"Phát hiện nguyên nhân không hợp lệ: {invalid_causes}")

    def test_13_date_year_logical_consistency(self):
        """TC13: Phát hiện chính xác duy nhất 1 bản ghi lệch Ngày-Năm (Obs_298) và kiểm tra tính nhất quán."""
        flood_df = self.data["Flood_Staging"]
        has_date = flood_df[flood_df['Date'].notna()].copy()
        has_date['Extracted_Year'] = pd.to_datetime(has_date['Date']).dt.year

        mismatch = has_date[has_date['Extracted_Year'] != has_date['Year']]
        mismatch_count = len(mismatch)
        mismatch_obs = mismatch['Obs_id'].tolist()

        # Bản ghi Obs_298 có Date 2018-10-08 nhưng Year 2019; 361 bản ghi có Date còn lại khớp 100%
        passed = (mismatch_count == 1 and "Obs_298" in mismatch_obs and len(has_date) == 362)
        status = "PASSED" if passed else "FAILED"
        details = f"Phát hiện đúng 1 bản ghi lệch ngày-năm ({mismatch_obs}: Date 2018 vs Year 2019); 361/362 bản ghi khớp 100%"
        record_result("TC13", "Domain & Business Logic", "Kiểm tra tính nhất quán giữa cột Date và cột Year", status, details)
        self.assertTrue(passed, f"Lệch ngày-năm không đúng dự kiến: count={mismatch_count}, obs={mismatch_obs}")

    # =========================================================================
    # SUITE 5: KIỂM TRA ĐỘ CHÍNH XÁC KHÔNG GIAN GIS (GEOSPATIAL VALIDITY - QR_03)
    # =========================================================================

    def test_14_coordinates_within_hcmc_bounds(self):
        """TC14 [QR_03]: Tọa độ 100% điểm ngập nằm trong bounding box khảo sát; xác định chính xác 2 điểm Vũng Tàu."""
        flood_df = self.data["Flood_Staging"]
        lat_valid = (flood_df['Latitude'] >= 10.3) & (flood_df['Latitude'] <= 11.2)
        lon_valid = (flood_df['Longitude'] >= 106.3) & (flood_df['Longitude'] <= 107.2)
        valid_coords = lat_valid & lon_valid
        invalid_count = int((~valid_coords).sum())

        # Riêng 2 điểm Obs_12, Obs_13 nằm tại Vũng Tàu (Lon ~107.12) được hệ thống ghi nhận chính xác
        vungtau_points = flood_df[flood_df['Longitude'] > 107.1]['Obs_id'].tolist()

        passed = (invalid_count == 0 and len(vungtau_points) == 2 and set(vungtau_points) == {'Obs_12', 'Obs_13'})
        status = "PASSED" if passed else "FAILED"
        details = (f"100% tọa độ nằm trong Bounding Box khảo sát [10.3-11.2°N, 106.3-107.2°E]; "
                   f"xác định đúng 2 điểm Vũng Tàu ({vungtau_points}) được định tuyến sang Unknown Member")
        record_result("TC14", "Geospatial Accuracy", "Kiểm tra quy tắc QR_03: Tọa độ WGS84 trong phạm vi khảo sát", status, details)
        self.assertTrue(passed, f"Tọa độ không hợp lệ: invalid={invalid_count}, vungtau={vungtau_points}")

    def test_15_distance_to_water_valid(self):
        """TC15: Khoảng cách ngắn nhất tới mạng lưới sông kênh phải không âm và nằm trong ngưỡng vật lý."""
        integ_df = self.data["Flood_Integrated"]
        dist_water = integ_df['DistanceToWater_m'].dropna()
        neg_dist = int((dist_water < 0).sum())
        min_dist = float(dist_water.min())
        mean_dist = float(dist_water.mean())
        max_dist = float(dist_water.max())

        passed = (neg_dist == 0 and min_dist == 0.0 and max_dist < 20000.0)
        status = "PASSED" if passed else "FAILED"
        details = f"0 khoảng cách âm | Min: {min_dist:.2f}m | Mean: {mean_dist:.2f}m | Max: {max_dist:.2f}m (Cần Giờ/Củ Chi)"
        record_result("TC15", "Geospatial Accuracy", "Kiểm tra tính hợp lệ khoảng cách tới sông kênh (DistanceToWater)", status, details)
        self.assertTrue(passed, f"Khoảng cách sông kênh không hợp lệ: min={min_dist}, max={max_dist}")

    def test_16_distance_to_roads_valid(self):
        """TC16: Khoảng cách ngắn nhất tới trục đường bộ phải không âm."""
        integ_df = self.data["Flood_Integrated"]
        dist_road = integ_df['DistanceToNearestRoad_m'].dropna()
        neg_dist = int((dist_road < 0).sum())
        min_dist = float(dist_road.min())
        max_dist = float(dist_road.max())

        passed = (neg_dist == 0 and min_dist >= 0.0)
        status = "PASSED" if passed else "FAILED"
        details = f"0 khoảng cách âm | Min: {min_dist:.2f}m | Max: {max_dist:.2f}m | 100% hợp lệ"
        record_result("TC16", "Geospatial Accuracy", "Kiểm tra tính hợp lệ khoảng cách tới đường bộ (DistanceToRoad)", status, details)
        self.assertTrue(passed, f"Khoảng cách tới đường bộ không hợp lệ: neg={neg_dist}")

    # =========================================================================
    # SUITE 6: TÍCH HỢP VÀ TOÀN VẸN THAM CHIẾU (INTEGRATION & REFERENTIAL - QR_04, QR_05)
    # =========================================================================

    def test_17_population_area_id_castable_to_int(self):
        """TC17 [QR_04]: Kiểm tra lỗi float string ('765.0') và xác nhận 100% chuyển đổi an toàn sang số nguyên."""
        integ_df = self.data["Flood_Integrated"]
        area_ids = integ_df['Population_Area_ID'].dropna().astype(str)

        # Kiểm tra xem có đuôi .0 hay không
        float_str_count = int(area_ids.str.endswith(".0").sum())

        # Kiểm tra khả năng ép kiểu an toàn
        cleaned_ids = area_ids.str.replace(r"\.0$", "", regex=True)
        is_digit = cleaned_ids.str.isdigit()
        non_digit_count = int((~is_digit).sum())

        passed = (non_digit_count == 0 and float_str_count == 417)
        status = "PASSED" if passed else "FAILED"
        details = f"Phát hiện 417 chuỗi float string; 100% ({len(cleaned_ids)} dòng) ép kiểu an toàn sang INT (QR_04)"
        record_result("TC17", "Integration & Referential", "Kiểm tra quy tắc QR_04: Ép kiểu mã quận/huyện dạng float string", status, details)
        self.assertTrue(passed, f"Có {non_digit_count} giá trị Area_ID không chuyển được sang số nguyên!")

    def test_18_area_referential_mapping(self):
        """TC18 [QR_05]: 417 bản ghi nội thành khớp 100% với 24 quận/huyện; 8 bản ghi giáp ranh gán Unknown (-1)."""
        integ_df = self.data["Flood_Integrated"]
        pop_df = self.data["Population"]

        valid_pop_codes = set(pop_df['Area_ID'].astype(str).str.replace(r"\.0$", "", regex=True))

        matched_mask = integ_df['Population_Area_ID'].notna()
        matched_count = int(matched_mask.sum())
        unmatched_count = int((~matched_mask).sum())

        matched_ids = set(
            integ_df.loc[matched_mask, 'Population_Area_ID']
            .astype(str)
            .str.replace(r"\.0$", "", regex=True)
        )

        all_matched_valid = matched_ids.issubset(valid_pop_codes)
        passed = (matched_count == 417 and unmatched_count == 8 and all_matched_valid)

        status = "PASSED" if passed else "FAILED"
        details = f"417/425 sự kiện khớp 24 quận/huyện; 8 điểm giáp ranh/ngoài tỉnh định tuyến sang Unknown Member (-1) theo QR_05"
        record_result("TC18", "Integration & Referential", "Kiểm tra quy tắc QR_05: Toàn vẹn tham chiếu mã đơn vị hành chính", status, details)
        self.assertTrue(passed, f"Sai lệch đối soát mã quận: matched={matched_count}, unmatched={unmatched_count}")


def generate_reports():
    """Xuất báo cáo kết quả kiểm thử ra tệp JSON và văn bản tổng hợp."""
    json_path = LOGS_DIR / "Data_Quality_Test_Report.json"
    summary_path = LOGS_DIR / "Data_Quality_Test_Summary.txt"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(TEST_RESULTS, f, ensure_ascii=False, indent=2)

    total_tests = len(TEST_RESULTS)
    passed_tests = sum(1 for r in TEST_RESULTS if r["Status"] == "PASSED")
    failed_tests = total_tests - passed_tests
    pass_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

    lines = [
        "=" * 100,
        "  BÁO CÁO TỔNG HỢP KẾT QUẢ KIỂM THỬ CHẤT LƯỢNG DỮ LIỆU TỰ ĐỘNG BẰNG PYTHON (FLOOD-DSS)",
        "=" * 100,
        f"Thời gian thực thi : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
        f"Tổng số ca kiểm thử: {total_tests}",
        f"Số ca ĐẠT (PASSED) : {passed_tests} / {total_tests}",
        f"Số ca LỖI (FAILED) : {failed_tests} / {total_tests}",
        f"Tỷ lệ thành công   : {pass_rate:.1f}%",
        "-" * 100,
        f"{'Mã TC':<6} | {'Phân nhóm kiểm thử':<26} | {'Trạng thái':<10} | {'Chi tiết kết quả'}",
        "-" * 100
    ]

    for r in TEST_RESULTS:
        lines.append(f"{r['Test_ID']:<6} | {r['Suite']:<26} | {r['Status']:<10} | {r['Details']}")

    lines.append("=" * 100)
    summary_text = "\n".join(lines)

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary_text)

    print(summary_text)


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print(" BẮT ĐẦU THỰC THI BỘ KIỂM THỬ CHẤT LƯỢNG DỮ LIỆU TỰ ĐỘNG (DATA QUALITY TEST SUITE)")
    print("=" * 80 + "\n")

    # Tạo Test Suite và nạp toàn bộ các test cases
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDataQualitySuite)
    runner = unittest.TextTestRunner(verbosity=2)
    test_result = runner.run(suite)

    # Xuất báo cáo chi tiết
    print("\n" + "=" * 80)
    print(" KẾT QUẢ TỔNG HỢP VÀ GHI NHẬN NHẬT KÝ KIỂM THỬ (TEST LOGS)")
    print("=" * 80)
    generate_reports()

    # Trả mã thoát tương ứng
    sys.exit(0 if test_result.wasSuccessful() else 1)
