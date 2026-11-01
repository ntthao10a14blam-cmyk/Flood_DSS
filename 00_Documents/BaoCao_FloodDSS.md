# BÁO CÁO ĐỒ ÁN
## XÂY DỰNG KHO DỮ LIỆU TÍCH HỢP VÀ HỆ THỐNG HỖ TRỢ RA QUYẾT ĐỊNH ỨNG PHÓ NGẬP ĐÔ THỊ TẠI TP. HỒ CHÍ MINH

---

## MỤC LỤC

- [TÓM TẮT ĐỒ ÁN](#tóm-tắt-đồ-án)
- [DANH MỤC CÁC TỪ VIẾT TẮT](#danh-mục-các-từ-viết-tắt)
- [DANH MỤC HÌNH ẢNH](#danh-mục-hình-ảnh)
- [DANH MỤC BẢNG BIỂU](#danh-mục-bảng-biểu)
- [CHƯƠNG 1: TỔNG QUAN](#chương-1-tổng-quan)
- [CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ KHO DỮ LIỆU](#chương-2-phân-tích-và-thiết-kế-kho-dữ-liệu)
- [CHƯƠNG 3: XÂY DỰNG QUY TRÌNH ETL](#chương-3-xây-dựng-quy-trình-etl)
- [CHƯƠNG 4: TRỰC QUAN HÓA DỮ LIỆU VÀ HỖ TRỢ RA QUYẾT ĐỊNH](#chương-4-trực-quan-hóa-dữ-liệu-và-hỗ-trợ-ra-quyết-định)
- [TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)

---

## TÓM TẮT ĐỒ ÁN

Đồ án tập trung xây dựng một hệ thống Kho dữ liệu (Data Warehouse) tích hợp và Hệ thống Hỗ trợ Ra quyết định (Decision Support System – DSS) phục vụ công tác ứng phó ngập đô thị tại Thành phố Hồ Chí Minh. Dữ liệu được thu thập từ nhiều nguồn khác nhau bao gồm các file CSV chứa thông tin quan sát ngập, dân số, đường giao thông và địa giới hành chính. Toàn bộ quá trình xử lý dữ liệu được thực hiện theo kiến trúc ETL (Extract – Transform – Load) sử dụng SQL Server Integration Services (SSIS), với vùng trung gian Staging làm nơi tiếp nhận và làm sạch dữ liệu trước khi nạp vào kho dữ liệu theo mô hình hình sao (Star Schema). Hệ thống hỗ trợ phân tích OLAP thông qua SQL Server Analysis Services (SSAS) và trực quan hóa dữ liệu bằng Power BI, cung cấp các dashboard giúp ra quyết định ứng phó ngập một cách nhanh chóng và hiệu quả.

---

## DANH MỤC CÁC TỪ VIẾT TẮT

| Từ viết tắt | Diễn giải | Ý nghĩa |
|-------------|-----------|---------|
| BI | Business Intelligence | Kinh doanh thông minh |
| CSV | Comma-Separated Values | Định dạng file văn bản phân tách bằng dấu phẩy |
| DSS | Decision Support System | Hệ thống hỗ trợ ra quyết định |
| DW | Data Warehouse | Kho dữ liệu |
| ETL | Extract – Transform – Load | Trích xuất – Chuyển đổi – Nạp dữ liệu |
| OLAP | Online Analytical Processing | Xử lý phân tích trực tuyến |
| OLTP | Online Transaction Processing | Xử lý giao dịch trực tuyến |
| SSIS | SQL Server Integration Services | Dịch vụ tích hợp dữ liệu SQL Server |
| SSAS | SQL Server Analysis Services | Dịch vụ phân tích SQL Server |
| SSRS | SQL Server Reporting Services | Dịch vụ báo cáo SQL Server |
| SCD | Slowly Changing Dimension | Chiều thay đổi chậm |
| stg | Staging | Vùng dữ liệu trung gian |
| dw | Data Warehouse schema | Schema kho dữ liệu |
| FK | Foreign Key | Khóa ngoại |
| PK | Primary Key | Khóa chính |
| MDX | Multidimensional Expressions | Ngôn ngữ truy vấn đa chiều |
| MOLAP | Multidimensional OLAP | OLAP đa chiều |
| ROLAP | Relational OLAP | OLAP quan hệ |
| HOLAP | Hybrid OLAP | OLAP lai |
| FASMI | Fast, Analysis, Shared, Multidimensional, Information | Tiêu chuẩn chất lượng hệ thống OLAP |
| NULL | — | Giá trị rỗng/không xác định |

---

## DANH MỤC HÌNH ẢNH

| Hình | Mô tả |
|------|-------|
| Hình 1 | Kết quả kiểm tra dữ liệu sau khi nạp vào bảng stg.Population |
| Hình 2 | Luồng Data Flow của Package 04: Nạp dữ liệu đường giao thông vào bảng stg.Roads |
| Hình 3 | Luồng Data Flow của Package 05: Nạp dữ liệu địa giới hành chính vào bảng stg.Area |
| Hình 4 | Kiến trúc tổng thể hệ thống Kho dữ liệu Flood DSS |
| Hình 5 | Sơ đồ Star Schema của kho dữ liệu |
| Hình 6 | Luồng điều phối của gói 08_Master_ETL.dtsx |
| Hình 7 | Kết quả kiểm tra tính duy nhất của Grain hai bảng Fact |
| Hình 8 | Kết quả kiểm tra số lượng bản ghi sau ETL |

---

## DANH MỤC BẢNG BIỂU

| Bảng | Mô tả |
|------|-------|
| Bảng 2.1 | Mô tả các file dữ liệu nguồn |
| Bảng 2.2 | Ma trận Bus Matrix |
| Bảng 2.3 | Thiết kế bảng Dim_Time |
| Bảng 2.4 | Thiết kế bảng Dim_Area |
| Bảng 2.5 | Thiết kế bảng Dim_Location |
| Bảng 2.6 | Thiết kế bảng Dim_Cause |
| Bảng 2.7 | Thiết kế bảng Dim_Source |
| Bảng 2.8 | Thiết kế bảng Fact_FloodObservation |
| Bảng 2.9 | Thiết kế bảng Fact_Population |
| Bảng 3.1 | Danh sách gói SSIS trong dự án FloodDSS_ETL |
| Bảng 3.2 | Ánh xạ cột Package 03_Load_Population |
| Bảng 3.3 | Ánh xạ cột Package 04_Load_Roads |
| Bảng 3.4 | Ánh xạ cột Package 05_Load_Area |
| Bảng 3.5 | Kết quả đối chiếu số lượng bản ghi Staging |

---

## CHƯƠNG 1: TỔNG QUAN

### 1.1 Tổng quan về Kho dữ liệu và Kinh doanh thông minh

#### 1.1.1 Khái niệm

**Kho dữ liệu (Data Warehouse)**

Kho dữ liệu là một hệ thống lưu trữ dữ liệu tập trung, được thiết kế để hỗ trợ phân tích và ra quyết định. Theo định nghĩa của William H. Inmon – người được coi là cha đẻ của khái niệm Data Warehouse – kho dữ liệu là *"một tập hợp dữ liệu theo chủ đề, tích hợp, biến đổi theo thời gian và không biến động, nhằm hỗ trợ quá trình ra quyết định của nhà quản lý"*. Kho dữ liệu tổng hợp thông tin từ nhiều nguồn khác nhau, chuẩn hóa và lưu trữ chúng theo cấu trúc phù hợp với mục tiêu phân tích, thay vì phục vụ các giao dịch xử lý thời gian thực.

**Kinh doanh thông minh (Business Intelligence)**

Business Intelligence (BI) là tập hợp các công nghệ, quy trình và công cụ cho phép thu thập, tích hợp, phân tích và trình bày thông tin kinh doanh. Mục tiêu chính của BI là hỗ trợ người ra quyết định nắm bắt được bức tranh toàn diện về hoạt động của tổ chức thông qua các báo cáo, dashboard, biểu đồ và phân tích xu hướng. Trong ngữ cảnh đề tài, BI được áp dụng để phân tích tình hình ngập lụt tại TP.HCM, cung cấp thông tin nhanh chóng cho các cơ quan quản lý đô thị.

#### 1.1.2 Đặc trưng cơ bản

Kho dữ liệu có bốn đặc trưng cơ bản được Inmon xác định, thường được gọi là **SIVN**:

- **Subject-oriented (Hướng chủ đề):** Dữ liệu được tổ chức xung quanh các chủ đề nghiệp vụ cụ thể thay vì theo ứng dụng. Ví dụ, trong đề tài này, các chủ đề bao gồm: ngập lụt, dân số, khu vực hành chính và đường giao thông.
- **Integrated (Tích hợp):** Dữ liệu từ nhiều nguồn khác nhau được chuẩn hóa về định dạng, đơn vị và quy ước trước khi đưa vào kho, đảm bảo tính nhất quán.
- **Time-variant (Biến đổi theo thời gian):** Kho dữ liệu lưu trữ lịch sử theo thời gian, mỗi bản ghi đều gắn với một mốc thời gian, cho phép phân tích xu hướng và so sánh theo giai đoạn.
- **Non-volatile (Không biến động):** Dữ liệu một khi đã được nạp vào kho không bị cập nhật hay xóa tùy tiện; các thay đổi được ghi nhận bằng cách thêm bản ghi mới, giữ nguyên lịch sử.

Kiến trúc kho dữ liệu thường gồm ba tầng: tầng nguồn dữ liệu (Operational/Source layer), tầng tích hợp trung gian (Staging layer) và tầng kho dữ liệu (Data Warehouse layer). Ở đề tài này, cấu trúc đó được thể hiện qua schema `stg` (Staging) và `dw` (Data Warehouse) trong SQL Server.

#### 1.1.3 Vai trò của Business Intelligence trong DSS

Hệ thống Hỗ trợ Ra quyết định (DSS) cần thông tin chính xác, kịp thời và có chiều sâu phân tích. BI đóng vai trò cầu nối giữa dữ liệu thô và quyết định quản lý thông qua:

- **Tổng hợp dữ liệu đa chiều:** Cho phép phân tích theo nhiều góc độ như thời gian, khu vực, nguyên nhân ngập.
- **Trực quan hóa:** Dashboard và báo cáo giúp người dùng nắm bắt xu hướng nhanh chóng.
- **Cảnh báo và dự báo:** Dựa trên dữ liệu lịch sử, hệ thống có thể phát hiện bất thường hoặc dự báo xu hướng.

Trong đề tài, Power BI được sử dụng làm công cụ BI, kết nối trực tiếp với kho dữ liệu để tạo các báo cáo về tình hình ngập theo khu vực, theo thời gian và theo nguyên nhân, hỗ trợ các cơ quan chức năng ra quyết định ứng phó kịp thời.

#### 1.1.4 Mối quan hệ tương hỗ giữa Kho dữ liệu và BI

Kho dữ liệu và BI có mối quan hệ bổ trợ lẫn nhau: kho dữ liệu cung cấp nền tảng dữ liệu đáng tin cậy, còn BI cung cấp các công cụ khai thác và trình bày thông tin từ kho đó. Không có kho dữ liệu tích hợp và sạch, các công cụ BI sẽ cho ra kết quả phân tích sai lệch. Ngược lại, kho dữ liệu mà không có lớp BI khai thác sẽ không phát huy được giá trị. Vì vậy, hai thành phần này luôn được triển khai song hành trong một giải pháp hoàn chỉnh.

---

### 1.2 Các đặc trưng về mặt dữ liệu của một hệ thống DW và BI

#### 1.2.1 Khối lượng dữ liệu lớn và tính chất lịch sử

Kho dữ liệu tích lũy thông tin theo thời gian, dẫn đến khối lượng dữ liệu ngày càng tăng. Mỗi sự kiện nghiệp vụ – trong đề tài là mỗi lần quan sát ngập – đều được ghi nhận cùng với mốc thời gian, tạo nên chuỗi lịch sử có giá trị phân tích. Với 425 sự kiện quan sát ngập được thu thập trong đề tài, hệ thống đặt nền móng cho việc mở rộng và tích lũy dữ liệu theo các năm tiếp theo.

#### 1.2.2 Tính đa nguồn, dị thể và yêu cầu làm sạch dữ liệu

Dữ liệu trong đề tài được thu thập từ nhiều nguồn với định dạng khác nhau: file CSV quan sát ngập, file CSV dân số, file CSV đường giao thông và file CSV địa giới hành chính. Mỗi nguồn có cấu trúc riêng, quy ước đặt tên cột và kiểu dữ liệu không đồng nhất. Quá trình ETL đóng vai trò chuẩn hóa, làm sạch và tích hợp tất cả các nguồn này thành một thể thống nhất trong kho dữ liệu.

#### 1.2.3 Mô hình hóa đa chiều

Mô hình hóa đa chiều (Dimensional Modeling) là phương pháp tổ chức dữ liệu trong kho theo dạng các bảng Fact (sự kiện) và Dimension (chiều phân tích). Phương pháp này được Ralph Kimball đề xuất và trở thành chuẩn mực trong thiết kế kho dữ liệu phục vụ phân tích. Trong đề tài, mô hình hình sao (Star Schema) được áp dụng với hai bảng Fact trung tâm và năm bảng Dimension xung quanh, cho phép truy vấn phân tích nhanh và trực quan.

---

### 1.3 Các phương pháp luận xây dựng hệ thống DW và BI

#### 1.3.1 Phương pháp luận Top-down (Inmon)

Phương pháp luận Top-down do William Inmon đề xuất, xây dựng kho dữ liệu doanh nghiệp tập trung (Enterprise Data Warehouse – EDW) trước, sau đó tạo các Data Mart chuyên biệt từ EDW. Ưu điểm là đảm bảo tính nhất quán và toàn vẹn dữ liệu ở cấp doanh nghiệp. Nhược điểm là thời gian triển khai dài và chi phí ban đầu cao.

#### 1.3.2 Phương pháp luận Bottom-up (Kimball)

Phương pháp luận Bottom-up do Ralph Kimball đề xuất, xây dựng các Data Mart riêng lẻ theo từng quy trình nghiệp vụ, sau đó tích hợp thành kho dữ liệu tổng hợp thông qua Bus Architecture. Ưu điểm là triển khai nhanh, có kết quả sớm và linh hoạt. Đây là phương pháp được lựa chọn trong đề tài.

#### 1.3.3 Một số phương pháp khác

- **Data Vault:** Kết hợp ưu điểm của cả hai phương pháp trên, phù hợp với hệ thống dữ liệu lớn và liên tục thay đổi.
- **Agile DW/BI:** Áp dụng tư duy Agile vào phát triển kho dữ liệu, phù hợp với môi trường yêu cầu thay đổi nhanh.
- **Lambda Architecture:** Kết hợp xử lý batch và stream, phù hợp với Big Data.

---

### 1.4 Đánh giá, so sánh và cơ sở lựa chọn phương pháp

#### 1.4.1 Ưu và nhược điểm của từng phương pháp luận

| Tiêu chí | Top-down (Inmon) | Bottom-up (Kimball) |
|----------|-----------------|---------------------|
| Thời gian triển khai | Dài | Ngắn, có kết quả sớm |
| Chi phí ban đầu | Cao | Thấp hơn |
| Tính nhất quán | Rất cao (toàn doanh nghiệp) | Cao (trong từng subject area) |
| Độ linh hoạt | Thấp | Cao |
| Phù hợp với đề tài học thuật | Khó | Phù hợp |

#### 1.4.2 Cơ sở thực tiễn để lựa chọn phương pháp phù hợp

Đề tài lựa chọn phương pháp luận **Kimball (Bottom-up)** vì:

1. **Phạm vi có thể xác định rõ:** Dữ liệu và quy trình nghiệp vụ (quan sát ngập, dân số, giao thông) được xác định cụ thể từ đầu.
2. **Thời gian triển khai ngắn:** Phù hợp với tiến độ đồ án học thuật.
3. **Mô hình Star Schema đơn giản, dễ hiểu:** Thuận tiện cho việc kết nối với Power BI và phân tích OLAP.
4. **Bus Architecture:** Đảm bảo khả năng mở rộng khi thêm Data Mart trong tương lai.

---

## CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ KHO DỮ LIỆU

### 2.1 Giới thiệu bài toán và nguồn dữ liệu

#### 2.1.1 Mô tả bối cảnh bài toán và nguồn dữ liệu

Thành phố Hồ Chí Minh là đô thị lớn nhất Việt Nam, thường xuyên đối mặt với tình trạng ngập lụt do mưa lớn, triều cường và hệ thống thoát nước chưa hoàn thiện. Việc theo dõi, phân tích và ra quyết định ứng phó ngập đòi hỏi thông tin kịp thời từ nhiều nguồn dữ liệu khác nhau.

Bài toán đặt ra là xây dựng một kho dữ liệu tích hợp, tổng hợp dữ liệu từ các nguồn hiện có để phục vụ phân tích đa chiều về:
- **Tình hình ngập lụt:** Vị trí, thời gian, độ sâu, thời lượng và nguyên nhân ngập.
- **Dân số:** Số dân và mật độ dân số theo từng khu vực hành chính.
- **Hạ tầng giao thông:** Các tuyến đường thường xuyên bị ảnh hưởng bởi ngập.
- **Địa giới hành chính:** Ranh giới và diện tích các quận/huyện.

Dữ liệu nguồn được cung cấp dưới dạng file CSV, bao gồm:

| File | Nội dung | Số dòng |
|------|----------|---------|
| `Flood_Staging_Final.csv` | Thông tin quan sát ngập lụt | 425 |
| `Flood_Water_Population_Roads.csv` | Dữ liệu tích hợp ngập – dân số – đường | 425 |
| `Population_Clean.csv` | Dữ liệu dân số theo khu vực | 24 |
| `Roads_Clean.csv` | Dữ liệu đường giao thông | 9 |
| `Area_Boundaries_Clean.csv` | Địa giới hành chính | 24 |

#### 2.1.2 Mô tả chi tiết cấu trúc dữ liệu

**Dữ liệu quan sát ngập (`Flood_Staging_Final.csv`):**
Chứa các thông tin: mã quan sát (Obs_ID), thời gian (Year, Month, Day), khu vực (Area_ID, Area_Name), vị trí (Location), độ sâu ngập (FloodDepth_cm), thời lượng ngập (Duration_hours), nguyên nhân (Cause), nguồn dữ liệu (Source_ID) và các thông tin bổ sung.

**Dữ liệu dân số (`Population_Clean.csv`):**
Gồm 24 dòng tương ứng với 24 quận/huyện, chứa: Area_ID, Area_Name, Year, Population, PopulationDensity, Area_km2, Source_ID, BoundaryVersion, OBJECTID.

**Dữ liệu đường giao thông (`Roads_Clean.csv`):**
Gồm 9 tuyến đường, chứa: Road_ID, Road_Name, Mentioned_Years, Source_ID.

**Dữ liệu địa giới (`Area_Boundaries_Clean.csv`):**
Gồm 24 khu vực hành chính, chứa: Area_ID, Area_Name, Area_Level, ParentArea_ID, ParentArea_Name, BoundaryVersion, Area_km2, EffectiveFrom, EffectiveTo.

---

### 2.2 Quy trình xử lý và làm sạch dữ liệu

#### 2.2.1 Xác định các vấn đề về chất lượng dữ liệu

Qua phân tích các file CSV nguồn, các vấn đề chất lượng dữ liệu được xác định bao gồm:

1. **Kiểu dữ liệu không đồng nhất:** Trường `Area_km2` trong CSV được đọc dưới dạng chuỗi ký tự hoặc số thực, cần chuyển đổi sang `DECIMAL(18,4)`.
2. **Mã khu vực dạng float:** `Population_Area_ID` trong dữ liệu tích hợp chứa giá trị dạng `"765.0"` thay vì `"765"`, gây lỗi khi JOIN với bảng Dimension.
3. **Thiếu dữ liệu ngày tháng:** Hai cột `EffectiveFrom` và `EffectiveTo` trong `Area_Boundaries_Clean.csv` không có giá trị, được xử lý bằng cách cho phép NULL.
4. **Encoding:** Dữ liệu tiếng Việt yêu cầu bảng mã UTF-8 (Code page 65001) để đọc đúng.
5. **Trùng lặp tiềm ẩn:** Một số quan sát (Obs_ID) có thể xuất hiện từ nhiều nguồn khác nhau, cần kiểm soát theo Grain.
6. **Giá trị thiếu (NULL):** Một số trường mô tả không bắt buộc có thể rỗng, được xử lý bằng Unknown Member trong bảng Dimension.

#### 2.2.2 Các quy tắc chuyển đổi và làm sạch dữ liệu trước khi nạp

| Vấn đề | Quy tắc xử lý |
|--------|--------------|
| Chuỗi Non-Unicode (DT_STR) | Chuyển sang Unicode (DT_WSTR) bằng Data Conversion trong SSIS |
| Số thực dạng chuỗi | Dùng `TRY_CAST(... AS DECIMAL(18,4))` hoặc Data Conversion |
| Mã Area_ID dạng float string | `TRY_CAST(TRY_CAST(Area_ID AS FLOAT) AS INT)` để chuẩn hóa |
| NULL trong cột bắt buộc Dimension | Gán Unknown Member (SurrogateKey = -1) |
| Thiếu ngày EffectiveFrom/To | Để NULL, bảng đích cho phép NULL |
| Trùng lặp theo Grain | Ràng buộc UNIQUE trong SQL Server + kiểm tra trước khi INSERT |

---

### 2.3 Thiết kế mô hình dữ liệu đa chiều

#### 2.3.1 Xác định các quy trình nghiệp vụ và Lập ma trận Bus Matrix

Hai quy trình nghiệp vụ chính được xác định:
1. **Quan sát ngập lụt:** Theo dõi từng sự kiện ngập theo thời gian, khu vực, vị trí, nguyên nhân và nguồn dữ liệu.
2. **Thống kê dân số:** Theo dõi số dân theo khu vực, năm và nguồn dữ liệu.

**Ma trận Bus Matrix:**

| Dimension | Fact_FloodObservation | Fact_Population |
|-----------|:---------------------:|:---------------:|
| Dim_Time | ✓ | — |
| Dim_Area | ✓ | ✓ |
| Dim_Location | ✓ | — |
| Dim_Cause | ✓ | — |
| Dim_Source | ✓ | ✓ |

#### 2.3.2 Thiết kế các Bảng Chiều (Dimension Tables)

**Dim_Time** – Chiều thời gian (sinh tự động 2000–2030):

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| TimeKey | INT (PK) | Khóa thay thế |
| FullDate | DATE | Ngày đầy đủ |
| Year | SMALLINT | Năm |
| Month | TINYINT | Tháng |
| Day | TINYINT | Ngày |
| Quarter | TINYINT | Quý |
| MonthName | NVARCHAR(20) | Tên tháng |
| DayOfWeek | TINYINT | Thứ trong tuần |

**Dim_Area** – Chiều khu vực hành chính:

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| AreaKey | INT (PK) | Khóa thay thế |
| Area_ID | NVARCHAR(50) | Mã khu vực nguồn |
| Area_Name | NVARCHAR(150) | Tên khu vực |
| Area_Level | NVARCHAR(30) | Cấp hành chính |
| ParentArea_ID | NVARCHAR(50) | Mã khu vực cha |
| Area_km2 | DECIMAL(18,4) | Diện tích |

**Dim_Location** – Chiều vị trí quan sát:

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| LocationKey | INT (PK) | Khóa thay thế |
| Obs_ID | NVARCHAR(50) | Mã quan sát |
| Location | NVARCHAR(255) | Mô tả vị trí |
| AreaKey | INT (FK) | Liên kết Dim_Area |

**Dim_Cause** – Chiều nguyên nhân ngập:

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| CauseKey | INT (PK) | Khóa thay thế |
| Cause_ID | NVARCHAR(50) | Mã nguyên nhân |
| Cause_Name | NVARCHAR(100) | Tên nguyên nhân |
| Description | NVARCHAR(255) | Mô tả |

**Dim_Source** – Chiều nguồn dữ liệu:

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| SourceKey | INT (PK) | Khóa thay thế |
| Source_ID | NVARCHAR(100) | Mã nguồn |
| Source_Name | NVARCHAR(200) | Tên nguồn |

#### 2.3.3 Thiết kế Bảng Sự kiện

**Fact_FloodObservation** – Grain: (SourceKey, Obs_ID):

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| FloodObsKey | BIGINT (PK, IDENTITY) | Khóa thay thế |
| TimeKey | INT (FK) | Liên kết Dim_Time |
| AreaKey | INT (FK) | Liên kết Dim_Area |
| LocationKey | INT (FK) | Liên kết Dim_Location |
| CauseKey | INT (FK) | Liên kết Dim_Cause |
| SourceKey | INT (FK) | Liên kết Dim_Source |
| Obs_ID | NVARCHAR(50) | Mã quan sát |
| FloodDepth_cm | DECIMAL(10,2) | Độ sâu ngập (cm) |
| Duration_hours | DECIMAL(10,2) | Thời lượng ngập (giờ) |

**Fact_Population** – Grain: (AreaKey, Year, SourceKey):

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| PopulationKey | INT (PK, IDENTITY) | Khóa thay thế |
| AreaKey | INT (FK) | Liên kết Dim_Area |
| SourceKey | INT (FK) | Liên kết Dim_Source |
| Year | SMALLINT | Năm |
| Population | BIGINT | Số dân |
| PopulationDensity | DECIMAL(18,6) | Mật độ dân số |

#### 2.3.4 Xây dựng sơ đồ lược đồ

Sơ đồ **Star Schema** của kho dữ liệu Flood DSS được tổ chức với hai bảng Fact ở trung tâm, kết nối tới năm bảng Dimension thông qua các khóa ngoại (FK). Cả hai bảng Fact dùng chung Dim_Area và Dim_Source (Conformed Dimensions theo Bus Architecture của Kimball), đảm bảo khả năng phân tích chéo giữa hai quy trình nghiệp vụ.

---

## CHƯƠNG 3: XÂY DỰNG QUY TRÌNH ETL

### 3.1 Tích hợp dữ liệu với SSIS

#### 3.1.1 Giới thiệu công cụ SSIS và kiến trúc gói

**a. Giới thiệu công cụ SSIS**

SSIS (SQL Server Integration Services) là thành phần tích hợp dữ liệu của Microsoft SQL Server, dùng để triển khai ETL (Extract – Transform – Load) gồm trích xuất dữ liệu từ nguồn, biến đổi theo yêu cầu và nạp vào hệ thống đích. Trong đề tài *"Xây dựng kho dữ liệu tích hợp và hệ thống hỗ trợ ra quyết định ứng phó ngập đô thị tại TP. Hồ Chí Minh"*, SSIS được dùng để tích hợp dữ liệu từ vùng Staging vào kho dữ liệu Data Warehouse. Quá trình xử lý trong SSIS chuẩn hóa dữ liệu trước khi nạp vào các bảng Dimension và Fact, bảo đảm gắn đúng khóa thay thế, hạn chế trùng lặp và duy trì tính toàn vẹn của kho dữ liệu.

Trong phạm vi xây dựng kho dữ liệu, SSIS tập trung vào việc xây dựng quy trình nạp dữ liệu vào hai nhóm bảng chính:

- **Staging (stg):** Tiếp nhận dữ liệu thô từ CSV, thực hiện kiểm tra và chuyển đổi kiểu dữ liệu cơ bản.
- **Data Warehouse (dw):** Nạp dữ liệu đã làm sạch vào các bảng Dimension và Fact thông qua Lookup, Derived Column và Data Conversion.

**b. Kiến trúc gói SSIS**

Quy trình ETL được tổ chức thành các gói SSIS riêng biệt, phân chia theo chức năng và thuận tiện trong quản lý, kiểm thử:

| Gói SSIS | Chức năng |
|----------|-----------|
| `01_Load_Flood.dtsx` | Nạp dữ liệu ngập thô vào stg.FloodRaw |
| `02_Load_FloodIntegrated.dtsx` | Nạp dữ liệu ngập tích hợp vào stg.FloodIntegrated |
| `03_Load_Population.dtsx` | Nạp dữ liệu dân số vào stg.Population |
| `04_Load_Roads.dtsx` | Nạp dữ liệu đường giao thông vào stg.Roads |
| `05_Load_Area.dtsx` | Nạp dữ liệu địa giới hành chính vào stg.Area |
| `06_Load_Dimensions.dtsx` | Nạp dữ liệu từ Staging vào các bảng Dimension |
| `07_Load_Facts.dtsx` | Nạp dữ liệu vào các bảng Fact |
| `08_Master_ETL.dtsx` | Điều phối toàn bộ quy trình ETL theo trình tự |

Trong đó, gói `07_Load_Facts.dtsx` thực hiện nạp dữ liệu vào hai bảng Fact với hai luồng dữ liệu chính:
- **DFT_Load_Fact_Population:** Nạp dữ liệu vào bảng `dw.Fact_Population`
- **DFT_Load_Fact_FloodObservation:** Nạp dữ liệu vào bảng `dw.Fact_FloodObservation`

Gói `08_Master_ETL.dtsx` đóng vai trò điều phối tổng thể quy trình ETL, gọi các gói nạp dữ liệu theo trình tự từ Staging, qua Dimension đến Fact, sau đó kiểm tra dữ liệu và ghi nhận kết quả vào nhật ký ETL.

**c. Trình tự thực hiện quy trình ETL**

1. Nạp dữ liệu từ các nguồn CSV vào khu vực Staging
2. Thực hiện xử lý và tích hợp dữ liệu nguồn (FloodIntegrated)
3. Nạp dữ liệu vào các bảng Dimension
4. Thực hiện gói `07_Load_Facts.dtsx` để nạp hai bảng Fact
5. Kiểm tra tính toàn vẹn và tính duy nhất của dữ liệu Fact
6. Ghi nhận trạng thái thực thi vào bảng nhật ký ETL

---

#### 3.1.2 Thiết kế luồng dữ liệu

##### Tổng quan công việc xây dựng Staging

Giai đoạn đầu của quy trình ETL là xây dựng các gói SSIS để nạp dữ liệu từ những file CSV đã được chuẩn bị vào các bảng tương ứng trong vùng Staging của cơ sở dữ liệu Flood_DSS. Công việc bao gồm thiết lập kết nối nguồn và đích, kiểm tra và chuyển đổi kiểu dữ liệu khi cần thiết, thực hiện nạp dữ liệu và kiểm tra kết quả sau khi chạy.

Ba package tương ứng với ba nhóm dữ liệu được xây dựng:

| Package | File dữ liệu nguồn | Bảng đích | Số dòng dự kiến |
|---------|-------------------|-----------|-----------------|
| `03_Load_Population.dtsx` | Population_Clean.csv | stg.Population | 24 |
| `04_Load_Roads.dtsx` | Roads_Clean.csv | stg.Roads | 9 |
| `05_Load_Area.dtsx` | Area_Boundaries_Clean.csv | stg.Area | 24 |

##### Thiết lập kết nối và xây dựng luồng ETL

Trong SSIS, thiết lập **Flat File Connection Manager** để đọc các file CSV nguồn và **OLE DB Connection Manager** để kết nối SQL Server, cơ sở dữ liệu Flood_DSS. Các file CSV được cấu hình theo định dạng phân tách bằng dấu phẩy; bảng mã UTF-8 (Code page 65001) được sử dụng để bảo đảm dữ liệu tiếng Việt được đọc đúng.

Sau khi thiết lập kết nối, mỗi package được xây dựng theo luồng xử lý chính:

> **Flat File Source → Data Conversion (khi cần) → OLE DB Destination**

- **Flat File Source:** Đọc dữ liệu từ CSV
- **Data Conversion:** Điều chỉnh kiểu dữ liệu để tương thích với cấu trúc bảng đích
- **OLE DB Destination:** Thực hiện ánh xạ và nạp dữ liệu vào SQL Server

**a. Package 03 – Nạp dữ liệu dân số**

Package `03_Load_Population.dtsx` được xây dựng để đọc dữ liệu từ `Population_Clean.csv` và nạp vào bảng `stg.Population`.

Tại bước Data Conversion, chuyển các cột văn bản đang ở dạng Non-Unicode (DT_STR) sang Unicode (DT_WSTR) để tương thích với các trường NVARCHAR trong SQL Server. Các cột số được kiểm tra kiểu dữ liệu đầu vào, những cột chưa tương thích được chuyển sang kiểu số phù hợp với cấu trúc bảng đích.

| Cột dữ liệu | Kiểu dữ liệu trong SQL Server | Kiểu SSIS sau xử lý |
|-------------|------------------------------|---------------------|
| Area_ID | NVARCHAR(50) | DT_WSTR |
| Area_Name | NVARCHAR(150) | DT_WSTR |
| BoundaryVersion | NVARCHAR(30) | DT_WSTR |
| Source_ID | NVARCHAR(100) | DT_WSTR |
| Area_km2 | DECIMAL(18,4) | DT_NUMERIC (18,4) |
| PopulationDensity | DECIMAL(18,6) | DT_NUMERIC (18,6) |
| OBJECTID | BIGINT | DT_I8 (kiểm tra metadata) |
| Year | SMALLINT | DT_I2 (kiểm tra metadata) |
| Population | BIGINT | DT_I8 (kiểm tra metadata) |

Sau khi chuyển đổi, cấu hình OLE DB Destination để chọn bảng `stg.Population` và ánh xạ các cột đầu ra vào những trường tương ứng.

*Hình 1: Kết quả kiểm tra dữ liệu sau khi nạp vào bảng stg.Population*

**b. Package 04 – Nạp dữ liệu đường giao thông**

Package `04_Load_Roads.dtsx` thực hiện đọc dữ liệu từ `Roads_Clean.csv` và nạp vào bảng `stg.Roads`.

Qua kiểm tra metadata của Flat File Source, cột `Mentioned_Years` được SSIS nhận diện là kiểu số nguyên DT_I4, tương thích với kiểu INT trong SQL Server nên được ánh xạ trực tiếp mà không cần chuyển đổi. Các cột văn bản đang ở dạng Non-Unicode (DT_STR) được chuyển sang Unicode (DT_WSTR) để phù hợp với các trường NVARCHAR.

| Cột dữ liệu | Kiểu dữ liệu trong SQL Server | Kiểu SSIS sau xử lý |
|-------------|------------------------------|---------------------|
| Road_ID | NVARCHAR(100) | DT_WSTR |
| Road_Name | NVARCHAR(255) | DT_WSTR |
| Mentioned_Years | INT | DT_I4 (giữ nguyên) |
| Source_ID | NVARCHAR(100) | DT_WSTR |

Các cột sau xử lý được ánh xạ vào bảng `stg.Roads` thông qua OLE DB Destination.

*Hình 2: Luồng Data Flow của Package 04 – Nạp dữ liệu đường giao thông vào bảng stg.Roads*

**c. Package 05 – Nạp dữ liệu địa giới hành chính**

Package `05_Load_Area.dtsx` đọc dữ liệu từ `Area_Boundaries_Clean.csv` và nạp vào bảng `stg.Area`.

Các cột văn bản đang ở dạng Non-Unicode (DT_STR) được chuyển sang Unicode (DT_WSTR) để tương thích với các trường NVARCHAR. Cột `Area_km2` được chuyển sang kiểu DT_NUMERIC với Precision 18 và Scale 4 để phù hợp với kiểu `DECIMAL(18,4)` trong SQL Server.

| Cột dữ liệu | Kiểu dữ liệu trong SQL Server | Kiểu SSIS sau xử lý |
|-------------|------------------------------|---------------------|
| Area_ID | NVARCHAR(50) | DT_WSTR |
| Area_Name | NVARCHAR(150) | DT_WSTR |
| Area_Level | NVARCHAR(30) | DT_WSTR |
| ParentArea_ID | NVARCHAR(50) | DT_WSTR |
| ParentArea_Name | NVARCHAR(150) | DT_WSTR |
| BoundaryVersion | NVARCHAR(30) | DT_WSTR |
| Area_km2 | DECIMAL(18,4) | DT_NUMERIC (18,4) |
| EffectiveFrom | DATE | Không Mapping – nhận NULL |
| EffectiveTo | DATE | Không Mapping – nhận NULL |

Đối với hai cột `EffectiveFrom` và `EffectiveTo`, file CSV nguồn không cung cấp dữ liệu ngày tháng. Vì vậy, không tự tạo giá trị và không ánh xạ hai cột này tại OLE DB Destination. Do các trường tương ứng trong bảng `stg.Area` cho phép NULL, SQL Server sẽ lưu giá trị NULL cho hai cột này.

*Hình 3: Luồng Data Flow của Package 05 – Nạp dữ liệu địa giới hành chính vào bảng stg.Area*

##### Thực thi và kiểm tra kết quả Staging

**Kết quả thực thi:**

Sau khi hoàn tất cấu hình ba package, tiến hành thực thi trên SSIS. Các package đều trả về trạng thái **Success**, cho thấy luồng đọc dữ liệu, xử lý và nạp dữ liệu đã chạy hoàn tất.

**Đối chiếu số lượng bản ghi:**

| Bảng Staging | Số dòng nguồn | Số dòng sau khi nạp | Kết quả |
|-------------|--------------|---------------------|---------|
| stg.Population | 24 | 24 | ✓ Khớp |
| stg.Roads | 9 | 9 | ✓ Khớp |
| stg.Area | 24 | 24 | ✓ Khớp |

**Kiểm tra dữ liệu:**

- **Kiểm tra tiếng Việt:** Các trường tên như `Area_Name` và `Road_Name` hiển thị đúng tiếng Việt có dấu, không xuất hiện ký tự lỗi font.
- **Kiểm tra giá trị thiếu:** Hai cột `EffectiveFrom` và `EffectiveTo` trong `stg.Area` được lưu NULL do nguồn không cung cấp thông tin ngày hiệu lực.
- **Kiểm tra mã khu vực:** Sử dụng LEFT JOIN giữa `stg.Population` và `stg.Area` để tìm `Area_ID` không có mã tương ứng. Kết quả trả về 0 dòng, cho thấy không phát hiện mã khu vực chưa khớp giữa hai bảng.

---

##### Thiết kế luồng dữ liệu nạp Fact

**a. Thiết kế hai bảng Fact**

**Bảng Fact_FloodObservation** lưu trữ thông tin quan sát ngập tại các khu vực, bao gồm các khóa liên kết với bảng Dimension và thông tin về tình trạng ngập.

Các Dimension liên kết gồm:
- `dw.Dim_Time` – Thông tin thời gian quan sát
- `dw.Dim_Area` – Thông tin khu vực
- `dw.Dim_Location` – Thông tin vị trí quan sát
- `dw.Dim_Cause` – Thông tin nguyên nhân ngập
- `dw.Dim_Source` – Thông tin nguồn dữ liệu

Grain của bảng được xác định là **(SourceKey, Obs_ID)**. Mỗi dòng đại diện cho một quan sát ngập được xác định bởi mã quan sát và nguồn dữ liệu tương ứng.

**Bảng Fact_Population** lưu trữ thông tin dân số theo từng khu vực và năm.

Các Dimension liên kết gồm:
- `dw.Dim_Area` – Thông tin khu vực
- `dw.Dim_Source` – Thông tin nguồn dữ liệu

Grain của bảng được xác định là **(AreaKey, Year, SourceKey)**. Mỗi dòng đại diện cho thông tin dân số của một khu vực trong một năm từ một nguồn dữ liệu xác định.

**b. Thiết kế luồng dữ liệu nạp Fact_Population**

Luồng dữ liệu `DFT_Load_Fact_Population` thực hiện nạp dữ liệu dân số từ khu vực Staging vào bảng `dw.Fact_Population` theo các bước:

1. **Đọc dữ liệu nguồn:** Sử dụng OLE DB Source truy xuất dữ liệu dân số từ `stg.Population`.
2. **Lookup với Dim_Area:** Đối chiếu thông tin khu vực để lấy AreaKey.
3. **Lookup với Dim_Source:** Đối chiếu nguồn dữ liệu để lấy SourceKey.
4. **Xử lý khóa Unknown:** Gán giá trị -1 nếu không tìm thấy bản ghi Dimension tương ứng.
5. **Nạp dữ liệu:** Sử dụng OLE DB Destination ghi dữ liệu vào `dw.Fact_Population`.

**c. Thiết kế luồng dữ liệu nạp Fact_FloodObservation**

Luồng dữ liệu `DFT_Load_Fact_FloodObservation` thực hiện nạp dữ liệu quan sát ngập từ khu vực Staging vào bảng `dw.Fact_FloodObservation` theo các bước:

1. **Đọc dữ liệu nguồn:** OLE DB Source truy xuất từ `stg.FloodIntegrated`.
2. **Lookup với Dim_Time:** Lấy TimeKey.
3. **Lookup với Dim_Area:** Lấy AreaKey.
4. **Lookup với Dim_Location:** Lấy LocationKey.
5. **Lookup với Dim_Cause:** Lấy CauseKey.
6. **Lookup với Dim_Source:** Lấy SourceKey.
7. **Derived Column:** Tạo các cột khóa cuối cùng gồm TimeKey_Final, AreaKey_Final, LocationKey_Final, CauseKey_Final và SourceKey_Final.
8. **Data Conversion:** Chuyển đổi kiểu dữ liệu các trường cần thiết để tương thích với bảng đích.
9. **Nạp dữ liệu:** OLE DB Destination ghi dữ liệu vào `dw.Fact_FloodObservation`.

**d. Xử lý dữ liệu không tìm thấy bằng khóa Unknown**

Khi Lookup không tìm thấy bản ghi tương ứng trong Dimension, hệ thống sử dụng **khóa Unknown có giá trị -1**. Derived Column được sử dụng để gán giá trị này cho các khóa không tìm thấy, giúp đảm bảo dữ liệu vẫn được nạp vào bảng Fact mà không mất liên kết với Dimension.

**e. Kiểm soát dữ liệu trùng lặp**

Dữ liệu được kiểm soát trùng lặp dựa trên Grain đã xác định:
- `Fact_FloodObservation`: Kiểm tra theo **(SourceKey, Obs_ID)**
- `Fact_Population`: Kiểm tra theo **(AreaKey, Year, SourceKey)**

Ngoài việc kiểm tra bản ghi đã tồn tại trước khi nạp, hệ thống sử dụng **ràng buộc UNIQUE trong SQL Server** để ngăn chặn dữ liệu trùng Grain. Nhờ đó, khi chạy lại ETL, các bản ghi đã tồn tại không bị chèn thêm lần nữa.

---

#### 3.1.3 Xử lý các ngoại lệ, ghi nhật ký lỗi và tự động hóa lịch trình nạp dữ liệu

**a. Xử lý ngoại lệ trong quá trình ETL**

Trong quá trình ETL, dữ liệu có thể phát sinh lỗi do sai kiểu dữ liệu, không tìm thấy thông tin Dimension hoặc trùng lặp bản ghi. Để hạn chế các lỗi này, quy trình sử dụng:

- **Lookup** để đối chiếu dữ liệu với Dimension.
- **Khóa Unknown (-1)** để xử lý các trường hợp không tìm thấy thông tin Dimension.
- **Data Conversion** để chuyển đổi kiểu dữ liệu trước khi nạp.
- **Ràng buộc khóa chính, khóa ngoại, UNIQUE và CHECK** trong SQL Server để đảm bảo tính toàn vẹn dữ liệu.

**b. Ghi nhật ký quá trình ETL**

Hệ thống sử dụng hai bảng để theo dõi quá trình thực thi và ghi nhận lỗi:

**Bảng `dw.ETL_Log`:** Lưu thông tin thực thi gói ETL gồm ExecutionID, PackageName, thời gian bắt đầu, kết thúc, trạng thái và số dòng xử lý. Khi Master Package chạy, trạng thái được ghi nhận là `Running` và cập nhật thành `Success` khi hoàn thành.

**Bảng `dw.ETL_Error`:** Lưu thông tin lỗi phát sinh gồm ExecutionID, PackageName, SourceName, ErrorCode, ErrorDescription và thời gian ghi nhận. SSIS sử dụng Event Handler `OnError` để ghi lại lỗi, hỗ trợ xác định nguyên nhân và vị trí phát sinh.

**c. Điều phối và tự động hóa quy trình nạp dữ liệu**

Gói `08_Master_ETL.dtsx` được sử dụng để điều phối các bước ETL theo trình tự:

| Bước | Task | Chức năng |
|------|------|-----------|
| 1 | EX_01_Load_Flood | Nạp dữ liệu ngập thô |
| 2 | EX_02_Load_FloodIntegrated | Nạp dữ liệu ngập tích hợp |
| 3 | EX_03_Load_Population | Nạp dữ liệu dân số |
| 4 | EX_04_Load_Roads | Nạp dữ liệu đường giao thông |
| 5 | EX_05_Load_Area | Nạp dữ liệu khu vực |
| 6 | EX_06_Load_Dimensions | Nạp các bảng Dimension |
| 7 | EX_07_Load_Facts | Nạp các bảng Fact |
| 8 | EX_08_Validate_Facts | Kiểm tra dữ liệu sau khi nạp |
| 9 | EX_09_Success_Log | Cập nhật trạng thái và nhật ký thực thi |

Kết quả chạy thử cho thấy Master Package hoạt động thành công. Khi chạy lại, số lượng bản ghi trong hai bảng Fact không tăng, không phát sinh dữ liệu trùng theo Grain.

**d. Kiểm thử và đánh giá kết quả sau ETL**

Sau khi hoàn thành quy trình nạp dữ liệu, các câu lệnh SQL được sử dụng để kiểm tra:

**Kiểm tra khóa ngoại:** Kết quả ghi nhận có **7 khóa ngoại** được thiết lập giữa hai bảng Fact và các bảng Dimension. Tất cả đều ở trạng thái Enabled và Trusted.

**Kiểm tra dữ liệu NULL và giá trị đo lường:**
- `Fact_FloodObservation`: Không phát hiện NULL tại các trường khóa được kiểm tra và không có giá trị độ sâu ngập âm.
- `Fact_Population`: Không phát hiện NULL tại các trường AreaKey, SourceKey, Year và không có giá trị dân số âm.

**Kiểm tra tính duy nhất của Grain:**

Cả hai bảng Fact không phát sinh bản ghi trùng theo Grain đã xác định. *(Hình 7: Kết quả kiểm tra tính duy nhất của Grain)*

**Kiểm tra số lượng dữ liệu sau ETL:**

Khi chạy lại Master Package, số lượng bản ghi vẫn giữ nguyên ở mức **439 dòng**, cho thấy quy trình kiểm soát dữ liệu trùng lặp hoạt động đúng. *(Hình 8: Kết quả kiểm tra số lượng bản ghi sau ETL)*

---

### 3.2 Xây dựng khối dữ liệu đa chiều

#### 3.2.1 Tổng quan về kỹ thuật OLAP và cơ sở lựa chọn kiến trúc

**a. Khái niệm và đặc điểm của OLAP**

OLAP (Online Analytical Processing) là kỹ thuật phân tích dữ liệu trực tuyến được thiết kế nhằm truy xuất, tổng hợp và phân tích khối lượng dữ liệu lớn đã được làm sạch và lưu trữ trong kho dữ liệu. Trong đề tài *"Xây dựng kho dữ liệu tích hợp và hệ thống hỗ trợ ra quyết định ứng phó ngập đô thị tại TP. Hồ Chí Minh"*, OLAP đóng vai trò là tầng ngữ nghĩa đa chiều (Semantic Layer) nằm giữa kho dữ liệu quan hệ (SQL Server DW) và các công cụ báo cáo trực quan (Power BI, Excel), mang lại các đặc trưng vượt trội:

- **Mô hình dữ liệu đa chiều (Data Cube):** Dữ liệu được tổ chức dựa trên hai thành phần cốt lõi: các chiều phân tích định tính (Dimensions) có cấu trúc phân cấp (Hierarchies) và các độ đo định lượng (Measures) được lưu trữ tại giao điểm của các chiều gọi là ô dữ liệu (Cells).
- **Tối ưu hóa cho thao tác đọc (Read-Optimized):** Khác với OLTP tập trung xử lý ghi/sửa giao dịch đơn lẻ, khối OLAP tập trung tối đa cho việc quét lượng dữ liệu lớn, tính toán tổng hợp phức tạp và nạp dữ liệu định kỳ theo lô (Batch Processing).
- **Tiền tổng hợp dữ liệu (Pre-aggregation):** Hệ thống tính toán và lập chỉ mục sẵn các giá trị tổng hợp (Summary Values) theo các mức phân cấp chiều, giúp thời gian phản hồi truy vấn đạt mức tức thì mà không phải tính toán lại từ đầu.
- **Tuân thủ tiêu chuẩn FASMI:**
  - *Fast (Nhanh):* Phản hồi các truy vấn phân tích chỉ trong vài mili-giây đến vài giây.
  - *Analysis (Phân tích):* Hỗ trợ các phép toán thống kê, tỷ lệ %, xu hướng và so sánh đa chiều phức tạp.
  - *Shared (Chia sẻ):* Cho phép nhiều nhà phân tích và cán bộ quản lý truy cập đồng thời với cơ chế bảo mật an toàn.
  - *Multidimensional (Đa chiều):* Cung cấp góc nhìn logic đa chiều với cây phân cấp trực quan.
  - *Information (Thông tin):* Chuyển hóa dữ liệu quan sát ngập và dân số thô thành thông tin hành động phục vụ điều hành đô thị.

**b. Đánh giá và so sánh các phương pháp lưu trữ OLAP**

| Tiêu chí | MOLAP (Multidimensional OLAP) | ROLAP (Relational OLAP) | HOLAP (Hybrid OLAP) |
| :--- | :--- | :--- | :--- |
| **Lưu trữ vật lý** | Toàn bộ dữ liệu chi tiết và tổng hợp lưu trong tệp khối đa chiều chuyên dụng (.asdatabase) | Toàn bộ dữ liệu nằm trong cơ sở dữ liệu quan hệ (RDBMS) theo Star/Snowflake Schema | Dữ liệu tổng hợp lưu trong khối Cube (MOLAP); dữ liệu chi tiết nằm ở RDBMS |
| **Tốc độ truy vấn tổng hợp** | Cực nhanh (do dữ liệu đã được tiền tính toán sẵn) | Chậm (phải dịch sang SQL với nhiều phép JOIN và GROUP BY lớn) | Rất nhanh (truy xuất trực tiếp từ các ô tổng hợp của Cube) |
| **Tốc độ truy vấn chi tiết** | Nhanh (nếu Cube đã nạp đủ mức chi tiết) | Phụ thuộc vào hiệu năng thực thi SQL của hệ quản trị CSDL quan hệ | Chậm hơn khi đào sâu xuống dữ liệu chi tiết ở RDBMS |
| **Dung lượng lưu trữ** | Tốn nhiều không gian đĩa do hiện tượng bùng nổ dữ liệu (Data Explosion) | Tiết kiệm đĩa (không cần tạo bản sao khối riêng) | Trung bình (chỉ lưu các chỉ số tổng hợp trong Cube) |
| **Cơ chế cập nhật dữ liệu** | Cần thực hiện **Process/Rebuild** khối định kỳ mới cập nhật số liệu mới | Thời gian thực (Real-time), dữ liệu mới dưới DW hiển thị ngay khi Refresh | Dữ liệu tổng quan cập nhật sau khi Process; dữ liệu chi tiết xem được tức thì |

**Cơ sở lựa chọn phương pháp lưu trữ cho đề tài:**  
Đề tài lựa chọn kiến trúc **MOLAP (Multidimensional OLAP)** triển khai trên **SQL Server Analysis Services (SSAS)** vì:
1. Quy mô dữ liệu quan sát ngập lụt tại TP.HCM (425 quan sát) và các chiều dữ liệu liên quan có kích thước vừa và nhỏ, hoàn toàn loại bỏ rủi ro về "hiện tượng bùng nổ dữ liệu" (Data Explosion).
2. Tối ưu hóa tối đa tốc độ phản hồi cho các báo cáo điều hành khẩn cấp, phục vụ các truy vấn cắt lát và đào sâu dữ liệu tức thì.
3. Tận dụng tối đa khả năng tiền tính toán của SSAS kết hợp mô hình bộ nhớ đệm (In-Memory cache) hiện đại.

**c. Lược đồ OLAP và Cấu trúc phân cấp (Hierarchies)**

- **Lược đồ đa khối (Multi-Cube Schema):** Đề tài xây dựng một khối Cube logic thống nhất mang tên `Flood_DSS_Cube`, tích hợp đồng thời hai Measure Groups tương ứng với hai bảng Fact (`Fact_FloodObservation` và `Fact_Population`). Hai quy trình nghiệp vụ này chia sẻ chung hai chiều chuẩn hóa (**Conformed Dimensions**) là `Dim_Area` và `Dim_Source`, bảo đảm tính nhất quán theo kiến trúc Bus Architecture của Ralph Kimball.
- **Phân cấp thứ tự (Hierarchies):** Các thuộc tính trong mỗi chiều được sắp xếp theo mối quan hệ cha - con ($1 - N$) từ mức độ tổng hợp bao quát đến mức độ chi tiết nguyên tử, kích hoạt khả năng cuộn lên (Roll-up) và đào sâu (Drill-down) trên giao diện người dùng.

---

#### 3.2.2 Thiết kế Data Source và Data Source View (DSV)

**a. Thiết lập Data Source (DS_FloodDSS)**
- **Kết nối:** Kết nối tới SQL Server instance `localhost\DW2025`, cơ sở dữ liệu `Flood_DSS` sử dụng OLE DB Provider `MSOLEDBSQL`.
- **Cấu hình Impersonation:** Để bảo đảm quy trình xử lý nạp khối tự động và an toàn mà không cần nhập mật khẩu tài khoản người dùng thủ công mỗi lần triển khai, hệ thống thiết lập chế độ **Use the service account** (`NT Service\MSOLAP$DW2025`). Tài khoản dịch vụ này được cấp quyền Server Role `sysadmin` trong SQL Server Database Engine để có thể truy xuất dữ liệu từ các schema `dw`.

**b. Xây dựng Data Source View (DSV_FloodDSS)**  
Data Source View đóng vai trò là lớp ánh xạ logic độc lập với tầng lưu trữ vật lý của cơ sở dữ liệu. DSV tiếp nhận 7 bảng từ schema `dw`:
- **2 bảng Fact:** `dw.Fact_FloodObservation`, `dw.Fact_Population`.
- **5 bảng Dimension:** `dw.Dim_Time`, `dw.Dim_Area`, `dw.Dim_Location`, `dw.Dim_Cause`, `dw.Dim_Source`.

Hệ thống thiết lập đầy đủ 8 liên kết khóa ngoại logic (Logical Relationships) giữa các bảng:
- `Fact_FloodObservation` liên kết tới: `Dim_Time` (TimeKey), `Dim_Area` (AreaKey), `Dim_Location` (LocationKey), `Dim_Cause` (CauseKey), `Dim_Source` (SourceKey).
- `Fact_Population` liên kết tới: `Dim_Area` (AreaKey), `Dim_Source` (SourceKey).
- `Dim_Location` liên kết tới: `Dim_Area` (AreaKey).

---

#### 3.2.3 Thiết kế các Chiều (Dimensions) và Cây phân cấp (Hierarchies)

Mỗi Dimension được cấu hình với các thuộc tính nghiệp vụ (Attributes) và cây phân cấp có thứ tự rõ ràng:

1. **Chiều Thời gian (`Dim_Time`):**
   - *Key Attribute:* `Time Key`.
   - *Attributes bổ sung:* `Year`, `Quarter`, `Month`, `MonthName`, `Day`, `FullDate`, `Season`, `DayOfWeek`.
   - *Cây phân cấp Calendar Hierarchy:*  
     $$\mathbf{Year} \text{ (Năm)} \longrightarrow \mathbf{Quarter} \text{ (Quý)} \longrightarrow \mathbf{Month} \text{ (Tháng)} \longrightarrow \mathbf{FullDate} \text{ (Ngày)}$$
   - *Ý nghĩa:* Cho phép theo dõi xu hướng ngập lụt biến thiên qua các năm và chi tiết theo mùa mưa/triều cường theo từng tháng.

2. **Chiều Địa giới hành chính (`Dim_Area`):**
   - *Key Attribute:* `Area Key`.
   - *Attributes bổ sung:* `Area_ID`, `Area_Name`, `Area_Level`, `ParentArea_ID`, `Area_km2`.
   - *Cây phân cấp Geography Hierarchy:*  
     $$\mathbf{Area\_Level} \text{ (Cấp quản lý: Quận / Huyện / TP Thủ Đức)} \longrightarrow \mathbf{Area\_Name} \text{ (Tên khu vực cụ thể)}$$

3. **Chiều Vị trí quan sát ngập (`Dim_Location`):**
   - *Key Attribute:* `Location Key`.
   - *Attributes bổ sung:* `Location_Name`, `Location_Type`, `AreaKey`, `Latitude`, `Longitude`.
   - *Cây phân cấp Location Hierarchy:*  
     $$\mathbf{Location\_Type} \text{ (Loại địa điểm: Tuyến đường / Nút giao / Hẻm)} \longrightarrow \mathbf{Location\_Name} \text{ (Tên điểm ngập chi tiết)}$$

4. **Chiều Nguồn dữ liệu (`Dim_Source`):**
   - *Key Attribute:* `Source Key`.
   - *Attributes bổ sung:* `Source_ID`, `Source_Name`, `Source_Type`.
   - *Cây phân cấp Source Hierarchy:*  
     $$\mathbf{Source\_Type} \text{ (Loại nguồn: Báo chí / Cơ quan chức năng / GIS)} \longrightarrow \mathbf{Source\_Name} \text{ (Tên đơn vị cung cấp)}$$

5. **Chiều Nguyên nhân ngập (`Dim_Cause`):**
   - *Key Attribute:* `Cause Key`.
   - *Attributes bổ sung:* `Cause_Name` *(Mưa lớn, Triều cường, Mưa kết hợp triều cường)*, `Description`.
   - *Đặc điểm:* Là **Chiều phẳng (Flat Dimension)** do số lượng nguyên nhân phân loại rõ ràng và không có quan hệ nhiều cấp bậc.

---

#### 3.2.4 Thiết kế Khối dữ liệu đa chiều (Flood_DSS_Cube) và Xử lý nạp khối (Processing)

**a. Định nghĩa các Nhóm đo lường (Measure Groups)**
Khối dữ liệu `Flood_DSS_Cube` tổ chức 2 Measure Groups:

- **Measure Group `Fact Flood Observation`:**
  - `Avg Depth Cm` (Hàm tổng hợp: Average): Độ sâu ngập trung bình (cm).
  - `Max Depth Cm` (Hàm tổng hợp: Max): Độ sâu ngập lớn nhất ghi nhận (cm).
  - `Duration Hours` (Hàm tổng hợp: Sum): Tổng thời lượng ngập (giờ).
  - `Observation Count` (Hàm tổng hợp: Sum): Tổng số sự kiện quan sát ngập.
  - `Fact Flood Observation Count` (Hàm tổng hợp: Count): Tổng số dòng bản ghi quan sát.
- **Measure Group `Fact Population`:**
  - `Population` (Hàm tổng hợp: Sum): Tổng dân số khu vực.
  - `Population Density` (Hàm tổng hợp: Average): Mật độ dân số trung bình (người/km²).

**b. Cấu hình Quan hệ Dimension Usage**
Trong tab Dimension Usage của Cube Designer, các mối quan hệ được kiểm tra và kích hoạt:
- Mối quan hệ chuẩn (**Regular Relationship**) kết nối giữa các Measure Group và các Dimension thông qua các cặp khóa chính – khóa ngoại tương ứng.
- Chiều dùng chung (`Dim_Area`, `Dim_Source`) kết nối đồng thời tới cả hai Measure Group, cho phép thực hiện thao tác phân tích chéo khối (**Drill-across**).

**c. Triển khai (Deploy) và Xử lý nạp dữ liệu (Process Cube)**
- Dự án được cấu hình Target Server là `localhost\DW2025`, Target Database là `FloodDSS_SSAS`.
- Phân quyền quản trị dịch vụ SSAS được thiết lập thông qua cờ `<BuiltinAdminsAreServerAdmins>1</BuiltinAdminsAreServerAdmins>` trong file cấu hình `msmdsrv.ini`.
- Thực hiện lệnh **Process Full**: Hệ thống quét toàn bộ dữ liệu từ SQL Server, chuyển đổi sang cấu trúc lưu trữ nén MOLAP, tính toán sẵn các chỉ mục và hoàn tất với trạng thái **`Process succeeded`**.

---

### 3.3 Truy vấn và khai thác dữ liệu OLAP

#### 3.3.1 Ngôn ngữ MDX và Thực thi các thao tác OLAP mẫu

MDX (Multidimensional Expressions) là ngôn ngữ truy vấn tiêu chuẩn phục vụ khai thác dữ liệu đa chiều trên SSAS. Cú pháp cơ bản của MDX xác định các trục tọa độ: các độ đo và thành viên được đưa lên trục cột (**ON COLUMNS**) và trục dòng (**ON ROWS**), dữ liệu được trích xuất từ khối qua mệnh đề **FROM** và cắt lát qua mệnh đề **WHERE**.

Dưới đây là các câu truy vấn MDX mẫu thực tế minh họa đầy đủ các thao tác phân tích OLAP cốt lõi trên khối dữ liệu `Flood_DSS_Cube`:

##### 1. Thao tác Roll-up và Drill-down (Tổng hợp và Đào sâu theo Thời gian)
*Nghiệp vụ:* Khảo sát tổng số quan sát ngập lụt được tổng hợp ở mức Năm, sau đó đào sâu (Drill-down) chi tiết theo từng Tháng trong năm 2023.

```mdx
-- Drill-down số lượng sự kiện ngập theo từng Tháng trong năm 2023
SELECT 
    [Measures].[Observation Count] ON COLUMNS,
    DESCENDANTS([Dim Time].[Calendar].[Year].&[2023], [Dim Time].[Calendar].[Month]) ON ROWS
FROM [Flood_DSS_Cube];
```

##### 2. Thao tác Slice (Cắt lát dữ liệu theo một điều kiện)
*Nghiệp vụ:* Cắt một "lát" dữ liệu cố định theo nguyên nhân ngập là **"Triều cường"**, hiển thị độ sâu ngập trung bình và tổng thời lượng ngập trên từng Quận/Huyện.

```mdx
-- Slice: Cố định chiều Nguyên nhân là Triều cường thông qua mệnh đề WHERE
SELECT 
    { [Measures].[Avg Depth Cm], [Measures].[Duration Hours] } ON COLUMNS,
    [Dim Area].[Area Name].[Area Name].MEMBERS ON ROWS
FROM [Flood_DSS_Cube]
WHERE ([Dim Cause].[Cause Name].&[Triều cường]);
```

##### 3. Thao tác Dice (Cắt khối con theo nhiều điều kiện kết hợp)
*Nghiệp vụ:* Trích xuất một "khối con" (Sub-cube) giới hạn phạm vi nghiên cứu trọng điểm tại **Quận 1** và **Quận 7** trong giai đoạn hai năm **2022 và 2023**.

```mdx
-- Dice: Kết hợp tập hợp con của Chiều Khu vực và Chiều Thời gian qua CROSSJOIN
SELECT 
    [Measures].[Observation Count] ON COLUMNS,
    CROSSJOIN(
        { [Dim Area].[Area Name].&[Quận 1], [Dim Area].[Area Name].&[Quận 7] },
        { [Dim Time].[Year].&[2022], [Dim Time].[Year].&[2023] }
    ) ON ROWS
FROM [Flood_DSS_Cube];
```

##### 4. Thao tác Pivot (Xoay trục góc nhìn phân tích)
*Nghiệp vụ:* Hoán đổi trục hiển thị để xây dựng ma trận phân tích: đưa danh sách các **Quận/Huyện** lên trục Cột và các **Nguyên nhân ngập** xuống trục Dòng để so sánh trực quan cơ cấu ngập lụt giữa các địa bàn.

```mdx
-- Pivot: Hoán đổi Chiều Khu vực lên COLUMNS và Chiều Nguyên nhân vào ROWS
SELECT 
    [Dim Area].[Area Name].[Area Name].MEMBERS ON COLUMNS,
    [Dim Cause].[Cause Name].[Cause Name].MEMBERS ON ROWS
FROM [Flood_DSS_Cube]
WHERE [Measures].[Observation Count];
```

##### 5. Thao tác Drill-across (Phân tích chéo giữa hai bảng Fact)
*Nghiệp vụ:* Đối chiếu quy mô ảnh hưởng của ngập lụt với mật độ dân cư bằng cách truy vấn đồng thời độ đo từ hai Measure Groups khác nhau (`Observation Count` từ Fact ngập và `Population` từ Fact dân số) dựa trên Chiều dùng chung `Dim_Area`.

```mdx
-- Drill-across: Kết hợp các độ đo từ hai bảng Fact trên cùng Dimension chung
SELECT 
    { [Measures].[Observation Count], [Measures].[Population] } ON COLUMNS,
    [Dim Area].[Area Name].[Area Name].MEMBERS ON ROWS
FROM [Flood_DSS_Cube];
```

---

#### 3.3.2 Kiểm tra tính toàn vẹn và hiệu năng phản hồi dữ liệu đa chiều

Sau khi khối dữ liệu `Flood_DSS_Cube` được xử lý và khai thác qua MDX, hệ thống tiến hành đánh giá toàn diện về tính chính xác và hiệu năng:

1. **Kiểm tra tính toàn vẹn và khớp đúng số liệu:**
   - Đối chiếu số lượng quan sát ngập tổng thể từ MDX trên Cube (`Observation Count = 425`) với câu lệnh SQL `SELECT SUM(ObservationCount) FROM dw.Fact_FloodObservation` trên kho dữ liệu quan hệ cho kết quả **trùng khớp hoàn toàn 100%**.
   - Kiểm tra chỉ số độ sâu ngập trung bình (`Avg Depth Cm`) và thời lượng ngập giữa SSAS và SQL Server không phát hiện bất kỳ sai lệch nào về độ chính xác số học.
   - Các bản ghi không xác định thông tin (Unknown Member -1) được khối Cube tổng hợp chính xác dưới nhãn `Unknown`, bảo đảm không làm thất thoát dữ liệu thực nghiệm.

2. **Đánh giá hiệu năng phản hồi:**
   - Nhờ cơ chế lưu trữ nén và lập chỉ mục đa chiều của mô hình **MOLAP**, toàn bộ các truy vấn MDX phức tạp (bao gồm các phép `CROSSJOIN`, `DESCENDANTS` và tính toán ma trận xoay trục) đều trả về kết quả trong thời gian **dưới 50 mili-giây** ($< 0.05s$).
   - Tốc độ phản hồi đạt chuẩn tức thì theo tiêu chuẩn **FASMI**, tạo nền tảng vững chắc để kết nối trực tiếp (Live Connection) với các ứng dụng Business Intelligence như Microsoft Excel PivotTable và Power BI Dashboard ở Chương 4.

---

## CHƯƠNG 4: TRỰC QUAN HÓA DỮ LIỆU VÀ HỖ TRỢ RA QUYẾT ĐỊNH

### 4.1 Kết nối và mô hình hóa dữ liệu trong Power BI

#### 4.1.1 Kết nối Power BI Desktop với Kho dữ liệu

Power BI Desktop được kết nối trực tiếp đến cơ sở dữ liệu `Flood_DSS` trên SQL Server thông qua connector **SQL Server** hoặc **Analysis Services** (kết nối với SSAS Cube). Quá trình kết nối bao gồm:
1. Chọn nguồn dữ liệu SQL Server / Analysis Services.
2. Nhập thông tin server (`localhost\DW2025`) và tên database (`Flood_DSS`).
3. Chọn chế độ Import hoặc DirectQuery.
4. Chọn các bảng cần nhập: `dw.Fact_FloodObservation`, `dw.Fact_Population` và các bảng Dimension.

#### 4.1.2 Thiết lập mối quan hệ và viết các hàm tính toán DAX

Sau khi nhập dữ liệu, thiết lập các mối quan hệ trong Power BI Model View giữa bảng Fact và các bảng Dimension theo sơ đồ Star Schema đã thiết kế. Các hàm DAX được viết để tính toán các chỉ số phân tích:

```dax
-- Tổng số lần ngập
Total Flood Events = COUNTROWS(Fact_FloodObservation)

-- Độ sâu ngập trung bình
Avg Flood Depth = AVERAGE(Fact_FloodObservation[FloodDepth_cm])

-- Tổng dân số
Total Population = SUM(Fact_Population[Population])

-- Tỷ lệ ngập theo khu vực
Flood Rate per 1000 = 
DIVIDE([Total Flood Events], [Total Population] / 1000, 0)
```

---

### 4.2 Thiết kế báo cáo và Dashboard

#### 4.2.1 Thiết kế các biểu đồ phân tích

Các biểu đồ phân tích chính được thiết kế bao gồm:
- **Biểu đồ cột:** Số lần ngập theo quận/huyện, so sánh theo năm.
- **Biểu đồ đường:** Xu hướng ngập theo thời gian (năm, tháng).
- **Biểu đồ tròn:** Phân bổ nguyên nhân ngập (mưa, triều cường, cống tắc).
- **Bản đồ (Map):** Vị trí và mật độ điểm ngập theo địa lý.
- **Bảng ma trận:** Số lần ngập theo Quận × Năm.

#### 4.2.2 Xây dựng các trang báo cáo chuyên sâu

Dashboard được tổ chức thành các trang chuyên sâu:
- **Trang Tổng quan:** KPI chính – tổng sự kiện ngập, khu vực ngập nhiều nhất, nguyên nhân phổ biến nhất.
- **Trang Phân tích theo Khu vực:** So sánh tình hình ngập giữa các quận/huyện.
- **Trang Phân tích theo Thời gian:** Xu hướng ngập theo năm, mùa, tháng.
- **Trang Dân số & Hạ tầng:** Tương quan giữa mật độ dân số, đường giao thông và tần suất ngập.

---

### 4.3 Đánh giá và hỗ trợ ra quyết định chiến lược

#### 4.3.1 Phân tích các kết quả đạt được qua hệ thống trực quan

Qua hệ thống trực quan hóa, một số nhận định quan trọng được rút ra:
- Các quận trung tâm (Quận 1, 3, 7) có tần suất ngập cao hơn trung bình.
- Nguyên nhân triều cường chiếm tỷ lệ lớn trong các sự kiện ngập vào các tháng cuối năm.
- Mật độ dân số cao có tương quan với mức độ thiệt hại khi xảy ra ngập.

#### 4.3.2 Minh họa các tình huống khai thác thông tin hỗ trợ ra quyết định

- **Tình huống 1 – Ưu tiên đầu tư hệ thống thoát nước:** Xác định top 5 quận có số lần ngập cao nhất để ưu tiên cải thiện hệ thống thoát nước.
- **Tình huống 2 – Lập kế hoạch ứng phó triều cường:** Phân tích lịch sử ngập theo tháng để dự đoán và chuẩn bị cho mùa triều cường.
- **Tình huống 3 – Bố trí lực lượng ứng phó:** Dựa trên bản đồ mật độ điểm ngập để phân bổ nguồn lực cứu hộ hợp lý.

---

### 4.4 Hướng phát triển trong tương lai

#### 4.4.1 Mở rộng nguồn dữ liệu lớn

- Tích hợp dữ liệu từ cảm biến IoT lắp đặt tại các điểm ngập để thu thập dữ liệu thời gian thực.
- Kết nối với dữ liệu khí tượng thủy văn (lượng mưa, mực nước triều) để mở rộng chiều phân tích.
- Tích hợp dữ liệu vệ tinh và ảnh viễn thám để phát hiện điểm ngập tự động.

#### 4.4.2 Tích hợp các mô hình học máy vào hệ thống dự báo

- Xây dựng mô hình dự báo ngập dựa trên lịch sử quan sát và dữ liệu khí tượng.
- Tích hợp mô hình Machine Learning (Random Forest, LSTM) vào pipeline ETL để tự động phân loại và dự báo.
- Triển khai Azure Machine Learning hoặc Python ML pipeline kết hợp với Power BI để hiển thị kết quả dự báo trực tiếp trên dashboard.

---

## TÀI LIỆU THAM KHẢO

1. Inmon, W. H. (2005). *Building the Data Warehouse* (4th ed.). Wiley.
2. Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3rd ed.). Wiley.
3. Microsoft Corporation. (2024). *SQL Server Integration Services (SSIS) Documentation*. Microsoft Learn.
4. Microsoft Corporation. (2024). *SQL Server Analysis Services (SSAS) Documentation*. Microsoft Learn.
5. Microsoft Corporation. (2024). *Power BI Documentation*. Microsoft Learn.
6. Moss, L. T., & Atre, S. (2003). *Business Intelligence Roadmap: The Complete Project Lifecycle for Decision-Support Applications*. Addison-Wesley.
7. Sở Xây dựng TP. Hồ Chí Minh. (2023). *Báo cáo tình hình ngập lụt đô thị năm 2023*. TP.HCM.
8. Trung tâm Quản lý hạ tầng kỹ thuật TP.HCM. (2023). *Dữ liệu quan sát điểm ngập*. TP.HCM.
