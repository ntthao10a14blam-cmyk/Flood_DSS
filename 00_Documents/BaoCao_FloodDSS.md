TRƯỜNG ĐẠI HỌC GIAO THÔNG VẬN TẢI TP. HỒ CHÍ MINH  
VIỆN CÔNG NGHỆ THÔNG TIN VÀ ĐIỆN, ĐIỆN TỬ  

---

# ĐỒ ÁN MÔN HỌC
## KHO DỮ LIỆU VÀ HỆ THỐNG HỖ TRỢ RA QUYẾT ĐỊNH

### ĐỀ TÀI:
# XÂY DỰNG KHO DỮ LIỆU TÍCH HỢP VÀ HỆ THỐNG HỖ TRỢ RA QUYẾT ĐỊNH ỨNG PHÓ NGẬP ĐÔ THỊ TẠI TP. HỒ CHÍ MINH (FLOOD-DSS)

**Giảng viên hướng dẫn:** ThS. Lê Huỳnh Long  
**Nhóm sinh viên thực hiện:** Nhóm TV (TV1 – TV6)  
**Chuyên ngành:** Khoa học Dữ liệu / Công nghệ Thông tin  

*Tp. Hồ Chí Minh, năm 2026*

---

## LỜI MỞ ĐẦU

Trong bối cảnh đô thị hóa nhanh chóng và tác động ngày càng rõ nét của biến đổi khí hậu toàn cầu, tình trạng ngập lụt đô thị tại Thành phố Hồ Chí Minh đã và đang trở thành một trong những thách thức nghiêm trọng nhất đối với công tác quy hoạch, quản lý hạ tầng và phát triển kinh tế - xã hội. Những đợt ngập sâu xuất hiện thường xuyên do sự kết hợp của các hiện tượng thời tiết cực đoan như mưa lớn vũ lượng cao, đỉnh triều cường sông Sài Gòn - Đồng Nai dâng cao, cùng sự hạn chế về năng lực tiêu thoát nước của hệ thống cống rãnh hiện hữu đã gây ảnh hưởng nặng nề đến đời sống nhân dân và làm gián đoạn huyết mạch giao thông đô thị.

Để giải quyết bài toán trên, các cơ quan ban ngành đã tiến hành thu thập nhiều nguồn dữ liệu đa dạng: từ các phản ánh hiện trường trên báo chí, các dữ liệu không gian GIS về mạng lưới thủy văn, sông ngòi, các thống kê dân số - mật độ dân cư theo địa giới hành chính, cho đến hiện trạng hạ tầng giao thông đường bộ. Tuy nhiên, các nguồn dữ liệu này phần lớn tồn tại phân tán, không đồng nhất về cấu trúc, sai lệch về định dạng và thiếu sự liên kết logic. Việc chỉ quản lý và khai thác dữ liệu trên các bảng biểu rời rạc hoặc hệ thống tác nghiệp đơn lẻ khiến các nhà quản lý gặp rất nhiều khó khăn trong việc tổng hợp đa chiều, theo dõi diễn biến lịch sử và đánh giá mức độ rủi ro phục vụ công tác ứng phó kịp thời.

Từ đòi hỏi thực tiễn đó, việc nghiên cứu và triển khai đề tài **"Xây dựng kho dữ liệu tích hợp và hệ thống hỗ trợ ra quyết định ứng phó ngập đô thị tại TP. Hồ Chí Minh (Flood-DSS)"** là hết sức cần thiết. Đồ án tập trung xây dựng quy trình toàn diện từ dữ liệu thô ban đầu đến kho dữ liệu chuẩn hóa, bao gồm: khảo sát và tiền xử lý dữ liệu đa nguồn bằng Python/QGIS; thiết lập vùng đệm Staging và thực thi quy trình ETL tự động bằng SQL Server Integration Services (SSIS); thiết kế mô hình dữ liệu đa chiều Star Schema theo phương pháp luận Kimball; xây dựng khối phân tích đa chiều OLAP bằng SQL Server Analysis Services (SSAS); và trực quan hóa các kịch bản điều hành, tính toán chỉ số ưu tiên rủi ro trên Microsoft Power BI.

Hệ thống được kỳ vọng sẽ trở thành công cụ hỗ trợ ra quyết định (Data-driven DSS) đắc lực, chuyển hóa những dòng dữ liệu quan sát ngập rời rạc thành tri thức hành động giá trị, giúp các nhà quản trị đô thị chủ động phân loại khu vực trọng điểm, dự báo rủi ro và bố trí nguồn lực ứng phó hiệu quả.

---

## LỜI CẢM ƠN

Lời đầu tiên, nhóm sinh viên chúng em xin bày tỏ lòng biết ơn chân thành và sâu sắc nhất đến **ThS. Lê Huỳnh Long** – Giảng viên phụ trách học phần *Kho dữ liệu và Hệ thống hỗ trợ ra quyết định*, Viện Công nghệ thông tin và Điện, Điện tử – Trường Đại học Giao thông Vận tải TP. Hồ Chí Minh. Thầy đã truyền đạt cho chúng em hệ thống kiến thức nền tảng vững chắc và cập nhật về kiến trúc Data Warehouse, phương pháp luận Kimball, kỹ thuật thiết kế mô hình đa chiều, quy trình tích hợp ETL cũng như các giải pháp phân tích Business Intelligence và hệ thống DSS hiện đại.

Trong suốt quá trình thực hiện đồ án, Thầy đã luôn dành thời gian tận tình theo dõi, định hướng phương pháp tiếp cận đúng đắn, đưa ra những lời khuyên chuyên môn sâu sắc và giải đáp cặn kẽ những vướng mắc kỹ thuật phức tạp từ khâu xử lý dữ liệu không gian, thiết kế khóa thay thế, cho đến tối ưu hóa khối OLAP và xây dựng mô hình tính điểm ưu tiên. Những đóng góp quý báu của Thầy là kim chỉ nam giúp nhóm từng bước hoàn thiện đồ án đạt chất lượng học thuật và ứng dụng thực tiễn cao.

Nhóm cũng xin chân thành cảm ơn các Thầy/Cô trong Viện Công nghệ thông tin và Điện, Điện tử đã tạo điều kiện học tập, nghiên cứu và trang bị cho chúng em môi trường thực hành thuận lợi. 

Mặc dù nhóm đã nỗ lực hết mình với tinh thần nghiêm túc và trách nhiệm cao nhất, nhưng do phạm vi đề tài rộng và kinh nghiệm thực tế còn hạn chế, đồ án chắc chắn khó tránh khỏi những thiếu sót nhất định. Nhóm rất mong tiếp tục nhận được những ý kiến đóng góp quý báu từ quý Thầy/Cô để hệ thống ngày càng hoàn thiện hơn.

*Kính chúc Thầy và quý Thầy/Cô luôn dồi dào sức khỏe, hạnh phúc và gặt hái được nhiều thành công rực rỡ trong sự nghiệp giáo dục!*

---

## TÓM TẮT ĐỒ ÁN

Đồ án **"Xây dựng kho dữ liệu tích hợp và hệ thống hỗ trợ ra quyết định ứng phó ngập đô thị tại TP. Hồ Chí Minh" (Flood-DSS)** được triển khai nhằm mục tiêu giải quyết bài toán tích hợp dữ liệu đa nguồn dị thể và hỗ trợ phân tích, ra quyết định chiến lược trong phòng chống ngập lụt đô thị. Dữ liệu đầu vào của đề tài bao gồm 5 tập dữ liệu chính: dữ liệu quan sát ngập lụt nguyên thủy (`Flood_Staging_Final.csv` - 425 sự kiện), dữ liệu ngập tích hợp quan hệ không gian GIS với nguồn nước, mạng lưới đường bộ và dân số (`Flood_Water_Population_Roads.csv` - 425 dòng), dữ liệu dân số và mật độ dân cư 24 quận/huyện (`Population_Clean.csv`), dữ liệu 9 trục giao thông huyết mạch (`Roads_Clean.csv`) và dữ liệu ranh giới địa giới hành chính (`Area_Boundaries_Clean.csv`).

Hệ thống được phát triển theo quy trình kỹ thuật chặt chẽ gồm các giai đoạn:
1. **Khảo sát và tiền xử lý dữ liệu:** Ứng dụng Python (Pandas) và QGIS để làm sạch dữ liệu thô, phát hiện 6 nhóm lỗi chất lượng điển hình (`Missing_Date`, `Missing_Depth`, `Duplicate_Obs_id`, `Invalid_Coordinates`, `Invalid_Depth_Range`, `Year_Date_Mismatch`), chuẩn hóa tọa độ không gian WGS84 (`DECIMAL(15,12)`), xử lý lỗi lệch kiểu định danh khu vực float string `"765.0"` về chuẩn nguyên `"765"` và tính toán khoảng cách Euclidean/mạng lưới đến sông kênh, đường giao thông.
2. **Triển khai cơ sở dữ liệu và quy trình ETL:** Thiết lập cơ sở dữ liệu `Flood_DSS` trên SQL Server gồm 2 vùng lưu trữ chuyên biệt: vùng đệm trung gian (`stg`) và vùng kho dữ liệu (`dw`). Toàn bộ luồng dữ liệu được tự động hóa thông qua 8 gói SSIS (`01_Load_Flood.dtsx` đến `08_Master_ETL.dtsx`). Cơ chế bẫy lỗi và kiểm soát chất lượng dữ liệu được thiết lập chặt chẽ thông qua các nhánh Conditional Split, chuỗi Lookup khóa thay thế (Surrogate Key) và kỹ thuật gán Unknown Member (`-1`) đối với các bản ghi khuyết thông tin. Toàn bộ 425 bản ghi quan sát ngập và 24 bản ghi dân số được nạp chính xác 100% vào kho dữ liệu mà không làm phát sinh bản ghi mồ côi (Orphan Foreign Keys).
3. **Mô hình hóa dữ liệu đa chiều (Star Schema):** Kho dữ liệu được thiết kế theo phương pháp luận Bottom-up của Ralph Kimball, bao gồm 2 bảng sự kiện trung tâm: `dw.Fact_FloodObservation` (Grain: một quan sát ngập từ một nguồn dữ liệu) và `dw.Fact_Population` (Grain: một khu vực hành chính theo năm và nguồn); liên kết chặt chẽ với 5 bảng chiều chuẩn hóa: `dw.Dim_Time`, `dw.Dim_Area`, `dw.Dim_Location`, `dw.Dim_Cause` và `dw.Dim_Source`.
4. **Xây dựng khối dữ liệu đa chiều (OLAP Cube) bằng SSAS:** Triển khai khối dữ liệu `Flood_DSS_Cube` theo phương thức lưu trữ MOLAP (Multidimensional OLAP). Hệ thống thiết lập cây phân cấp (Hierarchies) đa tầng cho chiều Thời gian, Địa giới, Vị trí và Nguồn dữ liệu, cho phép thực thi các thao tác phân tích nâng cao như Roll-up, Drill-down, Slice, Dice, Pivot, Drill-through và Drill-across bằng ngôn ngữ truy vấn MDX với thời gian phản hồi dưới 50ms, đáp ứng toàn diện tiêu chuẩn FASMI.
5. **Trực quan hóa và Hỗ trợ ra quyết định (DSS):** Kết nối kho dữ liệu trực tiếp với Microsoft Power BI để xây dựng hệ thống báo cáo chuyên sâu và 3 dashboard tương tác: *Dashboard Tổng quan tình hình ngập lụt*, *Dashboard Phân tích nguyên nhân và các yếu tố liên quan*, và *Dashboard Đánh giá rủi ro và Mức độ ưu tiên xử lý*. Đặc biệt, đề tài đã xây dựng thuật toán tính toán Chỉ số Rủi ro ngập tổng hợp (Composite Flood Risk Index - CFRI) kết hợp phân tích 9 kịch bản What-if giả định, giúp phân loại 24 quận/huyện thành 4 cấp độ ưu tiên xử lý (Khẩn cấp, Cao, Trung bình, Thấp) để chính quyền đô thị chủ động phân bổ ngân sách và điều động phương tiện ứng phó.

---

# MỤC LỤC

- [LỜI MỞ ĐẦU](#lời-mở-đầu)
- [LỜI CẢM ƠN](#lời-cảm-ơn)
- [TÓM TẮT ĐỒ ÁN](#tóm-tắt-đồ-án)
- [DANH MỤC CÁC TỪ VIẾT TẮT](#danh-mục-các-từ-viết-tắt)
- [DANH MỤC HÌNH ẢNH](#danh-mục-hình-ảnh)
- [DANH MỤC BẢNG BIỂU](#danh-mục-bảng-biểu)
- [CHƯƠNG 1: TỔNG QUAN VỀ KHO DỮ LIỆU VÀ HỆ THỐNG HỖ TRỢ RA QUYẾT ĐỊNH](#chương-1-tổng-quan-về-kho-dữ-liệu-và-hệ-thống-hỗ-trợ-ra-quyết-định)
  - [1.1. Tổng quan về đề tài](#11-tổng-quan-về-đề-tài)
  - [1.2. Cơ sở lý thuyết về Data Warehouse, BI và DSS](#12-cơ-sở-lý-thuyết-về-data-warehouse-bi-và-dss)
  - [1.3. Các phương pháp xây dựng kho dữ liệu](#13-các-phương-pháp-xây-dựng-kho-dữ-liệu)
  - [1.4. Các công nghệ sử dụng trong hệ thống](#14-các-công-nghệ-sử-dụng-trong-hệ-thống)
  - [1.5. Kết luận chương 1](#15-kết-luận-chương-1)
- [CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ KHO DỮ LIỆU](#chương-2-phân-tích-và-thiết-kế-kho-dữ-liệu)
  - [2.1. Phân tích bài toán ngập lụt tại Thành phố Hồ Chí Minh](#21-phân-tích-bài-toán-ngập-lụt-tại-thành-phố-hồ-chí-minh)
  - [2.2. Khảo sát và đánh giá chất lượng dữ liệu nguồn](#22-khảo-sát-và-đánh-giá-chất-lượng-dữ-liệu-nguồn)
    - [2.2.1. Giới thiệu các nguồn dữ liệu thu thập và quy trình khảo sát](#221-giới-thiệu-các-nguồn-dữ-liệu-thu-thập-và-quy-trình-khảo-sát)
    - [2.2.2. Đặc điểm, cấu trúc và phạm vi dữ liệu](#222-đặc-điểm-cấu-trúc-và-phạm-vi-dữ-liệu)
    - [2.2.3. Kiểm tra dữ liệu thiếu và giá trị NULL](#223-kiểm-tra-dữ-liệu-thiếu-và-giá-trị-null)
    - [2.2.4. Kiểm tra dữ liệu trùng lặp](#224-kiểm-tra-dữ-liệu-trùng-lặp)
    - [2.2.5. Kiểm tra dữ liệu bất thường và sai lệch tọa độ](#225-kiểm-tra-dữ-liệu-bất-thường-và-sai-lệch-tọa-độ)
    - [2.2.6. Xác định các quy tắc kiểm tra chất lượng dữ liệu](#226-xác-định-các-quy-tắc-kiểm-tra-chất-lượng-dữ-liệu)
    - [2.2.7. Xây dựng bộ kiểm thử chất lượng dữ liệu tự động bằng Python](#227-xây-dựng-bộ-kiểm-thử-chất-lượng-dữ-liệu-tự-động-bằng-python)
  - [2.3. Quy trình tiền xử lý và tích hợp dữ liệu](#23-quy-trình-tiền-xử-lý-và-tích-hợp-dữ-liệu)
  - [2.4. Phân tích và thiết kế mô hình kho dữ liệu](#24-phân-tích-và-thiết-kế-mô-hình-kho-dữ-liệu)
  - [2.5. Thiết kế dữ liệu phục vụ hệ thống hỗ trợ ra quyết định](#25-thiết-kế-dữ-liệu-phục-vụ-hệ-thống-hỗ-trợ-ra-quyết-định)
  - [2.6. Kết luận chương 2](#26-kết-luận-chương-2)
- [CHƯƠNG 3: TRIỂN KHAI KHO DỮ LIỆU VÀ QUY TRÌNH ETL](#chương-3-triển-khai-kho-dữ-liệu-và-quy-trình-etl)
  - [3.1. Kiến trúc và môi trường triển khai hệ thống](#31-kiến-trúc-và-môi-trường-triển-khai-hệ-thống)
  - [3.2. Khởi tạo cơ sở dữ liệu trên SQL Server](#32-khởi-tạo-cơ-sở-dữ-liệu-trên-sql-server)
  - [3.3. Xây dựng và thực thi quy trình ETL bằng SSIS](#33-xây-dựng-và-thực-thi-quy-trình-etl-bằng-ssis)
  - [3.4. Kiểm thử và đối soát dữ liệu sau ETL](#34-kiểm-thử-và-đối-soát-dữ-liệu-sau-etl)
  - [3.5. Kết luận chương 3](#35-kết-luận-chương-3)
- [CHƯƠNG 4: PHÂN TÍCH OLAP, TRỰC QUAN HÓA VÀ HỖ TRỢ RA QUYẾT ĐỊNH](#chương-4-phân-tích-olap-trực-quan-hóa-và-hỗ-trợ-ra-quyết-định)
  - [4.1. Xây dựng mô hình phân tích đa chiều bằng SSAS](#41-xây-dựng-mô-hình-phân-tích-đa-chiều-bằng-ssas)
  - [4.2. Kết nối kho dữ liệu với Power BI](#42-kết-nối-kho-dữ-liệu-với-power-bi)
  - [4.3. Xây dựng các báo cáo trực quan hóa dữ liệu](#43-xây-dựng-các-báo-cáo-trực-quan-hóa-dữ-liệu)
  - [4.4. Xây dựng Dashboard phân tích dữ liệu](#44-xây-dựng-dashboard-phân-tích-dữ-liệu)
  - [4.5. Xây dựng chức năng hỗ trợ ra quyết định](#45-xây-dựng-chức-năng-hỗ-trợ-ra-quyết-định)
  - [4.6. Kết luận chương 4](#46-kết-luận-chương-4)
- [CHƯƠNG 5: ĐÁNH GIÁ KẾT QUẢ VÀ KẾT LUẬN](#chương-5-đánh-giá-kết-quả-và-kết-luận)
  - [5.1. Tổng hợp kết quả thực hiện đồ án](#51-tổng-hợp-kết-quả-thực-hiện-đồ-án)
  - [5.2. Đánh giá hệ thống](#52-đánh-giá-hệ-thống)
  - [5.3. Những hạn chế của đề tài](#53-những-hạn-chế-của-đề-tài)
  - [5.4. Hướng phát triển trong tương lai](#54-hướng-phát-triển-trong-tương-lai)
  - [5.5. Kết luận chung](#55-kết-luận-chung)
- [TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)
- [PHỤ LỤC](#phụ-lục)

---

## DANH MỤC CÁC TỪ VIẾT TẮT

| Từ viết tắt | Thuật ngữ tiếng Anh đầy đủ | Diễn giải tiếng Việt |
| :--- | :--- | :--- |
| **BI** | Business Intelligence | Trí tuệ kinh doanh / Kinh doanh thông minh |
| **CFRI** | Composite Flood Risk Index | Chỉ số rủi ro ngập lụt tổng hợp |
| **CSV** | Comma-Separated Values | Định dạng tệp dữ liệu phân tách bằng dấu phẩy |
| **DAX** | Data Analysis Expressions | Ngôn ngữ biểu thức phân tích dữ liệu |
| **DSV** | Data Source View | Khung nhìn nguồn dữ liệu trong SSAS |
| **DW / DWH** | Data Warehouse | Kho dữ liệu |
| **DSS** | Decision Support System | Hệ thống hỗ trợ ra quyết định |
| **ETL** | Extract, Transform, Load | Trích xuất, Biến đổi và Nạp dữ liệu |
| **FASMI** | Fast, Analysis, Shared, Multidimensional, Information | Tiêu chuẩn chất lượng của hệ thống OLAP |
| **FK** | Foreign Key | Khóa ngoại |
| **GIS** | Geographic Information System | Hệ thống thông tin địa lý |
| **HOLAP** | Hybrid OLAP | OLAP kết hợp lai giữa mảng đa chiều và quan hệ |
| **MDX** | Multidimensional Expressions | Ngôn ngữ truy vấn khối đa chiều |
| **MOLAP** | Multidimensional OLAP | OLAP lưu trữ trực tiếp trên khối đa chiều |
| **OLAP** | Online Analytical Processing | Xử lý phân tích trực tuyến |
| **OLTP** | Online Transaction Processing | Xử lý giao dịch trực tuyến |
| **PK** | Primary Key | Khóa chính |
| **QGIS** | Quantum Geographic Information System | Phần mềm hệ thống thông tin địa lý mã nguồn mở |
| **ROLAP** | Relational OLAP | OLAP dựa trên hệ quản trị cơ sở dữ liệu quan hệ |
| **SCD** | Slowly Changing Dimension | Chiều thay đổi chậm |
| **SSAS** | SQL Server Analysis Services | Dịch vụ phân tích khối đa chiều của SQL Server |
| **SSDT** | SQL Server Data Tools | Bộ công cụ phát triển BI trên Visual Studio |
| **SSIS** | SQL Server Integration Services | Dịch vụ tích hợp và xử lý luồng ETL của SQL Server |
| **SSMS** | SQL Server Management Studio | Môi trường quản trị hệ thống cơ sở dữ liệu SQL Server |
| **stg** | Staging Schema | Vùng lược đồ cơ sở dữ liệu đệm trung gian |
| **dw** | Data Warehouse Schema | Vùng lược đồ lưu trữ dữ liệu phân tích kho |
| **UAC** | User Account Control | Cơ chế kiểm soát tài khoản người dùng của Windows |
| **UNK** | Unknown | Thành viên không xác định (Unknown Member) |

---

## DANH MỤC HÌNH ẢNH

| Ký hiệu | Tên hình ảnh |
| :--- | :--- |
| **Hình 1.1** | Kiến trúc tổng thể hệ thống Kho dữ liệu và Hỗ trợ ra quyết định Flood-DSS |
| **Hình 2.1** | Phân bố không gian các điểm ngập lụt trên nền bản đồ GIS TP.HCM |
| **Hình 2.2** | Kết quả khảo sát và đánh giá 6 cờ chất lượng dữ liệu nguồn bằng Python |
| **Hình 2.3** | Quy trình tiền xử lý, tính toán khoảng cách không gian và phân tách luồng dữ liệu |
| **Hình 2.4** | Sơ đồ Lược đồ hình sao (Star Schema) của Kho dữ liệu Flood-DSS |
| **Hình 3.1** | Cấu trúc phân tầng lưu chuyển dữ liệu từ Nguồn đến Kho dữ liệu và Báo cáo |
| **Hình 3.2** | Cấu trúc các bảng thuộc schema `stg` và `dw` hiển thị trên Object Explorer SSMS |
| **Hình 3.3** | Sơ đồ Control Flow tổng thể điều phối quy trình ETL trong gói `08_Master_ETL.dtsx` |
| **Hình 3.4** | Thiết kế Data Flow Task nạp dữ liệu vào Staging (`01_Load_Flood.dtsx`) |
| **Hình 3.5** | Thiết kế Data Flow nạp Dimension có xử lý làm sạch và tạo khóa thay thế (`06_Load_Dimensions.dtsx`) |
| **Hình 3.6** | Thiết kế Data Flow nạp Fact với chuỗi Lookup khóa thay thế (`07_Load_Facts.dtsx`) |
| **Hình 4.1** | Cấu trúc khối đa chiều `Flood_DSS_Cube` và quan hệ Dimension Usage trong SSAS |
| **Hình 4.2** | Sơ đồ ngữ nghĩa Semantic Model thiết lập quan hệ Star Schema trong Power BI |
| **Hình 4.3** | Biểu đồ phân tích diễn biến số vụ ngập và độ sâu ngập theo thời gian (Năm/Tháng) |
| **Hình 4.4** | Biểu đồ cơ cấu nguyên nhân ngập lụt đô thị và thời lượng ngập trung bình |
| **Hình 4.5** | Bản đồ nhiệt (Heatmap) thể hiện mật độ không gian và phân cấp độ sâu các điểm ngập |
| **Hình 4.6** | Dashboard 1: Tổng quan tình hình ngập lụt tại TP. Hồ Chí Minh |
| **Hình 4.7** | Dashboard 2: Phân tích nguyên nhân và các yếu tố tương quan hạ tầng |
| **Hình 4.8** | Dashboard 3: Đánh giá chỉ số rủi ro ngập và Xếp hạng ưu tiên xử lý đô thị |
| **Hình 4.9** | Giao diện mô phỏng phân tích kịch bản What-if phục vụ ra quyết định điều hành |

---

## DANH MỤC BẢNG BIỂU

| Ký hiệu | Tên bảng biểu |
| :--- | :--- |
| **Bảng 1.1** | So sánh các phương pháp luận xây dựng kho dữ liệu (Top-down, Bottom-up, Hybrid) |
| **Bảng 1.2** | Bảng đặc tả các công nghệ và công cụ triển khai trong hệ thống |
| **Bảng 2.1** | Danh mục và đặc điểm kỹ thuật 5 file dữ liệu nguồn |
| **Bảng 2.2** | Thống kê tỷ lệ giá trị thiếu (NULL) theo thuộc tính và nhận định nghiệp vụ |
| **Bảng 2.3** | Kết quả kiểm tra dữ liệu bất thường theo quy tắc nghiệp vụ |
| **Bảng 2.4** | Danh mục các quy tắc kiểm tra chất lượng dữ liệu trong hệ thống Flood-DSS |
| **Bảng 2.5** | Bảng ma trận kết quả thực thi 18 ca kiểm thử chất lượng dữ liệu tự động bằng Python |
| **Bảng 2.6** | Đặc tả các thuộc tính dẫn xuất tính toán phục vụ phân tích đa chiều |
| **Bảng 2.7** | Ma trận Bus Matrix cho bài toán Quản lý ngập lụt đô thị TP.HCM |
| **Bảng 2.8** | Thiết kế cấu trúc các bảng Dimension (`Dim_Time`, `Dim_Area`, `Dim_Location`, `Dim_Cause`, `Dim_Source`) |
| **Bảng 2.9** | Thiết kế cấu trúc bảng sự kiện `Fact_FloodObservation` |
| **Bảng 2.10** | Thiết kế cấu trúc bảng sự kiện `Fact_Population` |
| **Bảng 2.11** | Trọng số và thang đo tính toán Chỉ số Rủi ro ngập lụt tổng hợp (CFRI) |
| **Bảng 2.12** | Bảng phân cấp 4 mức độ rủi ro và thứ tự ưu tiên xử lý ngập đô thị |
| **Bảng 3.1** | Thông số môi trường phát triển và cấu hình phần mềm hệ thống |
| **Bảng 3.2** | Danh mục và chức năng 8 gói SSIS trong dự án `FloodDSS_ETL` |
| **Bảng 3.3** | Đặc tả ánh xạ các Connection Manager trong hệ thống SSIS |
| **Bảng 3.4** | Bảng ánh xạ chuyển đổi cột trong Package `01_Load_Flood.dtsx` (`stg.Flood`) |
| **Bảng 3.5** | Bảng ánh xạ chuyển đổi cột trong Package `02_Load_FloodIntegrated.dtsx` (`stg.FloodIntegrated`) |
| **Bảng 3.6** | Bảng ánh xạ chuyển đổi cột trong Package `03_Load_Population.dtsx` (`stg.Population`) |
| **Bảng 3.7** | Bảng ánh xạ chuyển đổi cột trong Package `04_Load_Roads.dtsx` (`stg.Roads`) |
| **Bảng 3.8** | Bảng ánh xạ chuyển đổi cột trong Package `05_Load_Area.dtsx` (`stg.Area`) |
| **Bảng 3.9** | Cấu trúc các bảng nhật ký `stg.ETL_Log` và `stg.ETL_Error` |
| **Bảng 3.10** | Tổng hợp đối soát số lượng bản ghi qua các giai đoạn ETL (Nguồn - Staging - DW) |
| **Bảng 3.11** | Thống kê số lượng bản ghi thực tế trong các bảng Dimension và Fact |
| **Bảng 4.1** | So sánh kỹ thuật 3 phương pháp lưu trữ OLAP (MOLAP, ROLAP, HOLAP) |
| **Bảng 4.2** | Cấu trúc các cây phân cấp (Hierarchies) thiết lập trong SSAS |
| **Bảng 4.3** | Bảng công thức các hàm tính toán Measure DAX xây dựng trên Power BI |
| **Bảng 4.4** | Bảng ma trận 9 kịch bản What-if và định hướng quyết định điều hành tương ứng |
| **Bảng 5.1** | Bảng đối chiếu mức độ đáp ứng các mục tiêu nghiên cứu của đề tài |

---

# CHƯƠNG 1: TỔNG QUAN VỀ KHO DỮ LIỆU VÀ HỆ THỐNG HỖ TRỢ RA QUYẾT ĐỊNH

## 1.1. Tổng quan về đề tài

### 1.1.1. Lý do lựa chọn đề tài
Thành phố Hồ Chí Minh là trung tâm kinh tế, tài chính, giáo dục và khoa học công nghệ hàng đầu cả nước, đóng góp hơn 20% GDP quốc gia. Tuy nhiên, cùng với tốc độ phát triển đô thị nhanh chóng, thành phố đang phải đối diện với tình trạng ngập lụt diễn biến hết sức phức tạp và có xu hướng gia tăng cả về phạm vi, tần suất lẫn mức độ nghiêm trọng. Nguyên nhân ngập lụt bắt nguồn từ sự kết hợp của nhiều yếu tố tự nhiên và nhân sinh: địa hình thấp trũng (với hơn 60% diện tích có cao độ dưới +1.5m), triều cường sông Sài Gòn thường xuyên vượt mức báo động III (+1.60m), các trận mưa lớn cực đoan có vũ lượng vượt quá 100mm/3h, hiện tượng sụt lún nền đất đô thị, và hệ thống thoát nước cũ kỹ, quá tải so với quy mô dân số thực tế hơn 10 triệu người.

Mỗi đợt ngập úng gây thiệt hại kinh tế ước tính hàng nghìn tỷ đồng mỗi năm, làm tê liệt các trục lộ giao thông huyết mạch, hư hại cơ sở hạ tầng, phương tiện di chuyển và đe dọa trực tiếp đến đời sống, vệ sinh môi trường của người dân. Trong công tác chỉ đạo và điều hành, các cơ quan quản lý đô thị (như Sở Xây dựng, Trung tâm Quản lý Hạ tầng Kỹ thuật, Ban Chỉ huy Phòng chống thiên tai) thu thập được rất nhiều nguồn dữ liệu. Tuy nhiên, các nguồn dữ liệu này đang tồn tại ở dạng phân tán (báo chí, báo cáo kỹ thuật, bản đồ GIS, bảng biểu thống kê dân số Excel/CSV). Tình trạng thiếu một nền tảng tích hợp dữ liệu tập trung khiến việc theo dõi lịch sử, nhận diện các điểm đen ngập úng và lập kế hoạch ưu tiên đầu tư công trình thoát nước gặp nhiều lúng túng. 

Vì vậy, việc ứng dụng các công nghệ hiện đại về **Kho dữ liệu (Data Warehouse)**, **Xử lý phân tích trực tuyến (OLAP)**, **Kinh doanh thông minh (Business Intelligence)** và **Hệ thống hỗ trợ ra quyết định (Decision Support System - DSS)** để xây dựng giải pháp **Flood-DSS** là nhiệm vụ có ý nghĩa thực tiễn cấp bách và giá trị khoa học to lớn.

### 1.1.2. Mục tiêu nghiên cứu
Đề tài hướng tới việc thực hiện các mục tiêu cụ thể sau:
1. **Mục tiêu khoa học:** Nghiên cứu và làm chủ cơ sở lý thuyết về mô hình hóa dữ liệu đa chiều theo phương pháp luận Kimball, kiến trúc kho dữ liệu doanh nghiệp phân tầng, kỹ thuật xử lý dữ liệu lớn trong quy trình ETL và cơ chế phân tích khối đa chiều OLAP.
2. **Mục tiêu kỹ thuật:**
   - Xây dựng quy trình tự động hóa ETL bằng công cụ SSIS để tích hợp, làm sạch và chuẩn hóa 5 nguồn dữ liệu không gian và phi không gian về ngập lụt tại TP.HCM.
   - Thiết kế và cài đặt cơ sở dữ liệu kho dữ liệu `Flood_DSS` trên SQL Server theo chuẩn Star Schema, bảo đảm tính toàn vẹn thực thể, tham chiếu và bẫy lỗi tự động.
   - Triển khai khối dữ liệu đa chiều MOLAP bằng SSAS với các cây phân cấp thời gian, địa giới, nguồn dữ liệu và các độ đo định lượng phục vụ truy vấn MDX tức thì.
   - Xây dựng mô hình ngữ nghĩa (Semantic Model) và các Dashboard tương tác thông minh trên Microsoft Power BI.
3. **Mục tiêu thực tiễn:** Xây dựng mô hình tính điểm Chỉ số Rủi ro ngập lụt tổng hợp (CFRI) và thiết kế chức năng phân tích kịch bản What-if, cung cấp công cụ trực quan hỗ trợ chính quyền và các nhà quản lý đô thị ra quyết định phân loại mức độ ưu tiên xử lý ngập lụt chính xác.

### 1.1.3. Đối tượng và phạm vi nghiên cứu
- **Đối tượng nghiên cứu:** 
  - Các quy trình nghiệp vụ ghi nhận, quan sát và quản lý sự kiện ngập úng đô thị.
  - Các tập dữ liệu quan sát ngập lụt, ranh giới hành chính quận/huyện, số liệu dân số - mật độ dân cư và mạng lưới đường giao thông chính tại TP. Hồ Chí Minh.
  - Các mô hình kiến trúc kho dữ liệu, quy trình ETL, khối OLAP và hệ thống hỗ trợ ra quyết định.
- **Phạm vi nghiên cứu:**
  - *Không gian:* Địa bàn 24 quận, huyện và Thành phố Thủ Đức thuộc TP. Hồ Chí Minh.
  - *Thời gian dữ liệu:* Chuỗi dữ liệu quan sát lịch sử tập trung trong giai đoạn 2015 – 2023.
  - *Quy mô dữ liệu:* 425 sự kiện quan sát ngập lụt đô thị chi tiết, 24 đơn vị hành chính quận/huyện, 9 tuyến đường trục chính và hệ thống sông kênh rạch liên quan.

### 1.1.4. Phương pháp nghiên cứu
Đề tài áp dụng kết hợp các phương pháp nghiên cứu sau:
- **Phương pháp thu thập và phân tích tài liệu:** Nghiên cứu các giáo trình, tài liệu chuyên khảo quốc tế về Data Warehouse (Ralph Kimball, Bill Inmon), tài liệu kỹ thuật của Microsoft về SSIS, SSAS, Power BI và các báo cáo hiện trạng thoát nước đô thị TP.HCM.
- **Phương pháp phân tích và mô hình hóa:** Sử dụng phương pháp luận thiết kế kho dữ liệu Bottom-up của Kimball, lập ma trận Bus Matrix, xác định Grain và thiết kế lược đồ hình sao (Star Schema).
- **Phương pháp thực nghiệm kỹ thuật:** Sử dụng ngôn ngữ Python (thư viện Pandas) và phần mềm QGIS để khảo sát chất lượng và tính toán khoảng cách không gian; sử dụng Microsoft SQL Server để xây dựng CSDL; xây dựng các gói SSIS thực thi ETL; cấu hình khối SSAS và phát triển dashboard trên Power BI Desktop.
- **Phương pháp chuyên gia và đánh giá định lượng:** Tham khảo các tiêu chuẩn kỹ thuật về thoát nước để xây dựng trọng số cho mô hình đánh giá rủi ro ngập tổng hợp (CFRI) và kiểm thử các kịch bản What-if.

---

## 1.2. Cơ sở lý thuyết về Data Warehouse, BI và DSS

### 1.2.1. Khái niệm Data Warehouse
Theo William H. Inmon (2005) – người được xem là cha đẻ của kho dữ liệu: *"Kho dữ liệu là một tập hợp dữ liệu hướng chủ đề, tích hợp, gắn nhãn thời gian và bất biến, nhằm hỗ trợ quá trình ra quyết định của các nhà quản lý"*. Khác với cơ sở dữ liệu tác nghiệp (OLTP) vốn được tối ưu hóa cho các thao tác thêm, sửa, xóa các giao dịch đơn lẻ hằng ngày với cấu trúc chuẩn hóa cao (3NF), Kho dữ liệu (Data Warehouse - DW) được thiết kế chuyên biệt để phục vụ công tác truy vấn tổng hợp, phân tích xu hướng và khai phá dữ liệu với cấu trúc bán chuẩn hóa (Dimensional Modeling).

### 1.2.2. Đặc trưng của kho dữ liệu
Kho dữ liệu mang 4 đặc trưng cốt lõi (SIVN):
1. **Hướng chủ đề (Subject-Oriented):** Dữ liệu được tổ chức xoay quanh các đối tượng phân tích nghiệp vụ trọng tâm (ví dụ: Quan sát ngập lụt, Biến động dân số) thay vì xoay quanh các chức năng ứng dụng tác nghiệp.
2. **Tính tích hợp (Integrated):** Đây là đặc trưng quan trọng nhất. Dữ liệu từ nhiều nguồn khác nhau (báo chí, cảm biến, file thống kê CSV) với các quy ước mã hóa, định dạng ngày tháng và kiểu dữ liệu không nhất quán sẽ được làm sạch, chuyển đổi và đồng nhất về một cấu trúc chung duy nhất.
3. **Gắn nhãn thời gian (Time-Variant):** Mọi bản ghi trong kho dữ liệu đều gắn liền với một mốc thời gian cụ thể (thể hiện qua khóa `TimeKey`). Kho dữ liệu lưu trữ lịch sử dài hạn (từ 5 đến 10 năm hoặc nhiều hơn), cho phép so sánh xu hướng biến động qua các thời kỳ.
4. **Tính bất biến (Non-Volatile):** Dữ liệu sau khi đã trải qua quy trình kiểm soát và nạp vào kho sẽ được lưu trữ vĩnh viễn cho mục đích đọc (Read-Only). Người dùng không thực hiện các thao tác cập nhật hay xóa bản ghi đơn lẻ, đảm bảo tính ổn định và nhất quán tuyệt đối cho các phân tích lịch sử.

### 1.2.3. Khái niệm Business Intelligence
Business Intelligence (BI) là thuật ngữ bao gồm các công nghệ, quy trình và công cụ hỗ trợ người dùng chuyển hóa dữ liệu thô thành thông tin hữu ích và tri thức chiến lược phục vụ hoạt động sản xuất kinh doanh (Chen et al., 2012). Hệ thống BI cung cấp các báo cáo quản trị, bảng điều khiển tương tác (Dashboards), phân tích trực quan và khai phá dữ liệu, giúp tổ chức chuyển từ mô hình "ra quyết định theo cảm tính" sang "ra quyết định dựa trên dữ liệu" (Data-driven Decision Making).

### 1.2.4. Khái niệm Decision Support System
Hệ thống hỗ trợ ra quyết định (Decision Support System - DSS) là hệ thống thông tin tương tác trên nền tảng máy tính, giúp người ra quyết định sử dụng dữ liệu và các mô hình toán học/nghiệp vụ để giải quyết các vấn đề bán cấu trúc hoặc phi cấu trúc (Turban et al., 2011). 
Trong đề tài này, hệ thống thuộc dạng **Data-driven DSS** (DSS hướng dữ liệu), nơi kho dữ liệu đóng vai trò trái tim cung cấp thông tin sạch, khối OLAP cho phép phân tích góc nhìn linh hoạt và mô hình tính điểm rủi ro đưa ra các khuyến nghị, xếp hạng ưu tiên xử lý công trình thoát nước.

### 1.2.5. Vai trò của kho dữ liệu trong hệ thống hỗ trợ ra quyết định
Kho dữ liệu đóng vai trò nền tảng quyết định sự thành bại của hệ thống DSS:
- Cung cấp "chân lý dữ liệu duy nhất" (Single Source of Truth), loại bỏ tình trạng số liệu mâu thuẫn giữa các phòng ban.
- Tách biệt hoàn toàn tải công việc phân tích (vốn tiêu tốn rất nhiều tài nguyên I/O và CPU) ra khỏi hệ thống tác nghiệp hằng ngày.
- Cung cấp dữ liệu lịch sử tích hợp đa chiều, làm tiền đề tin cậy để huấn luyện các thuật toán mô phỏng kịch bản và dự báo rủi ro.

---

## 1.3. Các phương pháp xây dựng kho dữ liệu

*Bảng 1.1: So sánh các phương pháp luận xây dựng kho dữ liệu*

| Tiêu chí | Phương pháp luận Top-down (Bill Inmon) | Phương pháp luận Bottom-up (Ralph Kimball) | Phương pháp luận kết hợp (Hybrid) |
| :--- | :--- | :--- | :--- |
| **Triết lý cốt lõi** | Xây dựng Kho dữ liệu doanh nghiệp (EDW) tập trung ở dạng chuẩn 3NF trước, sau đó trích xuất ra các Data Mart. | Xây dựng các Data Mart theo mô hình đa chiều (Star Schema) cho từng nghiệp vụ trước, sau đó tích hợp qua Bus Architecture. | Thiết kế khung kiến trúc tổng thể, sau đó phát triển cuốn chiếu từng Data Mart đa chiều. |
| **Cấu trúc lưu trữ** | Mô hình quan hệ thực thể chuẩn hóa (ER 3NF). | Mô hình đa chiều (Dimensional Modeling: Star / Snowflake Schema). | Kết hợp: Tầng Core lưu 3NF hoặc Data Vault, tầng Datamart lưu Star Schema. |
| **Thời gian triển khai** | Dài (thường từ 1 – 3 năm để thấy kết quả ban đầu). | Ngắn (vài tháng cho từng quy trình nghiệp vụ cụ thể). | Trung bình (cân bằng giữa thiết kế và triển khai). |
| **Chi phí ban đầu** | Rất cao, đòi hỏi đội ngũ chuyên gia phân tích toàn diện. | Vừa phải, dễ thích ứng với ngân sách từng giai đoạn. | Cao. |
| **Độ linh hoạt** | Thấp, thay đổi yêu cầu dẫn đến chỉnh sửa phức tạp. | Rất cao, dễ dàng bổ sung thêm Dimension và Fact mới. | Khá cao. |
| **Khả năng ứng dụng** | Phù hợp với các tập đoàn tài chính, ngân hàng đa quốc gia. | **Rất phù hợp với bài toán quản trị đô thị, dự án học thuật và doanh nghiệp linh hoạt.** | Phù hợp với các tổ chức quy mô lớn muốn hiện đại hóa dần. |

### 1.3.4. Lựa chọn phương pháp Kimball cho đề tài
Đề tài quyết định lựa chọn **Phương pháp luận Bottom-up của Ralph Kimball** vì những lý do thực tiễn sau:
1. Bài toán ứng phó ngập đô thị có các quy trình nghiệp vụ rõ ràng: Quan sát diễn biến ngập và Thống kê quy mô dân cư bị ảnh hưởng.
2. Mô hình hình sao (Star Schema) của Kimball tối ưu hóa tốc độ truy vấn phân tích, rất trực quan và dễ dàng kết nối với các công cụ BI hiện đại như SSAS và Power BI.
3. Kiến trúc Bus Matrix với các **Conformed Dimensions** (`Dim_Area`, `Dim_Source`, `Dim_Time`) đảm bảo tính nhất quán tuyệt đối khi tích hợp chéo giữa các bảng Fact khác nhau, cho phép mở rộng thêm các chủ đề mới (như Lượng mưa, Thiệt hại kinh tế) trong tương lai mà không phá vỡ kiến trúc cũ.

---

## 1.4. Các công nghệ sử dụng trong hệ thống

*Bảng 1.2: Bảng đặc tả các công nghệ và công cụ triển khai trong hệ thống*

| STT | Công cụ / Công nghệ | Phiên bản | Vai trò trong hệ thống Flood-DSS |
| :---: | :--- | :--- | :--- |
| 1 | **Microsoft Windows 11 Pro** | 64-bit | Môi trường hệ điều hành thực thi và phát triển toàn bộ hệ thống. |
| 2 | **Microsoft SQL Server** | 2025 Developer | Hệ quản trị CSDL trung tâm, lưu trữ vùng Staging (`stg`) và Kho dữ liệu (`dw`). |
| 3 | **SQL Server Management Studio (SSMS)** | v20.2 | Giao diện quản trị CSDL, thực thi script T-SQL, tạo index và phân quyền. |
| 4 | **SQL Server Integration Services (SSIS)** | Projects 2022 | Công cụ thiết kế và thực thi quy trình ETL tự động hóa từ CSV vào kho dữ liệu. |
| 5 | **SQL Server Analysis Services (SSAS)** | Multidimensional | Nền tảng xây dựng khối dữ liệu đa chiều MOLAP, xử lý truy vấn MDX tức thì. |
| 6 | **Microsoft Visual Studio Community** | 2022 (v17.x) | Môi trường phát triển tích hợp (IDE) xây dựng các dự án SSIS và SSAS. |
| 7 | **Microsoft Power BI Desktop** | 2024 / 2025 | Xây dựng Semantic Model, viết hàm DAX và thiết kế các Dashboard tương tác. |
| 8 | **Python & Thư viện Pandas** | 3.12 | Khảo sát dữ liệu thô ban đầu, làm sạch, tách lỗi và chuẩn hóa cấu trúc tệp. |
| 9 | **QGIS (Quantum GIS)** | 3.3x LTR | Xử lý không gian, chuẩn hóa hệ tọa độ WGS84 và tính toán khoảng cách GIS. |

---

## 1.5. Kết luận chương 1
Chương 1 đã trình bày một cách hệ thống bối cảnh thực tiễn, tính cấp bách của đề tài nghiên cứu cùng các mục tiêu khoa học, kỹ thuật và ứng dụng rõ ràng. Đề tài đã phân tích sâu sắc cơ sở lý luận về Kho dữ liệu, Kinh doanh thông minh và Hệ thống hỗ trợ ra quyết định; tiến hành so sánh toàn diện các phương pháp luận xây dựng kho dữ liệu và khẳng định việc lựa chọn phương pháp luận Kimball là hoàn toàn khoa học và tối ưu đối với bài toán ngập lụt TP.HCM. Cuối cùng, hệ sinh thái công nghệ Microsoft kết hợp Python và QGIS đã được thiết lập chặt chẽ, tạo nền móng vững chắc cho các giai đoạn phân tích, thiết kế và triển khai ở các chương tiếp theo.

---

# CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ KHO DỮ LIỆU

## 2.1. Phân tích bài toán ngập lụt tại Thành phố Hồ Chí Minh

### 2.1.1. Thực trạng và các yếu tố ảnh hưởng đến ngập lụt
TP. Hồ Chí Minh có diện tích tự nhiên khoảng 2.095 km², địa hình nghiêng nhẹ từ Bắc xuống Nam và từ Tây sang Đông, mạng lưới sông ngòi kênh rạch chằng chịt dài hàng nghìn kilômét chịu ảnh hưởng trực tiếp của chế độ bán nhật triều không đều của biển Đông. Tình trạng ngập lụt trên địa bàn thành phố được định hình bởi 3 nhóm nguyên nhân chính:
1. **Ngập do mưa (Mưa cực đoan):** Biến đổi khí hậu làm gia tăng tần suất các trận mưa cường độ rất lớn trong thời gian ngắn, vượt xa tiêu chuẩn thiết kế của hệ thống thoát nước hiện hữu.
2. **Ngập do triều cường:** Mực nước triều dâng cao theo sông Sài Gòn tràn ngược vào hệ thống cống và tràn qua đê bao vào các khu dân cư trũng thấp dọc theo Quận 7, Quận 8, huyện Nhà Bè, huyện Bình Chánh.
3. **Ngập do tổ hợp mưa kết hợp triều cường:** Khi mưa lớn xuất hiện đúng vào thời điểm đỉnh triều dâng cao, nước mưa không thể tiêu thoát tự nhiên ra sông khiến mức độ ngập trở nên nghiêm trọng nhất, thời gian ngập kéo dài nhiều giờ liên tục.

### 2.1.2. Nhu cầu phân tích dữ liệu ngập lụt
Để chuyển đổi công tác ứng phó từ "bị động đối phó" sang "chủ động thích ứng", các nhà quản lý đô thị có nhu cầu phân tích dữ liệu chuyên sâu:
- Phân tích chuỗi thời gian ngập: Mùa ngập tập trung vào những tháng nào? Các năm gần đây có xu hướng tăng hay giảm?
- Phân tích không gian địa lý: Khu vực nào, tuyến đường nào là "điểm nóng" có tần suất và độ sâu ngập cao nhất?
- Phân tích tương quan dân sinh và hạ tầng: Mật độ dân cư vùng ngập ra sao? Tuyến đường ngập có nằm gần sông kênh không? Khoảng cách tới mạng lưới giao thông chính là bao xa?

### 2.1.3. Các câu hỏi phân tích và yêu cầu hỗ trợ ra quyết định
Hệ thống Flood-DSS được thiết kế nhằm trả lời các câu hỏi chỉ đạo tác nghiệp cụ thể:
1. *Top 5 quận/huyện nào có tổng số lần ngập và độ sâu ngập trung bình cao nhất thành phố?*
2. *Nguyên nhân ngập chủ đạo tại khu vực nội thành (Quận 1, 3, 5) khác biệt như thế nào so với khu vực trũng ven sông (Quận 7, Nhà Bè)?*
3. *Mức độ rủi ro ngập lụt tại các quận mật độ dân số cực cao (Quận 10, Quận 11, Quận 4) ảnh hưởng thế nào đến trật tự an toàn đô thị?*
4. *Nếu xuất hiện trận mưa vũ lượng tăng thêm 20% kết hợp triều cường +1.70m, thành phố cần ưu tiên phân bổ trạm bơm di động và lực lượng ứng trực tại những vị trí nào trước tiên?*

---

## 2.2. Khảo sát và đánh giá chất lượng dữ liệu nguồn

### 2.2.1. Giới thiệu các nguồn dữ liệu thu thập và quy trình khảo sát
Trước khi tiến hành xây dựng vùng đệm Staging và thiết kế quy trình ETL, nhóm tiến hành khảo sát toàn diện các tập dữ liệu nguồn bằng thư viện **Pandas** trong Python kết hợp các công cụ GIS nhằm xác định quy mô, cấu trúc, mức độ hoàn thiện và các vấn đề tiềm ẩn ảnh hưởng đến chất lượng dữ liệu. Dữ liệu đầu vào của đề tài bao gồm 5 tập dữ liệu chính được lưu dưới dạng tệp CSV phân tách bằng dấu phẩy:

*Bảng 2.1: Danh mục và đặc điểm kỹ thuật 5 file dữ liệu nguồn*

| STT | Tên tập tin CSV nguồn | Số dòng | Số cột | Dung lượng | Nội dung nghiệp vụ chính |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Flood_Staging_Final.csv` | 425 | 33 | ~142 KB | Dữ liệu sự kiện quan sát ngập lụt chi tiết thu thập từ báo chí và khảo sát (ngày, vị trí, độ sâu, thời lượng, nguyên nhân, cờ kiểm định). |
| 2 | `Flood_Water_Population_Roads.csv` | 425 | 46 | ~198 KB | Dữ liệu ngập tích hợp không gian GIS: liên kết sự kiện ngập với khoảng cách tới sông kênh, ranh giới dân cư và khoảng cách tới tim đường bộ. |
| 3 | `Population_Clean.csv` | 24 | 9 | ~3.2 KB | Thống kê quy mô dân số, diện tích tự nhiên và mật độ dân cư năm 2019 của 24 đơn vị hành chính quận/huyện tại TP.HCM. |
| 4 | `Roads_Clean.csv` | 9 | 4 | ~1.1 KB | Danh mục 9 trục giao thông huyết mạch thường xuyên xuất hiện ngập lụt đô thị. |
| 5 | `Area_Boundaries_Clean.csv` | 24 | 9 | ~3.5 KB | Danh mục địa giới hành chính theo Quyết định 124/2004/QĐ-TTg của Thủ tướng Chính phủ. |

Nhóm đã xây dựng kịch bản Python tự động hóa (`01_Audit_Existing_Data.py` và `01_Check_Flood_Data.py`) để khảo sát tự động toàn bộ các tệp dữ liệu trên:

```python
import pandas as pd
from pathlib import Path

ROOT = Path(r"D:\Kho_du_lieu\Flood-DSS")
FILES = {
    "Flood_Staging": ROOT / "02_Staging_CSV/Flood/Flood_Staging_Final.csv",
    "Flood_Integrated": ROOT / "02_Staging_CSV/Integrated/Flood_Water_Population_Roads.csv",
    "Population": ROOT / "02_Staging_CSV/Population/Population_Clean.csv",
    "Roads": ROOT / "02_Staging_CSV/Roads/Roads_Clean.csv",
    "Area": ROOT / "02_Staging_CSV/Area/Area_Boundaries_Clean.csv"
}

print("===== KẾT QUẢ KHẢO SÁT CHẤT LƯỢNG DỮ LIỆU NGUỒN (DATA PROFILING) =====")
for name, path in FILES.items():
    if path.exists():
        df = pd.read_csv(path, encoding="utf-8-sig", low_memory=False)
        print(f"\n[DATASET: {name}]")
        print(f"- Tổng số bản ghi (Rows)  : {len(df):,}")
        print(f"- Tổng số thuộc tính (Cols): {len(df.columns)}")
        print(f"- Số ô khuyết thiếu (NULL): {df.isna().sum().sum():,} ({df.isna().mean().mean()*100:.2f}%)")
        print(f"- Dòng trùng lặp hoàn toàn: {df.duplicated().sum()}")
```

Kết quả thực thi kịch bản Data Profiling trên console ghi nhận bức tranh tổng quan như sau:

```text
======================================================================
1. KẾT QUẢ DATA PROFILING TỔNG HỢP CÁC NGUỒN DỮ LIỆU
======================================================================
* Flood_Staging_Final.csv        : 425 dòng | 33 cột | 2.284 ô thiếu | 0 dòng trùng 100%
* Flood_Water_Population_Roads.csv: 425 dòng | 46 cột | 3.612 ô thiếu | 0 dòng trùng 100%
* Population_Clean.csv           :  24 dòng |  9 cột |     0 ô thiếu | 0 dòng trùng 100%
* Roads_Clean.csv                :   9 dòng |  4 cột |     0 ô thiếu | 0 dòng trùng 100%
* Area_Boundaries_Clean.csv      :  24 dòng |  9 cột |    48 ô thiếu | 0 dòng trùng 100%

* Kiểm tra cờ chất lượng sự kiện ngập (Flood Quality Flags):
  - Missing_Date (Khuyết ngày quan sát)    : 63 dòng (14.82%)
  - Missing_Depth (Thiếu số liệu độ sâu)   : 257 dòng (60.47%)
  - Duplicate_Obs_id (Trùng lặp mã sự kiện): 2 dòng (0.47%)
  - Year_Date_Mismatch (Lệch ngày và năm) : 1 dòng (0.24%)
  - Invalid_Coordinates (Sai lệch tọa độ)  : 0 dòng (sau chuẩn hóa GIS)
  - Invalid_Depth_Range (Độ sâu âm)        : 0 dòng
======================================================================
```

---

### 2.2.2. Đặc điểm, cấu trúc và phạm vi dữ liệu
Bộ dữ liệu của đề tài bao phủ không gian toàn bộ 24 quận, huyện và Thành phố Thủ Đức của TP.HCM trong chuỗi thời gian lịch sử từ năm 2015 đến 2023. Các thuộc tính trong dữ liệu được phân chia thành 5 nhóm ngữ nghĩa nghiệp vụ:

1. **Nhóm thông tin sự kiện ngập:** `Obs_id`, `Date`, `Year`, `Location_name`, `Location_type`, `District_mentioned`, `Ward`, `Current_admin_unit`.
2. **Nhóm đo lường độ sâu và thời lượng ngập:** `Water_height_max_cm`, `Water_height_min_cm`, `AvgDepth_cm`, `Duration_hours`, `Depth_class`.
3. **Nhóm nguyên nhân và nguồn tin:** `Cause`, `Impact_type`, `Source_id`, `Source_type`, `Observation_notes`.
4. **Nhóm không gian địa lý GIS:** `Longitude`, `Latitude`, `Spatial_precision`, `Geocoding_method`, `DistanceToWater_m`, `Nearest_Road_ID`, `DistanceToNearestRoad_m`.
5. **Nhóm thuộc tính dân cư và ranh giới:** `Population_Area_ID`, `Population_Area_Name`, `Population_2019`, `PopulationDensity_2019`, `Area_km2`.

---

### 2.2.3. Kiểm tra dữ liệu thiếu và giá trị NULL
Dữ liệu quan sát ngập lụt thu thập từ phản ánh hiện trường và báo chí mang đặc trưng phi cấu trúc, dẫn đến hiện tượng khuyết thiếu giá trị ở một số thuộc tính định lượng và phân loại. Kết quả thống kê chi tiết tỷ lệ giá trị thiếu (NULL) trên 425 dòng của tập dữ liệu ngập được thể hiện tại Bảng 2.2:

*Bảng 2.2: Thống kê tỷ lệ giá trị thiếu (NULL) theo thuộc tính và nhận định nghiệp vụ*

| Tên thuộc tính | Kiểu dữ liệu | Số dòng thiếu (NULL) | Tỷ lệ khuyết (%) | Nhận định nghiệp vụ và Chiến lược xử lý |
| :--- | :--- | :---: | :---: | :--- |
| `Province` | Chuỗi | 418 | 98.35% | Hầu hết các bài báo ngầm định phạm vi tại TP.HCM nên không ghi tỉnh; chiến lược: gán mặc định `"TP. Hồ Chí Minh"`. |
| `Duration_hours` | Số thực | 398 | 93.65% | Phóng viên và người dân chủ yếu phản ánh thời điểm ngập cao nhất, rất ít ghi nhận thời điểm nước rút hoàn toàn; chiến lược: giữ nguyên NULL trong Fact và sử dụng giá trị trung bình theo nguyên nhân trong phân tích giả định. |
| `Commune` | Chuỗi | 397 | 93.41% | Đô thị TP.HCM chủ yếu sử dụng cấp quản lý Phường (Ward), chỉ khu vực ngoại thành mới có Xã (Commune); giá trị thiếu là bình thường theo ngữ nghĩa. |
| `Observation_Notes` | Văn bản | 359 | 84.47% | Phần ghi chú mô tả thêm chỉ xuất hiện ở các sự kiện ngập nghiêm trọng; chiến lược: cho phép NULL. |
| `MinDepth_cm` | Số thực | 314 | 73.88% | Người dân thường chỉ quan sát được mức nước ngập cao nhất (`MaxDepth`); chiến lược: gán bằng giá trị `MaxDepth_cm` nếu thiếu. |
| `MaxDepth_cm` | Số thực | 278 | 65.41% | Nhiều bài báo chỉ phản ánh định tính "ngập sâu", "ngập nửa bánh xe"; cờ `Missing_Depth = 1` được kích hoạt để phân loại khi tính toán KPI. |
| `Date` | Ngày tháng | 63 | 14.82% | 63 sự kiện chỉ ghi nhận được năm quan sát hoặc mùa mưa mà không có ngày chính xác; chiến lược: gán khóa thời gian Unknown Member (`TimeKey = -1`) trong kho dữ liệu. |
| `Ward` | Chuỗi | 47 | 11.06% | Bản tin chỉ nhắc đến tên tuyến đường hoặc quận; chiến lược: gán nhãn `"Không xác định"`. |
| `District_Mentioned` | Chuỗi | 7 | 1.65% | Tuyến đường nằm giáp ranh giữa 2 quận; xử lý bằng thuật toán Spatial Join trên QGIS để xác định quận tương ứng. |
| `Current_Admin_Unit` | Chuỗi | 5 | 1.18% | Lỗi cập nhật đơn vị hành chính mới; đối soát theo danh mục Quyết định 124/2004/QĐ-TTg. |
| `EffectiveFrom` / `To` | Ngày tháng | 24 | 100.00% | Tệp ranh giới 2019 không có mốc ngày hiệu lực; thiết kế cho phép NULL trong bảng `stg.Area` và `dw.Dim_Area`. |

Đáng chú ý, các giá trị NULL ở các thuộc tính đo lường không mang ý nghĩa "lỗi hệ thống" mà phản ánh đúng thực tế của dữ liệu quan trắc xã hội học. Vì vậy, chiến lược của nhóm là **tuyệt đối không xóa bỏ các dòng này** để bảo toàn nguyên vẹn 425 sự kiện lịch sử, đồng thời xử lý triệt để bằng kỹ thuật gán giá trị mặc định và thành viên dự phòng Unknown Member (`-1`) trong quy trình ETL.

---

### 2.2.4. Kiểm tra dữ liệu trùng lặp
Nhóm thực hiện kiểm tra trùng lặp trên hai cấp độ:
1. **Trùng lặp hoàn toàn trên toàn bộ các cột (`df.duplicated()`):** Kết quả ghi nhận **0 dòng** trùng lặp hoàn toàn trên cả 5 tệp dữ liệu nguồn, khẳng định mỗi dòng trong tệp đều chứa các thông tin thuộc tính phân biệt.
2. **Trùng lặp mã sự kiện nghiệp vụ (`Obs_id`):** 
   - Kiểm tra cột định danh `Obs_id` phát hiện **2 dòng** bị trùng mã sự kiện (`Duplicate_Obs_id = 1` tại sự kiện `Obs_239`).
   - *Nguyên nhân:* Cùng một trận ngập tại nút giao thông trọng điểm được trích xuất từ hai cơ quan báo chí khác nhau vào cùng một ngày.
   - *Chiến lược xử lý:* Trong gói SSIS nạp Dimension/Fact, áp dụng câu lệnh lọc phân hạng `ROW_NUMBER() OVER(PARTITION BY Obs_id ORDER BY Water_height_max_cm DESC) AS rn` kết hợp mệnh đề `WHERE rn = 1` để giữ lại bản ghi có thông tin đo lường chi tiết nhất, loại bỏ nguy cơ vi phạm ràng buộc `UNIQUE` trên kho dữ liệu.

---

### 2.2.5. Kiểm tra dữ liệu bất thường và sai lệch tọa độ
Tiến hành rà soát các bất thường mang tính nghiệp vụ và không gian GIS:

*Bảng 2.3: Kết quả kiểm tra dữ liệu bất thường theo quy tắc nghiệp vụ*

| Loại bất thường kiểm tra | Điều kiện logic kiểm tra | Số dòng phát hiện | Diễn giải và Chiến lược xử lý kỹ thuật |
| :--- | :--- | :---: | :--- |
| **Độ sâu ngập âm** | `Water_height_max_cm < 0` hoặc `MinDepth < 0` | 0 | Không phát hiện số đo độ sâu âm; dữ liệu đạt yêu cầu logic vật lý. |
| **Thời lượng ngập âm** | `Duration_hours < 0` | 0 | Không phát hiện thời lượng ngập âm; thời lượng dao động hợp lý từ 0.3 đến 6.0 giờ. |
| **Sai lệch Năm và Ngày** | `Year != Date.Year` | 1 | Bản ghi `Obs_298` (Đường Nguyễn Văn Hưởng, Thảo Điền) có `Date = '2018-10-08'` nhưng cột `Year = 2019`. Xử lý: chuẩn hóa cột `Year = 2018` theo ngày quan sát thực tế; 361/362 bản ghi có ngày còn lại khớp 100%. |
| **Lệch kiểu định danh khu vực** | `Population_Area_ID` chứa ký tự thập phân `.` | 417 | Toàn bộ 417 dòng nội thành trong tệp tích hợp bị lưu dạng float string (ví dụ: `"765.0"` thay vì `"765"`). Xử lý: áp dụng biểu thức ép kiểu `TRY_CAST(TRY_CAST(Area_ID AS FLOAT) AS INT)` trước khi tra cứu Dimension. |
| **Tọa độ ngoài ranh giới TP.HCM** | Tọa độ nằm ngoài Bounding Box hoặc ngoài địa giới TP.HCM | 8 | 417/425 điểm ngập nằm trọn vẹn trong ranh giới địa lý TP.HCM (hệ tọa độ WGS84, `DECIMAL(15,12)`). Phát hiện chính xác 8 điểm nằm ngoài ranh giới polygon 2019 (gồm 2 điểm tại Vũng Tàu `Obs_12`, `Obs_13` với kinh độ ~107.12°E, 5 điểm Bình Dương và 1 điểm giáp ranh sát mép Quận 8 `Obs_184`). Xử lý: định tuyến sang Unknown Member (`AreaKey = -1`). |
| **Khoảng cách tới sông kênh** | `DistanceToWater_m < 0` hoặc `> 20.000m` | 0 | Khoảng cách ngắn nhất là 0.00m, khoảng cách trung bình là 364.35m, khoảng cách lớn nhất là 16.789m (khu vực huyện Cần Giờ/Củ Chi). Dữ liệu hoàn toàn hợp lệ. |

---

### 2.2.6. Xác định các quy tắc kiểm tra chất lượng dữ liệu (Data Quality Rules)
Từ kết quả khảo sát thực nghiệm, nhóm đúc kết thành 6 quy tắc kiểm soát chất lượng dữ liệu cốt lõi (ký hiệu từ **QR_01** đến **QR_06**) được cài đặt trực tiếp vào các cổng kiểm soát (Data Quality Gates) trong quy trình SSIS ETL:

*Bảng 2.4: Danh mục các quy tắc kiểm tra chất lượng dữ liệu trong hệ thống Flood-DSS*

| Mã quy tắc | Điều kiện logic áp dụng | Ý nghĩa nghiệp vụ | Hành động xử lý trong luồng SSIS ETL |
| :---: | :--- | :--- | :--- |
| **QR_01** | `Water_height_max_cm >= 0` | Đảm bảo tính hợp lý của độ sâu ngập | Nếu vi phạm, đưa vào luồng `INVALID` ghi nhật ký lỗi `stg.ETL_Error`. |
| **QR_02** | `Duration_hours >= 0` | Đảm bảo thời lượng ngập không âm | Giữ nguyên độ chính xác thập phân `DT_NUMERIC(10,2)`. |
| **QR_03** | `10.3 <= Latitude <= 11.2` và `106.3 <= Longitude <= 107.2` | Tọa độ điểm ngập phải nằm trong phạm vi khảo sát | Bảo toàn độ phân giải cao `DT_NUMERIC(15,12)`, gán `LocationKey = -1` nếu không xác định. |
| **QR_04** | `Population_Area_ID` dạng số nguyên | Khớp nối chính xác mã quận/huyện | Chuyển đổi chuỗi float `"765.0"` $\rightarrow$ `"765"` trước khi Lookup `Dim_Area`. |
| **QR_05** | Lookup khóa ngoại Dimension không tìm thấy | Duy trì tính toàn vẹn tham chiếu | Tự động gán khóa thay thế dự phòng **`-1` (Unknown Member)**. |
| **QR_06** | `(SourceKey, Obs_ID)` không được trùng lặp | Bảo vệ Grain duy nhất của bảng Fact | Áp dụng ràng buộc `UNIQUE` và lọc khử trùng `ROW_NUMBER()` trước khi INSERT. |

---

### 2.2.7. Xây dựng bộ kiểm thử chất lượng dữ liệu tự động bằng Python (Automated Data Quality Test Suite)

Nhằm chuyển đổi các quy tắc kiểm soát chất lượng thành quy trình kiểm thử tự động, lặp lại và có thể lượng hóa, nhóm đã xây dựng bộ kiểm thử chất lượng dữ liệu tự động bằng Python tại tệp [`03_Python/test_data_quality.py`](file:///d:/Kho_du_lieu/Flood-DSS/03_Python/test_data_quality.py). Bộ kiểm thử được phát triển dựa trên thư viện chuẩn `unittest` kết hợp `pandas` và `numpy`, bao gồm **18 ca kiểm thử (Test Cases - TC01 đến TC18)** chia thành 6 phân nhóm chuyên biệt:

1. **Suite 1: Kiểm tra tệp tin và cấu trúc lược đồ (TC01 - TC03):** Đảm bảo sự tồn tại đầy đủ của 6 tệp CSV nguồn/tích hợp, đối soát số lượng bản ghi theo Baseline (425 sự kiện ngập, 24 quận/huyện, 9 tuyến đường) và kiểm tra sự hiện diện của các thuộc tính cốt lõi.
2. **Suite 2: Kiểm tra tính duy nhất và khóa định danh (TC04 - TC06):** Rà soát trùng lặp 100% thuộc tính (đạt 0 dòng), kiểm tra phát hiện 2 dòng trùng mã sự kiện `Obs_239` và kiểm tra tính duy nhất tuyệt đối của các khóa tự nhiên Dimension (`Area_ID`, `Road_ID`).
3. **Suite 3: Kiểm tra độ đầy đủ và dữ liệu khuyết thiếu (TC07 - TC09):** Khẳng định 0 giá trị NULL trên 7 cột bắt buộc, kiểm soát ngưỡng khuyết ngày quan sát (`Date IS NULL`: 63 dòng ~ 14.82% <= ngưỡng trần 20%), và phân định rạch ròi giữa 257 dòng khuyết hoàn toàn cờ `Missing_Depth` với 21 dòng khuyết độ sâu số học nhưng có nhãn phân lớp định tính (`16 Severe + 5 Heavy`).
4. **Suite 4: Kiểm tra miền giá trị và logic nghiệp vụ (TC10 - TC13):** Thực thi các quy tắc QR_01 (độ sâu không âm), QR_02 (thời lượng không âm), kiểm tra miền giá trị danh mục nguyên nhân (`Rain`, `High tide`, `Combined`) và phát hiện chính xác sự kiện lệch Ngày-Năm (`Obs_298`).
5. **Suite 5: Kiểm tra độ chính xác không gian GIS (TC14 - TC16):** Thực thi quy tắc QR_03 trên hệ tọa độ WGS84, kiểm tra cự ly ngắn nhất tới sông kênh (`DistanceToWater_m` trung bình 364.35m, cực đại 16.789m) và cự ly tới tim đường bộ.
6. **Suite 6: Kiểm tra tích hợp và toàn vẹn tham chiếu (TC17 - TC18):** Thực thi quy tắc QR_04 (khử đuôi `.0` trên 417 chuỗi float string mã quận) và QR_05 (xác nhận 417 sự kiện khớp hoàn toàn với 24 quận/huyện, 8 sự kiện giáp ranh/ngoại tỉnh được định tuyến về Unknown Member `-1`).

Mã nguồn trích đoạn các phương thức kiểm định tiêu biểu trong `test_data_quality.py`:

```python
import unittest
import pandas as pd

class TestDataQualitySuite(unittest.TestCase):

    def test_05_obs_id_deduplication_audit(self):
        """TC05: Phát hiện chính xác 2 dòng trùng Obs_id (Obs_239) và xác nhận khử trùng thành công."""
        flood_df = self.data["Flood_Staging"]
        dup_obs = flood_df[flood_df.duplicated("Obs_id", keep=False)]
        dup_count = len(dup_obs)
        dup_ids = dup_obs["Obs_id"].unique().tolist()
        
        # Khử trùng theo MaxDepth: mỗi Obs_id là duy nhất
        dedup_df = flood_df.sort_values("Water_height_max_cm", ascending=False).drop_duplicates(subset=["Obs_id"], keep="first")
        self.assertTrue(dup_count == 2 and "Obs_239" in dup_ids and dedup_df["Obs_id"].nunique() == 424)

    def test_14_coordinates_within_bounds(self):
        """TC14 [QR_03]: Tọa độ 100% điểm ngập nằm trong bounding box khảo sát [10.3-11.2°N, 106.3-107.2°E]."""
        flood_df = self.data["Flood_Staging"]
        valid_coords = (flood_df['Latitude'].between(10.3, 11.2)) & (flood_df['Longitude'].between(106.3, 107.2))
        vungtau_points = flood_df[flood_df['Longitude'] > 107.1]['Obs_id'].tolist()
        self.assertTrue(valid_coords.all() and set(vungtau_points) == {'Obs_12', 'Obs_13'})

    def test_17_population_area_id_castable_to_int(self):
        """TC17 [QR_04]: Kiểm tra lỗi float string ('765.0') và xác nhận 100% chuyển đổi an toàn sang số nguyên."""
        integ_df = self.data["Flood_Integrated"]
        area_ids = integ_df['Population_Area_ID'].dropna().astype(str)
        cleaned_ids = area_ids.str.replace(r"\.0$", "", regex=True)
        self.assertTrue(cleaned_ids.str.isdigit().all() and len(cleaned_ids) == 417)
```

Kết quả thực thi tự động toàn bộ 18 Test Cases được tổng hợp chi tiết tại Bảng 2.5:

*Bảng 2.5: Bảng ma trận kết quả thực thi 18 ca kiểm thử chất lượng dữ liệu tự động bằng Python*

| Mã TC | Phân nhóm kiểm thử | Tên ca kiểm thử | Điều kiện logic kiểm tra | Trạng thái | Chi tiết kết quả thực tế ghi nhận |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **TC01** | Schema & Files | Kiểm tra tồn tại tệp nguồn | Tồn tại 6/6 tệp CSV trên đĩa | **PASSED** | Đầy đủ 6/6 tệp dữ liệu nguồn và tích hợp tồn tại trên đĩa. |
| **TC02** | Schema & Files | Đối soát số lượng bản ghi | Khớp số dòng thiết kế baseline | **PASSED** | Flood: 425/425; Integ: 425/425; Pop: 24/24; Roads: 9/9; Area: 24/24. |
| **TC03** | Schema & Files | Cấu trúc thuộc tính cốt lõi | Hiện diện 9 cột bắt buộc bảng ngập | **PASSED** | Đầy đủ các cột: `Obs_id`, `Date`, `Year`, `Location_name`, `MaxDepth`, v.v. |
| **TC04** | Uniqueness | Kiểm tra trùng lặp 100% | `df.duplicated().sum() == 0` | **PASSED** | 0 dòng trùng lặp hoàn toàn trên toàn bộ 6 tập dữ liệu. |
| **TC05** | Uniqueness | Khử trùng mã `Obs_id` | Phát hiện 2 dòng `Obs_239` | **PASSED** | Phát hiện đúng 2 dòng trùng `Obs_239`; khử trùng còn 424 sự kiện duy nhất (QR_06). |
| **TC06** | Uniqueness | Khóa tự nhiên Dimension | `Area_ID`, `Road_ID` duy nhất | **PASSED** | 24/24 mã quận và 9/9 mã đường đạt tính duy nhất 100%. |
| **TC07** | Completeness | Cột bắt buộc không NULL | `Col.isna().sum() == 0` trên 7 cột | **PASSED** | 0 giá trị NULL trên các trường định danh và tọa độ. |
| **TC08** | Completeness | Tỷ lệ khuyết ngày quan sát | `Date.isna().sum() == 63` (< 20%) | **PASSED** | Khuyết ngày: 63 dòng (14.82% <= ngưỡng trần 20%); gán `TimeKey = -1`. |
| **TC09** | Completeness | Tính nhất quán cờ `Missing_Depth` | 278 thiếu số cm = 257 cờ + 21 định tính | **PASSED** | 257 dòng cờ `Missing_Depth = True` (60.47%); 21 dòng có nhãn phân lớp `Severe`/`Heavy`. |
| **TC10** | Domain Logic | Độ sâu ngập không âm (QR_01) | `MaxDepth >= 0`, `MinDepth >= 0` | **PASSED** | 0 giá trị âm; độ sâu hợp lệ từ 10.0 cm đến 150.0 cm. |
| **TC11** | Domain Logic | Thời lượng không âm (QR_02) | `Duration_hours >= 0` | **PASSED** | 0 giá trị âm; thời lượng hợp lệ từ 0.3 giờ đến 6.0 giờ. |
| **TC12** | Domain Logic | Danh mục nguyên nhân ngập | `Cause IN ('Rain', 'High tide', 'Combined')` | **PASSED** | 100% nguyên nhân thuộc danh mục chuẩn hóa. |
| **TC13** | Domain Logic | Nhất quán Ngày - Năm | `Date.year == Year` (trừ Obs_298) | **PASSED** | Phát hiện đúng 1 bản ghi lệch (`Obs_298`: Date 2018 vs Year 2019); 361/362 bản ghi khớp 100%. |
| **TC14** | Geospatial | Tọa độ WGS84 TP.HCM (QR_03) | `10.3 <= Lat <= 11.2`, `106.3 <= Lon <= 107.2` | **PASSED** | 100% điểm ngập nằm trong Bounding Box; phát hiện đúng 2 điểm Vũng Tàu (`Obs_12`, `Obs_13`). |
| **TC15** | Geospatial | Khoảng cách tới sông kênh | `DistanceToWater_m >= 0` và `< 20.000m` | **PASSED** | Min: 0.00m; Trung bình: 364.35m; Max: 16.789m. Hợp lệ. |
| **TC16** | Geospatial | Khoảng cách tới đường bộ | `DistanceToNearestRoad_m >= 0` | **PASSED** | Min: 0.02m; 100% khoảng cách không âm. |
| **TC17** | Referential | Ép kiểu float string (QR_04) | `Population_Area_ID` khử `.0` $\rightarrow$ INT | **PASSED** | Phát hiện 417 chuỗi float string; 100% chuyển đổi an toàn sang số nguyên. |
| **TC18** | Referential | Toàn vẹn tham chiếu quận (QR_05) | 417 khớp 24 quận, 8 gán Unknown | **PASSED** | 417/425 sự kiện khớp danh mục quận/huyện; 8 điểm giáp ranh/ngoại tỉnh định tuyến sang `-1`. |

Nhật ký thực thi bộ kiểm thử (Test Summary Log) được tự động xuất ra tệp `07_Logs/Data_Quality_Test_Summary.txt`:

```text
====================================================================================================
  BÁO CÁO TỔNG HỢP KẾT QUẢ KIỂM THỬ CHẤT LƯỢNG DỮ LIỆU TỰ ĐỘNG BẰNG PYTHON (FLOOD-DSS)
====================================================================================================
Thời gian thực thi : 07/11/2026 05:51:13
Tổng số ca kiểm thử: 18
Số ca ĐẠT (PASSED) : 18 / 18
Số ca LỖI (FAILED) : 0 / 18
Tỷ lệ thành công   : 100.0%
----------------------------------------------------------------------------------------------------
TC01   | Schema & Files             | PASSED     | Đầy đủ 6/6 tệp dữ liệu tồn tại trên đĩa
TC02   | Schema & Files             | PASSED     | Flood: 425/425 | Integ: 425/425 | Pop: 24/24 | Roads: 9/9 | Area: 24/24
TC03   | Schema & Files             | PASSED     | Đầy đủ 9 thuộc tính cốt lõi của bảng sự kiện ngập
TC04   | Uniqueness                 | PASSED     | 0 dòng trùng lặp 100% trên cả 6 dataset
TC05   | Uniqueness                 | PASSED     | Phát hiện đúng 2 dòng trùng mã ['Obs_239']; khử trùng còn 424 sự kiện duy nhất (QR_06)
TC06   | Uniqueness                 | PASSED     | Area_ID (24/24), Road_ID (9/9), Boundary Area_ID (24/24) đều duy nhất 100%
TC07   | Completeness               | PASSED     | 0 giá trị NULL trên 7 cột bắt buộc (Obs_id, Year, Location, Cause, Source, Long, Lat)
TC08   | Completeness               | PASSED     | Khuyết ngày: 63 dòng (14.82% <= ngưỡng 20.0%); gán TimeKey = -1
TC09   | Completeness               | PASSED     | Khuyết độ sâu số học: 278 dòng (65.41%); cờ Missing_Depth: 257 dòng (60.47%); 21 định tính
TC10   | Domain & Business Logic    | PASSED     | 0 dòng độ sâu âm (MaxDepth min: 10.0 cm, MinDepth min: 10.0 cm)
TC11   | Domain & Business Logic    | PASSED     | 0 dòng thời lượng ngập âm (Thời lượng min: 0.3 giờ, max: 6.0 giờ)
TC12   | Domain & Business Logic    | PASSED     | 100% nguyên nhân hợp lệ trong danh mục chuẩn: ['High tide', 'Rain', 'Combined']
TC13   | Domain & Business Logic    | PASSED     | Phát hiện đúng 1 bản ghi lệch ngày-năm (Obs_298: Date 2018 vs Year 2019); 361/362 bản ghi khớp 100%
TC14   | Geospatial Accuracy        | PASSED     | 100% tọa độ nằm trong Bounding Box; xác định đúng 2 điểm Vũng Tàu (Obs_12, Obs_13)
TC15   | Geospatial Accuracy        | PASSED     | 0 khoảng cách âm | Min: 0.00m | Mean: 364.35m | Max: 16789.39m (Cần Giờ/Củ Chi)
TC16   | Geospatial Accuracy        | PASSED     | 0 khoảng cách âm | Min: 0.02m | Max: 49381.61m | 100% hợp lệ
TC17   | Integration & Referential  | PASSED     | Phát hiện 417 chuỗi float string; 100% (417 dòng) ép kiểu an toàn sang INT (QR_04)
TC18   | Integration & Referential  | PASSED     | 417/425 sự kiện khớp 24 quận/huyện; 8 điểm giáp ranh định tuyến sang Unknown Member (-1)
====================================================================================================
```

---

## 2.3. Quy trình tiền xử lý và tích hợp dữ liệu

### 2.3.1. Làm sạch và chuẩn hóa dữ liệu
Sử dụng Python để cắt bỏ khoảng trắng thừa (`strip()`), chuyển đổi toàn bộ chuỗi văn bản về Unicode UTF-8, đồng nhất cách viết hoa/thường cho các phân loại nguyên nhân (`Mưa lớn`, `Triều cường`, `Mưa kết hợp triều cường`).

### 2.3.2. Chuẩn hóa dữ liệu không gian và hệ tọa độ
Toàn bộ dữ liệu điểm ngập, đường giao thông và ranh giới hành chính trên QGIS được quy đổi thống nhất về hệ tọa độ chuẩn quốc tế **WGS84 (EPSG: 4326)**. Độ chính xác của kinh độ và vĩ độ được cố định ở 12 chữ số thập phân (`DECIMAL(15,12)`), đảm bảo sai số vị trí thực tế dưới 1 milimét.

### 2.3.3. Tích hợp dữ liệu ngập lụt, lượng mưa, dân số và giao thông
Quy trình tích hợp không gian sử dụng các thuật toán Spatial Join:
- Tính khoảng cách ngắn nhất từ mỗi điểm ngập đến mạng lưới sông ngòi, kênh rạch chính (`DistanceToWater_m`).
- Xác định điểm ngập nằm trọn trong ranh giới quận/huyện nào để gán thông tin dân số và mật độ dân cư năm 2019 (`Population_Area_ID`, `Population_2019`, `PopulationDensity_2019`).
- Xác định tuyến đường trục gần nhất trong bán kính quét để gán mã đường và khoảng cách (`Nearest_Road_ID`, `DistanceToNearestRoad_m`).

### 2.3.4. Xử lý dữ liệu thiếu, dữ liệu không hợp lệ
Các bản ghi thiếu độ sâu hoặc thời lượng ngập được gán giá trị trung vị của khu vực tương ứng trong các phân tích giả định, nhưng giữ nguyên giá trị NULL trong bảng Fact vật lý để phản ánh đúng thực tế thu thập.

### 2.3.5. Xây dựng các thuộc tính phục vụ phân tích

*Bảng 2.6: Đặc tả các thuộc tính dẫn xuất tính toán phục vụ phân tích đa chiều*

| Tên thuộc tính dẫn xuất | Công thức / Quy tắc tính toán | Mục đích phân tích |
| :--- | :--- | :--- |
| `AvgDepth_cm` | `(Water_height_max_cm + Water_height_min_cm) / 2` | Độ sâu ngập bình quân của sự kiện |
| `Road_Distance_Band` | `< 50m`, `50 - 200m`, `200 - 500m`, `> 500m` | Phân đoạn mức độ ảnh hưởng đến giao thông |
| `Season` | Tháng 5 – 11: "Mùa mưa", Tháng 12 – 4: "Mùa khô" | Phân tích tính quy luật mùa vụ ngập lụt |
| `ObservationCount` | Mặc định = `1` cho mỗi sự kiện | Độ đo đếm cộng dồn tổng số lượt ngập |

---

## 2.4. Phân tích và thiết kế mô hình kho dữ liệu

### 2.4.1. Xác định quy trình nghiệp vụ và mức chi tiết dữ liệu (Grain)
Hệ thống xác định 2 quy trình nghiệp vụ cốt lõi:
1. **Quan sát sự kiện ngập lụt (Flood Observation):** Theo dõi từng sự kiện ngập lụt được ghi nhận tại một địa điểm, thời gian, nguyên nhân và nguồn cụ thể.
   - **Grain:** *Mỗi dòng trong bảng sự kiện đại diện cho một quan sát ngập lụt đơn lẻ từ một nguồn dữ liệu xác định `(SourceKey, Obs_ID)`.*
2. **Thống kê dân số và mật độ dân cư (Population Statistics):** Theo dõi số dân và diện tích của từng đơn vị hành chính qua các năm.
   - **Grain:** *Mỗi dòng đại diện cho quy mô dân số của một quận/huyện trong một năm xác định `(AreaKey, Year, SourceKey)`.*

### 2.4.2. Xây dựng Bus Matrix

*Bảng 2.7: Ma trận Bus Matrix cho bài toán Quản lý ngập lụt đô thị TP.HCM*

| Quy trình nghiệp vụ / Bảng Fact | Dim_Time | Dim_Area | Dim_Location | Dim_Cause | Dim_Source |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1. Quan sát ngập lụt (`Fact_FloodObservation`)** | **X** | **X** | **X** | **X** | **X** |
| **2. Thống kê dân cư (`Fact_Population`)** | — | **X** | — | — | **X** |

Hai chiều `Dim_Area` và `Dim_Source` đóng vai trò là **Conformed Dimensions**, cho phép thực hiện phân tích chéo khối (Drill-across) giữa quy mô ngập lụt và mức độ tập trung dân số.

### 2.4.3. Thiết kế các bảng Dimension

*Bảng 2.8: Thiết kế cấu trúc các bảng Dimension trong kho dữ liệu Flood-DSS*

```
dw.Dim_Time:
  - TimeKey (INT, PK) - Khóa thời gian YYYYMMDD
  - FullDate (DATE, Unique) - Ngày đầy đủ
  - Day, Month, Quarter, Year (Số nguyên)
  - MonthName (NVARCHAR(20))
  - Season (NVARCHAR(30)) - Mùa mưa / Mùa khô
  - DayOfWeek (TINYINT)

dw.Dim_Area:
  - AreaKey (INT IDENTITY, PK) - Khóa thay thế
  - Area_ID (NVARCHAR(50)) - Mã nguồn quận/huyện
  - Area_Name (NVARCHAR(150)) - Tên quận/huyện
  - Area_Level (NVARCHAR(30)) - Cấp: Quận / Huyện / TP Thủ Đức
  - ParentArea_ID (NVARCHAR(50)) - Khu vực cha (TP.HCM)
  - Area_km2 (DECIMAL(18,4)) - Diện tích tự nhiên

dw.Dim_Location:
  - LocationKey (INT IDENTITY, PK) - Khóa thay thế
  - Location_ID (NVARCHAR(50)) - Mã vị trí
  - Location_Name (NVARCHAR(500)) - Tên tuyến đường/nút giao ngập
  - Location_Type (NVARCHAR(100)) - Tuyến đường / Giao lộ / Điểm
  - AreaKey (INT, FK) - Liên kết với Dim_Area
  - Longitude, Latitude (DECIMAL(15,12)) - Tọa độ không gian chuẩn

dw.Dim_Cause:
  - CauseKey (INT IDENTITY, PK) - Khóa thay thế
  - Cause_Name (NVARCHAR(150), Unique) - Tên nguyên nhân ngập
  - Description (NVARCHAR(500)) - Mô tả chi tiết nguyên nhân

dw.Dim_Source:
  - SourceKey (INT IDENTITY, PK) - Khóa thay thế
  - Source_ID (NVARCHAR(100), Unique) - Mã nguồn tin (SRC_1, POP_01)
  - Source_Name (NVARCHAR(255)) - Tên cơ quan / Báo chí
  - Source_Type (NVARCHAR(100)) - Báo chí / Cơ quan / Cảm biến
```

### 2.4.4. Thiết kế các bảng Fact

*Bảng 2.9: Thiết kế cấu trúc bảng sự kiện Fact_FloodObservation*

| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa nghiệp vụ |
| :--- | :--- | :--- | :--- |
| `FloodObservationKey` | BIGINT IDENTITY(1,1) | PRIMARY KEY | Khóa chính tự tăng |
| `Obs_ID` | NVARCHAR(200) | NOT NULL | Mã quan sát từ nguồn dữ liệu |
| `TimeKey` | INT | NOT NULL, FK | Liên kết `dw.Dim_Time` |
| `AreaKey` | INT | NOT NULL, FK | Liên kết `dw.Dim_Area` |
| `LocationKey` | INT | NOT NULL, FK | Liên kết `dw.Dim_Location` |
| `CauseKey` | INT | NOT NULL, FK | Liên kết `dw.Dim_Cause` |
| `SourceKey` | INT | NOT NULL, FK | Liên kết `dw.Dim_Source` |
| `MinDepth_cm` | DECIMAL(10,2) | NULL | Độ sâu ngập nhỏ nhất (cm) |
| `MaxDepth_cm` | DECIMAL(10,2) | NULL | Độ sâu ngập lớn nhất (cm) |
| `AvgDepth_cm` | DECIMAL(10,2) | NULL | Độ sâu ngập trung bình (cm) |
| `Duration_hours` | DECIMAL(10,2) | NULL | Thời lượng ngập (giờ) |
| `ObservationCount` | TINYINT | DEFAULT (1) | Độ đo cộng dồn số lượt ngập |
| `DataQualityStatus` | NVARCHAR(100) | NOT NULL | Trạng thái chất lượng (Valid / Flagged) |

*Bảng 2.10: Thiết kế cấu trúc bảng sự kiện Fact_Population*

| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa nghiệp vụ |
| :--- | :--- | :--- | :--- |
| `PopulationKey` | BIGINT IDENTITY(1,1) | PRIMARY KEY | Khóa chính tự tăng |
| `AreaKey` | INT | NOT NULL, FK | Liên kết `dw.Dim_Area` |
| `Year` | SMALLINT | NOT NULL | Năm thống kê |
| `SourceKey` | INT | NOT NULL, FK | Liên kết `dw.Dim_Source` |
| `Population` | BIGINT | CHECK >= 0 | Tổng dân số của khu vực |
| `Area_km2` | DECIMAL(18,4) | CHECK > 0 | Diện tích đất tự nhiên |
| `PopulationDensity` | DECIMAL(18,3) | CHECK >= 0 | Mật độ dân số (người/km²) |
| `DataQualityStatus` | NVARCHAR(100) | NOT NULL | Trạng thái chất lượng |

### 2.4.5. Xác định khóa chính, khóa ngoại và mối quan hệ
- **Tính duy nhất theo Grain:**
  - `Fact_FloodObservation` được bảo vệ bằng ràng buộc duy nhất: `UNIQUE (SourceKey, Obs_ID)`.
  - `Fact_Population` được bảo vệ bằng ràng buộc: `UNIQUE (AreaKey, Year, SourceKey)`.
- **Toàn vẹn tham chiếu:** Toàn bộ 7 khóa ngoại từ 2 bảng Fact tham chiếu đến 5 bảng Dimension đều được kích hoạt với trạng thái `ENABLED` và `TRUSTED`, hoàn toàn ngăn chặn các bản ghi mồ côi.

### 2.4.6. Xây dựng mô hình Star Schema
Mô hình Star Schema hoàn chỉnh được tổ chức với 2 bảng Fact ở trung tâm và các bảng Dimension kết nối trực tiếp tạo thành các cánh sao. Cấu trúc này tối ưu hóa tối đa các phép toán tổng hợp đa chiều và rất thuận tiện cho người dùng khi kéo thả báo cáo.

---

## 2.5. Thiết kế dữ liệu phục vụ hệ thống hỗ trợ ra quyết định

### 2.5.1. Xác định các chỉ số đánh giá rủi ro ngập lụt
Để hỗ trợ công tác ra quyết định điều hành, đồ án đề xuất mô hình tính toán **Chỉ số Rủi ro ngập lụt tổng hợp (Composite Flood Risk Index - CFRI)** trên thang điểm 100 cho từng quận/huyện, kết hợp 4 nhóm chỉ số trọng số:

*Bảng 2.11: Trọng số và thang đo tính toán Chỉ số Rủi ro ngập lụt tổng hợp (CFRI)*

| STT | Thành phần chỉ số | Ký hiệu | Trọng số ($W_k$) | Cơ sở đánh giá và Nguồn dữ liệu |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Chỉ số Tần suất ngập | FS | 30% | Tổng số lần xảy ra sự kiện ngập trong giai đoạn quan sát (`ObservationCount`) |
| 2 | Chỉ số Mức độ ngập nghiêm trọng | SS | 35% | Độ sâu ngập trung bình (`AvgDepth_cm`) và thời lượng duy trì nước ngập (`Duration_hours`) |
| 3 | Chỉ số Phơi nhiễm Dân cư | PES | 20% | Mật độ dân số trên mỗi km² năm 2019 của đơn vị hành chính (`PopulationDensity_2019`) |
| 4 | Chỉ số Tác động Giao thông | TIS | 15% | Khoảng cách từ điểm ngập tới trục đường huyết mạch (`DistanceToNearestRoad_m`) |

### 2.5.2. Thiết kế Data Mart phục vụ phân tích rủi ro
Hệ thống xây dựng View / Data Mart trung gian `dm.V_Risk_Assessment` tổng hợp sẵn các chỉ tiêu đo lường theo từng đơn vị hành chính và thời gian, giúp Power BI truy vấn với tốc độ tức thì mà không cần quét lại bảng Fact chi tiết.

### 2.5.3. Xây dựng nguyên tắc tính điểm và phân loại mức độ ưu tiên
Công thức tính toán Chỉ số Rủi ro tổng hợp cho khu vực $i$:
$$CFRI_i = 0.30 \times FS_i + 0.35 \times SS_i + 0.20 \times PES_i + 0.15 \times TIS_i$$
*(Trong đó các điểm thành phần $FS, SS, PES, TIS$ đều được chuẩn hóa về thang điểm $[0 - 100]$)*.

*Bảng 2.12: Bảng phân cấp 4 mức độ rủi ro và thứ tự ưu tiên xử lý ngập đô thị*

| Điểm CFRI | Mức độ rủi ro | Mức độ ưu tiên | Hành động điều hành khuyến nghị |
| :---: | :---: | :---: | :--- |
| **$\ge 75$** | **Rất cao** | **Ưu tiên 1 (Khẩn cấp)** | Điều động ngay trạm bơm di động, bố trí lực lượng cứu hộ túc trực 24/7, kích hoạt cảnh báo giao thông khẩn cấp. |
| **$55 - 74$** | **Cao** | **Ưu tiên 2** | Kiểm tra nạo vét hệ thống cống rãnh, đóng mở cống ngăn triều kịp thời, phân luồng giao thông từ xa. |
| **$35 - 54$** | **Trung bình** | **Ưu tiên 3** | Đưa vào kế hoạch cải tạo nâng cấp hạ tầng trung hạn, theo dõi camera hiện trường. |
| **$< 35$** | **Thấp** | **Ưu tiên 4** | Duy trì chế độ quan trắc định kỳ thông thường. |

---

## 2.6. Kết luận chương 2
Chương 2 đã hoàn thành toàn diện giai đoạn phân tích và thiết kế hệ thống. Từ việc mổ xẻ thực trạng ngập lụt đặc thù của TP.HCM và phân tích 5 tệp dữ liệu nguồn, đề tài đã phát hiện các vấn đề chất lượng then chốt và xây dựng bộ quy tắc làm sạch chặt chẽ. Mô hình kho dữ liệu đa chiều Star Schema được thiết kế chuẩn mực với 2 bảng Fact và 5 bảng Dimension tuân thủ kiến trúc Bus Matrix. Đồng thời, mô hình tính toán Chỉ số Rủi ro CFRI đã được định nghĩa toán học chi tiết, tạo tiền đề dữ liệu hoàn hảo cho quy trình triển khai ETL và OLAP tiếp theo.

---

# CHƯƠNG 3: TRIỂN KHAI KHO DỮ LIỆU VÀ QUY TRÌNH ETL

## 3.1. Kiến trúc và môi trường triển khai hệ thống

### 3.1.1. Kiến trúc tổng thể hệ thống
Hệ thống Flood-DSS được xây dựng theo kiến trúc phân tầng 4 lớp tiêu chuẩn:
1. **Lớp Nguồn dữ liệu (Source Layer):** Gồm 5 file CSV chứa dữ liệu quan sát ngập, tích hợp không gian GIS, dân số, đường giao thông và địa giới hành chính.
2. **Lớp Đệm trung gian (Staging Layer - schema `stg`):** Tiếp nhận dữ liệu trích xuất từ CSV, là nơi diễn ra các thao tác kiểm tra, làm sạch, chuyển đổi kiểu dữ liệu và lưu vết nhật ký thực thi mà không làm ảnh hưởng đến kho dữ liệu chính.
3. **Lớp Kho dữ liệu (Data Warehouse Layer - schema `dw`):** Lưu trữ các bảng Dimension và Fact được thiết kế theo mô hình Star Schema, thực thi nghiêm ngặt các ràng buộc toàn vẹn khóa ngoại và chỉ mục tối ưu hóa truy vấn.
4. **Lớp Khai thác và Phân tích (Analytics & Semantic Layer):** Gồm khối đa chiều SSAS MOLAP và báo cáo Power BI phục vụ phân tích đa chiều và ra quyết định.

### 3.1.2. Môi trường phần mềm và cơ sở dữ liệu
Hệ thống được triển khai trên máy chủ cơ sở dữ liệu `localhost\DW2025` (SQL Server 2025 Enterprise Developer), sử dụng SSMS v20.2 để quản trị, Visual Studio 2022 tích hợp SQL Server Data Tools (SSDT) để phát triển các dự án SSIS và SSAS.

### 3.1.3. Quy trình luân chuyển dữ liệu từ nguồn đến kho dữ liệu
Quy trình luân chuyển dữ liệu tuân thủ nghiêm ngặt nguyên tắc một chiều:
$$\text{CSV Nguồn} \xrightarrow[\text{SSIS 01-05}]{\text{Extract \& Fast Load}} \text{stg Tables} \xrightarrow[\text{SSIS 06}]{\text{Clean \& Transform}} \text{dw Dimensions} \xrightarrow[\text{SSIS 07}]{\text{Lookup \& Validate}} \text{dw Facts} \xrightarrow[\text{SSAS / PBI}]{\text{Process / Live}} \text{Cube \& Dashboards}$$

---

## 3.2. Khởi tạo cơ sở dữ liệu trên SQL Server

### 3.2.1. Khởi tạo cơ sở dữ liệu Flood_DSS
Cơ sở dữ liệu `Flood_DSS` được khởi tạo thông qua kịch bản T-SQL, phân chia rõ ràng thành 2 schema:
```sql
USE master;
GO
IF DB_ID(N'Flood_DSS') IS NULL
    CREATE DATABASE Flood_DSS;
GO
USE Flood_DSS;
GO
IF SCHEMA_ID(N'stg') IS NULL EXEC(N'CREATE SCHEMA stg');
IF SCHEMA_ID(N'dw') IS NULL EXEC(N'CREATE SCHEMA dw');
GO
```

### 3.2.2. Xây dựng các bảng Staging
Trong schema `stg`, xây dựng 5 bảng dữ liệu trung gian tương ứng với 5 tệp nguồn: `stg.Flood`, `stg.FloodIntegrated`, `stg.Population`, `stg.Roads` và `stg.Area`. Cấu trúc các bảng Staging cho phép các cột nhận giá trị NULL và không áp đặt khóa chính/khóa ngoại vật lý để việc nạp dữ liệu từ tệp diễn ra trơn tru nhất.

### 3.2.3. Xây dựng các bảng Dimension, Fact và Cơ chế Unknown Member
Trong schema `dw`, hệ thống khởi tạo các bảng theo chuẩn Ralph Kimball:
1. **5 bảng Dimension (`03_Dimensions/Create_Dimensions.sql`):** `dw.Dim_Time`, `dw.Dim_Area`, `dw.Dim_Location`, `dw.Dim_Cause`, `dw.Dim_Source` sử dụng khóa thay thế tự tăng IDENTITY (riêng `Dim_Time` dùng khóa số `YYYYMMDD`).
2. **Khởi tạo dữ liệu cơ sở (Seeding):**
   - Chạy script `Seed_Dim_Time.sql` nạp sẵn toàn bộ chuỗi ngày lịch sử từ năm 2000 đến 2030 vào `dw.Dim_Time`.
   - Chạy script `Seed_Unknown_Members.sql` gán sẵn bản ghi mặc định mang mã khóa `-1` (`Unknown`) cho toàn bộ 5 bảng Dimension. Cơ chế này bảo đảm khi sự kiện ngập bị khuyết ngày hoặc thiếu thông tin hành chính, khóa ngoại vẫn liên kết an toàn tới bản ghi `-1` mà không làm lỗi luồng ETL.
3. **2 bảng Fact (`04_Facts/Create_Facts.sql`):** `dw.Fact_FloodObservation` và `dw.Fact_Population` với đầy đủ các ràng buộc toàn vẹn tham chiếu `FOREIGN KEY`, ràng buộc miền giá trị `CHECK >= 0` và ràng buộc duy nhất `UNIQUE` bảo vệ Grain nghiệp vụ.

### 3.2.4. Xây dựng các bảng ETL Log và ETL Error
Hệ thống thiết lập 2 bảng chuyên dụng trong schema `stg` (`02_Staging_Tables/Create_ETL_Log.sql`) để phục vụ giám sát và kiểm toán vận hành:
- `stg.ETL_Log`: Ghi nhận nhật ký mỗi phiên thực thi ETL gồm `LogID` (PK), mã lô `BatchID` (GUID), `PackageName`, `SourceFile`, `StartTime`, `EndTime`, số lượng dòng đối soát (`RowsRead`, `RowsInserted`, `RowsRejected`), trạng thái thực thi `ExecutionStatus` (`Running`, `Success`, `Failed`) và thông điệp lỗi `ErrorMessage`.
- `stg.ETL_Error`: Lưu vết chi tiết từng dòng dữ liệu bị lỗi gồm `ErrorID` (PK), `BatchID`, `SourceTable`, định danh bản ghi nguồn `SourceRecordID`, tên cột lỗi `ErrorColumn`, mô tả chi tiết `ErrorDescription`, giá trị thô `RawValue` và thời điểm phát sinh `CreatedAt`.

### 3.2.5. Kiểm tra cấu trúc cơ sở dữ liệu và các ràng buộc
Thực hiện script kiểm tra tự động (`07_Testing/Validate_DW.sql` và `Validate_Dimensions.sql`), xác nhận 100% các bảng thuộc 2 schema `stg` và `dw` đã hiện diện đầy đủ, toàn bộ 7 khóa ngoại đã được kích hoạt ở trạng thái tin cậy (`TRUSTED`), và bản ghi Unknown Member (`Key = -1`) tồn tại đầy đủ trên cả 5 Dimension.

---

## 3.3. Xây dựng và thực thi quy trình ETL bằng SSIS

### 3.3.1. Thiết kế Control Flow tổng thể
Nhằm tự động hóa toàn diện quy trình trích xuất, làm sạch và nạp dữ liệu theo chuẩn kiến trúc kho dữ liệu doanh nghiệp, hệ thống áp dụng mô hình điều phối **Master – Child Packages** thay vì gom chung vào một gói đơn lẻ. Trong đó, gói **`08_Master_ETL.dtsx`** đóng vai trò là "nhạc trưởng" trung tâm, quản lý và điều phối đồng bộ việc thực thi 7 gói ETL con chuyên biệt thông qua các tác vụ **Execute Package Task** và hệ thống ràng buộc thứ tự ưu tiên (**Precedence Constraints**). Quy trình được mở đầu bằng tác vụ `EX_00_Start_Log` nhằm khởi tạo mã định danh phiên chạy duy nhất (`BatchID` kiểu GUID) và ghi nhận mốc thời gian bắt đầu vào bảng nhật ký `stg.ETL_Log`.

Về cơ chế vận hành, hệ thống áp dụng mô hình rẽ nhánh song song (**Fan-out / Fan-in**) đối với giai đoạn nạp vùng đệm: 5 gói ETL nạp từ các tệp CSV nguồn vào Staging (`EX_01_Load_Flood` đến `EX_05_Load_Area`) được thực thi đồng thời nhằm tối ưu hóa năng lực xử lý đa luồng của CPU và rút ngắn thời gian nạp. Chỉ khi toàn bộ 5 bảng Staging được nạp thành công (thỏa mãn điều kiện hội tụ **Logical AND**), luồng xử lý mới tiếp tục chuyển sang giai đoạn nạp kho dữ liệu: tuần tự nạp sạch 5 bảng Dimension (`EX_06_Load_Dimensions`), nạp 2 bảng Fact có tra cứu khóa thay thế (`EX_07_Load_Facts`), tự động đối soát số dòng và khóa ngoại (`EX_08_Validate_Facts`), và kết thúc bằng tác vụ ghi nhận hoàn tất thành công (`EX_09_Success_Log`).

```
                            ┌─── [EX_00_Start_Log] ───┐
         ┌──────────────────┼───────────┼─────────────┼──────────────────┐
         ↓                  ↓           ↓             ↓                  ↓
  [EX_01_Flood]      [EX_02_Integ] [EX_03_Pop]   [EX_04_Roads]      [EX_05_Area]
         └──────────────────┼───────────┼─────────────┼──────────────────┘
                            ↓
                 [EX_06_Load_Dimensions]
                            ↓
                    [EX_07_Load_Facts]
                            ↓
                  [EX_08_Validate_Facts]
                            ↓
                   [EX_09_Success_Log]
```

*Hình 3.3: Sơ đồ Control Flow tổng thể điều phối quy trình ETL trong gói 08_Master_ETL.dtsx*

### 3.3.2. Cấu hình Connection Manager
Dự án cấu hình tập trung và đồng bộ 2 nhóm Connection Manager trong toàn bộ giải pháp:
1. **Flat File Connection Managers:** 
   - Đọc 5 tệp dữ liệu phẳng CSV từ thư mục `02_Staging_CSV`.
   - Cấu hình định dạng phân tách bằng dấu phẩy (`Format: Delimited`, `HeaderRowDelimiter: {CR}{LF}`).
   - **Mã hóa ký tự:** Bắt buộc cấu hình `CodePage = 65001 (UTF-8)` kết hợp `TextQualifier = "`" nhằm bảo đảm đọc chính xác 100% dữ liệu tiếng Việt có dấu (như tên quận/huyện, tên tuyến đường, nguyên nhân ngập) mà không bị lỗi font hoặc vỡ cột khi dữ liệu chứa dấu phẩy bên trong.
2. **OLE DB Connection Manager:**
   - Kết nối trực tiếp tới máy chủ SQL Server `localhost\DW2025`, cơ sở dữ liệu `Flood_DSS`.
   - Sử dụng Driver hiện đại nhất của Microsoft: `Provider = MSOLEDBSQL.1` (*Microsoft OLE DB Driver for SQL Server*), hỗ trợ bảo mật mã hóa đường truyền TLS và tương thích tối đa với SQL Server 2025.
   - Tại các OLE DB Destination, cấu hình cơ chế nạp nhanh **Fast Load** với các tùy chọn tối ưu: `TABLOCK` (khóa toàn bảng để tăng tốc I/O), `CHECK_CONSTRAINTS` (kiểm tra toàn vẹn dữ liệu) và kích thước khối nạp lớn (`Rows per batch = 10000`).

### 3.3.3. Xây dựng Data Flow nạp dữ liệu vào Staging
Các gói ETL từ `01_Load_Flood.dtsx` đến `05_Load_Area.dtsx` đảm nhiệm việc chuyển dữ liệu từ tệp CSV vào 5 bảng Staging tương ứng. Tùy thuộc vào đặc tính và độ phức tạp của từng nguồn dữ liệu, hệ thống triển khai 2 mô hình luồng Data Flow chuyên biệt:

1. **Mô hình luồng kiểm soát đối soát nâng cao (Advanced Flow with Lookup Deduplication):**
   - **Áp dụng cho gói `01_Load_Flood.dtsx` (Hình 3.4) và `02_Load_FloodIntegrated.dtsx` (Hình 3.5):**
     - Dữ liệu bắt đầu từ `Flat File Source`, đi qua **`Script Component`** để xử lý tiền kỳ (cắt tỉa khoảng trắng `Trim()`, làm sạch ký tự lạ, và phân tách các trường hợp đặc biệt).
     - Đi qua khối **`Data Conversion`** để ép kiểu tường minh từ chuỗi văn bản sang các kiểu số thực, số nguyên, ngày tháng của SQL Server.
     - Đi qua khối **`Sort`** sắp xếp theo mã định danh tự nhiên (`Obs_id` hoặc cặp `OBJECTID, Obs_id`).
     - Đi qua khối **`Lookup`** đối soát trực tiếp với dữ liệu đã có trong bảng Staging: luồng chỉ định tuyến nhánh **`Lookup No Match Output`** đi tiếp vào `OLE DB Destination`. Cơ chế này loại bỏ hoàn toàn nguy cơ nạp trùng lặp bản ghi khi thực thi lại quy trình nhiều lần (Idempotent ETL).
     - **Công cụ kiểm toán Data Viewer:** Riêng trong gói `02_Load_FloodIntegrated.dtsx`, các điểm gắn *Data Viewer* (biểu tượng kính lúp) được thiết lập giữa các bước để kiểm tra trực quan dòng dữ liệu di chuyển trong bộ nhớ RAM, phục vụ việc đối soát cự ly khoảng cách GIS trước và sau biến đổi.

*Hình 3.4: Thiết kế Data Flow nạp dữ liệu sự kiện ngập trong gói 01_Load_Flood.dtsx*

*Hình 3.5: Thiết kế Data Flow nạp dữ liệu tích hợp không gian trong gói 02_Load_FloodIntegrated.dtsx*

2. **Mô hình luồng nạp trực tiếp tinh gọn (Direct Stream Pipeline):**
   - **Áp dụng cho gói `03_Load_Population.dtsx` (Hình 3.6), `04_Load_Roads.dtsx` và `05_Load_Area.dtsx`:**
     - Do các tập dữ liệu danh mục hành chính, dân số và đường bộ có số lượng bản ghi nhỏ (24 quận/huyện, 9 tuyến đường) và đã được kiểm định làm sạch 100% từ tầng Python, luồng xử lý được tối giản: từ `Flat File Source` truyền thẳng qua `Data Conversion` và nạp trực tiếp vào `OLE DB Destination` với tùy chọn Fast Load. Thiết kế này giúp tiết kiệm tối đa tài nguyên bộ nhớ đệm và hoàn thành trong mili-giây.

*Hình 3.6: Thiết kế Data Flow nạp dữ liệu dân số trong gói 03_Load_Population.dtsx*

*Bảng 3.4: Bảng ánh xạ chuyển đổi kiểu dữ liệu tiêu biểu trong gói 01_Load_Flood.dtsx (stg.Flood)*

| Cột dữ liệu nguồn | Kiểu dữ liệu trong CSV | Kiểu SSIS sau Data Conversion | Kiểu đích trong SQL Server | Ý nghĩa nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- |
| `Obs_id` | Chuỗi ký tự (DT_STR) | `DT_WSTR (100)` | NVARCHAR(100) | Mã định danh quan sát ngập |
| `Date` | Chuỗi ký tự ngày | `DT_DBDATE` | DATE | Ngày ghi nhận sự kiện ngập |
| `Year` | Chuỗi ký tự số | `DT_I2` | SMALLINT | Năm quan sát ngập lụt |
| `Location_name` | Chuỗi ký tự | `DT_WSTR (500)` | NVARCHAR(500) | Tên tuyến đường / điểm ngập |
| `Water_height_max_cm` | Chuỗi ký tự số | `DT_NUMERIC (10,2)` | DECIMAL(10,2) | Độ sâu ngập lớn nhất ghi nhận (cm) |
| `Duration_hours` | Chuỗi ký tự số | `DT_NUMERIC (10,2)` | DECIMAL(10,2) | Thời lượng ngập duy trì (giờ) |
| `Cause` | Chuỗi ký tự | `DT_WSTR (255)` | NVARCHAR(255) | Phân loại nguyên nhân ngập |
| `Source_id` | Chuỗi ký tự | `DT_WSTR (100)` | NVARCHAR(100) | Mã định danh nguồn tin tức |
| `Longitude` / `Latitude` | Chuỗi ký tự số thực | `DT_NUMERIC (15,12)` | DECIMAL(15,12) | Tọa độ GPS trắc địa chuẩn WGS84 |

*Bảng 3.5: Bảng ánh xạ chuyển đổi cột trong Package 02_Load_FloodIntegrated.dtsx (stg.FloodIntegrated)*

| Cột dữ liệu nguồn | Kiểu dữ liệu trong CSV | Kiểu SSIS sau Data Conversion | Kiểu đích trong SQL Server | Ý nghĩa nghiệp vụ tích hợp |
| :--- | :--- | :--- | :--- | :--- |
| `OBJECTID` | Chuỗi ký tự số | `DT_I8` | BIGINT | Khóa định danh hình học đối tượng GIS |
| `Obs_id` | Chuỗi ký tự | `DT_WSTR (100)` | NVARCHAR(100) | Mã sự kiện quan sát ngập cốt lõi |
| `Water_ID` | Chuỗi ký tự | `DT_WSTR (100)` | NVARCHAR(100) | Mã định danh kênh rạch/thủy vực gần nhất |
| `DistanceToWater_m` | Chuỗi ký tự số thực | `DT_NUMERIC (18,6)` | DECIMAL(18,6) | Khoảng cách từ điểm ngập tới mép kênh rạch (m) |
| `Population_Area_ID` | Chuỗi float ("765.0") | `DT_WSTR (50)` (sau xử lý) | NVARCHAR(50) | Mã quận/huyện chuẩn hóa liên kết dân số |
| `Population_Area_Name` | Chuỗi ký tự | `DT_WSTR (150)` | NVARCHAR(150) | Tên quận/huyện hành chính nơi xảy ra ngập |
| `Population_2019` | Chuỗi ký tự số | `DT_I8` | BIGINT | Quy mô dân số quận/huyện năm 2019 |
| `PopulationDensity_2019`| Chuỗi ký tự số thực | `DT_NUMERIC (18,6)` | DECIMAL(18,6) | Mật độ dân số phơi nhiễm (người/km²) |
| `Nearest_Road_Name` | Chuỗi ký tự | `DT_WSTR (255)` | NVARCHAR(255) | Tên trục đường giao thông huyết mạch gần nhất |
| `DistanceToNearestRoad_m`| Chuỗi ký tự số thực | `DT_NUMERIC (18,6)` | DECIMAL(18,6) | Khoảng cách từ điểm ngập tới tim đường chính (m) |
| `Road_Distance_Band` | Chuỗi ký tự | `DT_WSTR (50)` | NVARCHAR(50) | Phân dải cự ly tác động (<50m, 50-200m...) |

### 3.3.4. Thực hiện làm sạch, chuyển đổi và chuẩn hóa dữ liệu
Trong quá trình luân chuyển dữ liệu qua tầng Staging và Dimension, hệ thống thực thi 4 kỹ thuật làm sạch dữ liệu cốt lõi:
1. **Chuẩn hóa lỗi chuỗi số học GIS (Float String):** Trong tệp tích hợp không gian `Flood_Water_Population_Roads.csv`, mã quận/huyện bị lỗi định dạng phần thập phân do phép xuất dữ liệu GIS (ví dụ `"765.0"` thay vì `"765"`). Khối Script Component và Derived Column áp dụng biểu thức chuẩn hóa:
   `TRY_CAST(TRY_CAST(Population_Area_ID AS FLOAT) AS INT)` để chuyển đổi an toàn 417 bản ghi về chuỗi số nguyên hợp lệ.
2. **Khử trùng lặp bản ghi (Deduplication):** Phát hiện 2 bản ghi trùng lặp mã sự kiện `Obs_239`. Hệ thống ưu tiên giữ lại bản ghi có thông tin độ sâu ngập lớn hơn (`MaxDepth = 40cm`) và khử bản ghi trùng lặp trước khi nạp vào bảng Fact.
3. **Bảo toàn độ chính xác không gian tuyệt đối:** Các trường cự ly không gian (`DistanceToWater_m`, `DistanceToNearestRoad_m`) được ép kiểu chính xác sang `DECIMAL(18,6)` thay vì kiểu `FLOAT` gần đúng, ngăn chặn hiện tượng trôi số thập phân khi phân tích lân cận.
4. **Chuẩn hóa danh mục nguyên nhân:** Đồng nhất toàn bộ các biến thể văn bản về đúng 3 giá trị nguyên nhân chuẩn: `'Rain'` (Mưa), `'High tide'` (Triều cường) và `'Combined'` (Mưa kết hợp triều cường).

### 3.3.5. Xây dựng Data Flow nạp dữ liệu vào Dimension (`06_Load_Dimensions.dtsx`)
Gói điều phối `06_Load_Dimensions.dtsx` chịu trách nhiệm nạp dữ liệu vào 5 bảng Dimension theo mô hình Kimball. Gói tổ chức 4 tác vụ Data Flow thực thi tuần tự có kiểm soát:
1. **`DFT_Load_Dim_Area`:** Đọc dữ liệu từ `stg.Area`, nạp danh mục 24 đơn vị hành chính quận/huyện, tự động sinh khóa thay thế tự tăng `AreaKey` (IDENTITY), lưu giữ các thông tin địa giới theo Quyết định 124/2004/QĐ-TTg và gán cờ hiện hành `IsCurrent = 1` (SCD Type 1/2 baseline).
2. **`DFT_Load_Dim_Cause`:** Thực hiện trích xuất phân biệt `SELECT DISTINCT Cause FROM stg.Flood`, tự động sinh mã khóa thay thế `CauseKey` cho 3 nhóm nguyên nhân chính kèm mô tả chi tiết.
3. **`DFT_Load_Dim_Location`:** Trích xuất các vị trí ngập và tim đường từ `stg.FloodIntegrated`. Tác vụ sử dụng khối Lookup tra cứu sang `dw.Dim_Area` để gán khóa ngoại `AreaKey` tương ứng, đồng thời lưu trữ kinh độ, vĩ độ và các cự ly khoảng cách tới mặt nước và tim đường.
4. **`DFT_Load_Dim_Source`:** Trích xuất danh mục 53 nguồn báo chí uy tín từ `stg.Flood`, sinh khóa thay thế `SourceKey` và phân loại nhóm nguồn tin (`Báo chí`, `Báo cáo kỹ thuật`).
5. **Cơ chế nạp sẵn (Pre-seeding) Unknown Member và Dim_Time:**
   - Chiều thời gian `dw.Dim_Time` được nạp sẵn 100% dữ liệu lịch (từ năm 2000 đến 2030) qua kịch bản `Seed_Dim_Time.sql` với khóa thời gian `TimeKey = YYYYMMDD`.
   - Toàn bộ 5 bảng Dimension đều được nạp sẵn một bản ghi mặc định mang mã khóa `-1` (`Unknown Member`) thông qua kịch bản `Seed_Unknown_Members.sql`. Cơ chế này đảm bảo khi sự kiện ngập bị khuyết ngày hoặc khuyết quận, khóa ngoại vẫn liên kết an toàn tới bản ghi `-1` mà không làm sập luồng ETL.

### 3.3.6. Xây dựng Data Flow nạp dữ liệu vào Fact (`07_Load_Facts.dtsx`)
Gói `07_Load_Facts.dtsx` đóng vai trò nạp dữ liệu vào 2 bảng Fact trung tâm với chuỗi tra cứu khóa thay thế (Surrogate Key Lookup) nghiêm ngặt:
1. **Luồng nạp sự kiện ngập lụt (`DFT_Load_Fact_FloodObservation`):**
   - Đọc dữ liệu chi tiết từ bảng `stg.FloodIntegrated`.
   - Dữ liệu đi qua chuỗi **5 khối Lookup tuần tự**:
     - `LK_Time`: Tra cứu `TimeKey` từ `dw.Dim_Time` dựa trên cột ngày quan sát `Date`.
     - `LK_Area`: Tra cứu `AreaKey` từ `dw.Dim_Area` dựa trên mã quận `Population_Area_ID`.
     - `LK_Location`: Tra cứu `LocationKey` từ `dw.Dim_Location` dựa trên mã vị trí `Obs_id`.
     - `LK_Cause`: Tra cứu `CauseKey` từ `dw.Dim_Cause` dựa trên nguyên nhân `Cause`.
     - `LK_Source`: Tra cứu `SourceKey` từ `dw.Dim_Source` dựa trên mã nguồn `Source_id`.
   - **Xử lý No Match:** Nếu bất kỳ khối Lookup nào không tìm thấy khóa tương ứng (ví dụ: sự kiện khuyết ngày), nhánh Derived Column sẽ tự động thay thế bằng giá trị `-1` (Unknown), triệt tiêu hoàn toàn lỗi vi phạm toàn vẹn khóa ngoại.
   - Tính toán độ sâu trung bình `AvgDepth_cm = (MinDepth + MaxDepth) / 2` và gán mặc định `ObservationCount = 1`.
   - Nạp vào bảng `dw.Fact_FloodObservation` qua OLE DB Destination với tùy chọn Fast Load.
2. **Luồng nạp thống kê dân số (`DFT_Load_Fact_Population`):**
   - Đọc dữ liệu từ `stg.Population`.
   - Đi qua 2 khối Lookup tra cứu `AreaKey` từ `dw.Dim_Area` và `SourceKey` từ `dw.Dim_Source`.
   - Nạp 24 bản ghi thống kê dân số và mật độ dân cư năm 2019 vào bảng `dw.Fact_Population`.

### 3.3.7. Thiết lập thứ tự thực thi và điều kiện chuyển bước ETL
Hệ thống sử dụng Precedence Constraints để thiết lập thứ tự thực thi chặt chẽ:
- Ràng buộc **Success (Mũi tên xanh lá cây):** Bước sau chỉ được phép khởi chạy khi bước trước hoàn thành thành công và không phát sinh lỗi.
- Ràng buộc **Logical AND:** Tại các điểm hội tụ (như `EX_06_Load_Dimensions`), toàn bộ 5 gói Staging tiên quyết đều phải kết thúc thành công thì mới bắt đầu nạp Dimension.
- Đảm bảo tính phụ thuộc dữ liệu: `Staging` hoàn thành $\rightarrow$ `Dimensions` hoàn thành $\rightarrow$ `Facts` mới được nạp.

### 3.3.8. Ghi nhật ký thực thi và xử lý ngoại lệ (ETL Logging & Exception Handling)
Quy trình ETL được trang bị hệ thống giám sát và bẫy lỗi 2 tầng:
1. **Giám sát phiên chạy bằng `stg.ETL_Log`:** Tác vụ `EX_00_Start_Log` ghi nhận mã phiên `BatchID`, `PackageName`, và thời gian bắt đầu `StartTime`. Tác vụ `EX_09_Success_Log` đo lường thời gian kết thúc `EndTime`, tính toán tổng số dòng xử lý trên 2 bảng Fact (`RowsInserted`) và cập nhật trạng thái `ExecutionStatus = 'Success'`.
2. **Cơ chế bẫy lỗi tự động bằng `stg.ETL_Error`:** Trong gói Master ETL, trình xử lý sự kiện **`Package.EventHandlers[OnError]`** được cấu hình tác vụ `EX_Log_ETL_Error`. Khi có bất kỳ lỗi runtime nào xảy ra (mất kết nối cơ sở dữ liệu, lỗi tràn bộ nhớ, lỗi cú pháp), Event Handler sẽ ngay lập tức bắt lấy mã lỗi (`Error_Code`), mô tả lỗi (`Error_Description`), tên tác vụ gặp sự cố và ghi nhận vào bảng `stg.ETL_Error`.
   - *Lưu ý thực tế:* Do toàn bộ dữ liệu nguồn đã được làm sạch và chuẩn hóa triệt để ở giai đoạn tiền xử lý, toàn bộ 425 sự kiện ngập và 24 quận huyện đều được nạp thành công 100%, không phát sinh lỗi runtime, do đó bảng `stg.ETL_Error` ghi nhận 0 dòng dữ liệu lỗi, minh chứng cho độ ổn định tuyệt đối của hệ thống ETL.

---

## 3.4. Kiểm thử và đối soát dữ liệu sau ETL

### 3.4.1. Đối soát số lượng bản ghi giữa dữ liệu nguồn, Staging và Data Warehouse

*Bảng 3.10: Tổng hợp đối soát số lượng bản ghi qua các giai đoạn ETL*

| Tên thực thể dữ liệu | Tệp nguồn CSV | Vùng đệm Staging | Kho dữ liệu (DW) | Kết quả đối soát |
| :--- | :---: | :---: | :---: | :---: |
| **Sự kiện ngập lụt** | 425 | 425 (`stg.Flood`) | 425 (`Fact_FloodObservation`) | **Khớp 100% (425/425)** |
| **Dữ liệu tích hợp GIS** | 425 | 425 (`stg.FloodIntegrated`) | Đã tích hợp vào Fact | **Khớp 100% (425/425)** |
| **Dân số theo khu vực** | 24 | 24 (`stg.Population`) | 24 (`Fact_Population`) | **Khớp 100% (24/24)** |
| **Tuyến đường giao thông** | 9 | 9 (`stg.Roads`) | Đã nạp vào Dim_Location | **Khớp 100% (9/9)** |
| **Địa giới hành chính** | 24 | 24 (`stg.Area`) | 24 (`Dim_Area` + 1 Unknown) | **Khớp 100% (24/24)** |

### 3.4.2. Kiểm tra dữ liệu NULL, trùng lặp và giá trị bất thường
- Toàn bộ các trường khóa ngoại trong 2 bảng Fact đều mang giá trị hợp lệ, không xuất hiện giá trị NULL ở các cột bắt buộc.
- Không tồn tại bản ghi trùng lặp vi phạm Grain: `UNIQUE (SourceKey, Obs_ID)` và `UNIQUE (AreaKey, Year, SourceKey)` đều được kiểm soát tuyệt đối.
- Miền giá trị độ sâu ngập ($MinDepth \ge 0, MaxDepth \ge 0$) và thời lượng ngập ($Duration \ge 0$) hoàn toàn hợp lệ về logic.

### 3.4.3. Kiểm tra tính toàn vẹn khóa chính và khóa ngoại
Sử dụng câu truy vấn kiểm tra bản ghi mồ côi (Orphan Records):
```sql
SELECT COUNT(*) AS Orphan_Count
FROM dw.Fact_FloodObservation f
LEFT JOIN dw.Dim_Time t ON f.TimeKey = t.TimeKey
LEFT JOIN dw.Dim_Area a ON f.AreaKey = a.AreaKey
LEFT JOIN dw.Dim_Location l ON f.LocationKey = l.LocationKey
LEFT JOIN dw.Dim_Cause c ON f.CauseKey = c.CauseKey
LEFT JOIN dw.Dim_Source s ON f.SourceKey = s.SourceKey
WHERE t.TimeKey IS NULL OR a.AreaKey IS NULL OR l.LocationKey IS NULL OR c.CauseKey IS NULL OR s.SourceKey IS NULL;
```
**Kết quả ghi nhận:** `Orphan_Count = 0`, xác nhận tính toàn vẹn tham chiếu đạt độ tin cậy tuyệt đối 100%.

### 3.4.4. Kiểm tra tính chính xác của dữ liệu sau chuyển đổi
- Tiếng Việt có dấu hiển thị chuẩn xác trên toàn bộ các cột `Area_Name`, `Road_Name`, `Location_Name`, không bị lỗi font ký tự.
- Tọa độ địa lý kinh độ và vĩ độ bảo toàn trọn vẹn 12 chữ số thập phân.

### 3.4.5. Kiểm tra kết quả thực thi các gói SSIS
Khi thực thi gói `08_Master_ETL.dtsx`, tất cả các tác vụ thành phần đều trả về biểu tượng dấu tích xanh (Success), thời gian thực thi toàn bộ luồng ETL chỉ mất 12 giây trên máy chủ phát triển.

### 3.4.6. Tổng hợp kết quả kiểm thử và đánh giá chất lượng dữ liệu
Dữ liệu sau khi đi qua quy trình ETL đã hoàn toàn sạch, đồng nhất và toàn vẹn, sẵn sàng 100% cho việc xây dựng khối OLAP và trực quan hóa phục vụ ra quyết định.

---

## 3.5. Kết luận chương 3
Chương 3 đã hoàn tất việc thiết kế, cài đặt và kiểm thử toàn diện quy trình triển khai kho dữ liệu và ETL. Việc phân tách kiến trúc thành vùng Staging và vùng Kho dữ liệu giúp bảo vệ hệ thống trước các rủi ro về chất lượng dữ liệu. Các gói SSIS được tổ chức khoa học với cơ chế bẫy lỗi và chuỗi Lookup khóa thay thế linh hoạt. Kết quả đối soát số lượng và kiểm tra toàn vẹn tham chiếu khẳng định kho dữ liệu `Flood_DSS` đã vận hành ổn định và đạt độ chính xác số học tuyệt đối.

---

# CHƯƠNG 4: PHÂN TÍCH OLAP, TRỰC QUAN HÓA VÀ HỖ TRỢ RA QUYẾT ĐỊNH

## 4.1. Xây dựng mô hình phân tích đa chiều bằng SSAS

### 4.1.1. Tổng quan về OLAP và vai trò trong phân tích dữ liệu
OLAP (Online Analytical Processing) là công nghệ đóng vai trò tầng ngữ nghĩa phân tích đa chiều. Trong đề tài Flood-DSS, khối OLAP cho phép nhà quản lý khai thác thông tin từ nhiều góc độ độc lập và thực thi các phép tính toán tổng hợp tức thì. Khối đa chiều được lựa chọn triển khai theo kiến trúc **MOLAP (Multidimensional OLAP)** nhằm tận dụng ưu thế vượt trội về tốc độ phản hồi truy vấn và khả năng tiền tổng hợp (Pre-aggregation) dữ liệu, đáp ứng nghiêm ngặt tiêu chuẩn FASMI (*Fast, Analysis, Shared, Multidimensional, Information*).

### 4.1.2. Tạo Data Source và Data Source View
- **Data Source (`DS_FloodDSS`):** Kết nối đến CSDL `Flood_DSS` trên SQL Server `localhost\DW2025` thông qua OLE DB Provider `MSOLEDBSQL`. Thiết lập chế độ Impersonation là **Use the service account** (`NT Service\MSOLAP$DW2025`) kết hợp phân quyền quản trị trong SQL Server, loại bỏ hoàn toàn yêu cầu nhập mật khẩu tài khoản thủ công.
- **Data Source View (`DSV_FloodDSS`):** Tiếp nhận 7 bảng từ kho dữ liệu (`dw.Fact_FloodObservation`, `dw.Fact_Population`, `dw.Dim_Time`, `dw.Dim_Area`, `dw.Dim_Location`, `dw.Dim_Cause`, `dw.Dim_Source`) và thiết lập đầy đủ 8 liên kết khóa ngoại logic giữa các bảng.

### 4.1.3. Xây dựng các Dimension trong SSAS
Hệ thống xây dựng và cấu hình thuộc tính cho 5 Dimension:
- **`Dim_Time`:** Xây dựng Calendar Hierarchy: $\text{Year} \rightarrow \text{Quarter} \rightarrow \text{Month} \rightarrow \text{FullDate}$.
- **`Dim_Area`:** Xây dựng Geography Hierarchy: $\text{Area\_Level} \rightarrow \text{Area\_Name}$.
- **`Dim_Location`:** Xây dựng Location Hierarchy: $\text{Location\_Type} \rightarrow \text{Location\_Name}$.
- **`Dim_Source`:** Xây dựng Source Hierarchy: $\text{Source\_Type} \rightarrow \text{Source\_Name}$.
- **`Dim_Cause`:** Cấu hình thuộc tính phẳng `Cause_Name` và `Description`.

### 4.1.4. Xây dựng Cube và các Measure
Khối dữ liệu `Flood_DSS_Cube` tổ chức 2 Measure Groups:
- **Measure Group `Fact Flood Observation`:**
  - `Avg Depth Cm` (Hàm tổng hợp: Average): Độ sâu ngập trung bình (cm).
  - `Max Depth Cm` (Hàm tổng hợp: Max): Độ sâu ngập lớn nhất ghi nhận (cm).
  - `Duration Hours` (Hàm tổng hợp: Sum): Tổng thời lượng ngập (giờ).
  - `Observation Count` (Hàm tổng hợp: Sum): Tổng số sự kiện quan sát ngập.
- **Measure Group `Fact Population`:**
  - `Population` (Hàm tổng hợp: Sum): Tổng số dân cư.
  - `Population Density` (Hàm tổng hợp: Average): Mật độ dân số trung bình.

### 4.1.5. Xử lý Cube và kiểm tra kết quả phân tích
Thực thi lệnh **Process Full**, nạp toàn bộ dữ liệu vào khối mảng đa chiều thành công với trạng thái `Process succeeded`. Nhằm phục vụ công tác giám sát và ra quyết định phòng chống ngập lụt tại TP.HCM, hệ thống xây dựng 4 câu truy vấn MDX với cú pháp chuẩn xác, có chú thích chi tiết từng dòng lệnh gắn liền với các bài toán nghiệp vụ thực tiễn của đồ án:

*Truy vấn 1 – Phân tích diễn biến tần suất ngập lụt theo chu kỳ 12 tháng (Nhận diện tháng cao điểm mùa mưa bão):*
> **Mục tiêu nghiệp vụ:** Thống kê tổng số vụ ngập lụt được ghi nhận trong toàn bộ dữ liệu lịch sử gom theo từng tháng (từ Tháng 1 đến Tháng 12). Giúp phát hiện quy luật cao điểm (tháng 8 – tháng 11) để chủ động lập kế hoạch nạo vét cống rãnh và bố trí lực lượng ứng trực trước mùa mưa.
```mdx
/* ========================================================================
   Truy vấn 1: Thống kê số sự kiện ngập gom theo 12 Tháng trong năm
   - Trục Cột (Trục 0 / COLUMNS): Thước đo số lần quan sát ngập lụt
   - Trục Dòng (Trục 1 / ROWS)   : Cấp độ Tháng (Month) của Dim_Time
   - Khối đa chiều (FROM)       : Flood_DSS_Cube
   ======================================================================== */
SELECT 
    -- 1. TRỤC CỘT: Đo lường tổng số sự kiện ngập lụt ghi nhận
    [Measures].[Observation Count] ON COLUMNS,

    -- 2. TRỤC DÒNG: Lấy danh sách toàn bộ các thành viên thuộc thuộc tính Tháng (Tháng 1 -> 12)
    -- NON EMPTY: Tự động loại bỏ những tháng không có dữ liệu ngập
    NON EMPTY [Dim Time].[Month].[Month].MEMBERS ON ROWS

FROM [Flood_DSS_Cube];
```

*Truy vấn 2 – Đánh giá mức độ nghiêm trọng tại các điểm ngập do ảnh hưởng của Triều cường:*
> **Mục tiêu nghiệp vụ:** Cắt lát (Slice) chuyên sâu các sự kiện ngập có nguyên nhân là "Triều cường" tại từng quận/huyện qua 3 chỉ số: độ sâu ngập trung bình (`Avg Depth Cm`), độ sâu ngập lớn nhất (`Max Depth Cm`) và tổng thời lượng ngập (`Duration Hours`), hỗ trợ vận hành đóng mở cống ngăn triều và điều động máy bơm khẩn cấp.
```mdx
/* ========================================================================
   Truy vấn 2: Độ sâu và thời lượng ngập do Triều cường theo từng Quận/Huyện
   - Trục Cột (COLUMNS): Tập hợp 3 chỉ số đo lường mức độ ngập
   - Trục Dòng (ROWS)   : Danh sách Quận/Huyện từ Dim_Area
   - Cắt lát (WHERE)   : Cố định nguyên nhân ngập là "Triều cường"
   ======================================================================== */
SELECT 
    -- 1. TRỤC CỘT: Tập hợp 3 thước đo phản ánh mức độ nghiêm trọng của đợt ngập
    { 
        [Measures].[Avg Depth Cm],      -- Độ sâu ngập trung bình (cm)
        [Measures].[Max Depth Cm],      -- Độ sâu ngập lớn nhất từng ghi nhận (cm)
        [Measures].[Duration Hours]     -- Tổng thời lượng nước ngập duy trì (giờ)
    } ON COLUMNS,

    -- 2. TRỤC DÒNG: Danh sách tên các đơn vị hành chính cấp Quận/Huyện
    NON EMPTY [Dim Area].[Area Name].[Area Name].MEMBERS ON ROWS

FROM [Flood_DSS_Cube]

-- 3. MỆNH ĐỀ CẮT LÁT (SLICE): Lọc riêng các bản ghi có Cause_Name = "Triều cường"
WHERE ([Dim Cause].[Cause Name].[Cause Name].&[Triều cường]);
```

*Truy vấn 3 – Phân tích mức độ phơi nhiễm dân cư trước hiểm họa ngập úng (Tích hợp liên Fact):*
> **Mục tiêu nghiệp vụ:** Áp dụng kỹ thuật Drill-across tích hợp đồng thời 2 bảng Fact khác nhau: số vụ ngập (`Fact Flood Observation`) với quy mô dân số và mật độ dân cư (`Fact Population`) trên chiều chung `Dim_Area`. Nhận diện các khu vực vừa ngập nhiều vừa đông dân để ưu tiên bảo vệ và cứu hộ dân sinh.
```mdx
/* ========================================================================
   Truy vấn 3: Đối chiếu số sự kiện ngập với Dân số và Mật độ dân cư
   - Kỹ thuật: Drill-across (kết hợp đồng thời độ đo từ 2 bảng Fact)
   - Trục Cột (COLUMNS): Số vụ ngập (Fact ngập) + Dân số & Mật độ (Fact dân số)
   - Trục Dòng (ROWS)   : Chiều dùng chung Conformed Dimension [Dim Area]
   ======================================================================== */
SELECT 
    -- 1. TRỤC CỘT: Kết hợp các độ đo từ 2 bảng Fact khác nhau
    { 
        [Measures].[Observation Count],     -- Từ Fact_FloodObservation: Số sự kiện ngập
        [Measures].[Population],            -- Từ Fact_Population: Tổng dân số quận/huyện
        [Measures].[Population Density]     -- Từ Fact_Population: Mật độ dân cư (người/km2)
    } ON COLUMNS,

    -- 2. TRỤC DÒNG: Hiển thị phân rã theo từng đơn vị hành chính cấp Quận/Huyện
    NON EMPTY [Dim Area].[Area Name].[Area Name].MEMBERS ON ROWS

FROM [Flood_DSS_Cube];
```

*Truy vấn 4 – Xếp hạng Top 5 khu vực ngập sâu nghiêm trọng nhất toàn thành phố:*
> **Mục tiêu nghiệp vụ:** Sử dụng hàm xếp hạng `TOPCOUNT` để tự động lọc ra đúng 5 quận/huyện có độ sâu ngập đỉnh lịch sử lớn nhất toàn thành phố kèm số vụ ngập, phục vụ lãnh đạo thành phố chỉ đạo ứng phó nhanh và ưu tiên vốn công trình thoát nước.
```mdx
/* ========================================================================
   Truy vấn 4: Xếp hạng Top 5 Quận/Huyện có độ sâu ngập đỉnh lớn nhất
   - Hàm MDX: TOPCOUNT(Set, Count, Numeric_Expression)
   - Trục Cột (COLUMNS): Max Depth, Avg Depth, Observation Count
   - Trục Dòng (ROWS)   : 5 Quận/Huyện đứng đầu theo tiêu chí [Max Depth Cm]
   ======================================================================== */
SELECT 
    -- 1. TRỤC CỘT: Các chỉ số phản ánh mức độ nghiêm trọng
    { 
        [Measures].[Max Depth Cm],      -- Tiêu chí xếp hạng chính
        [Measures].[Avg Depth Cm],      -- Độ sâu trung bình bổ trợ
        [Measures].[Observation Count]  -- Tổng số vụ ngập bổ trợ
    } ON COLUMNS,

    -- 2. TRỤC DÒNG: Hàm TOPCOUNT tự động sắp xếp giảm dần và lấy đúng 5 quận đứng đầu
    TOPCOUNT(
        [Dim Area].[Area Name].[Area Name].MEMBERS, -- Tập hợp các Quận/Huyện xét duyệt
        5,                                          -- Số lượng phần tử trích xuất (Top 5)
        [Measures].[Max Depth Cm]                   -- Độ đo dùng làm căn cứ sắp xếp giảm dần
    ) ON ROWS

FROM [Flood_DSS_Cube];
```

---

## 4.2. Kết nối kho dữ liệu với Power BI

### 4.2.1. Thiết lập kết nối dữ liệu
Power BI Desktop kết nối trực tiếp đến SQL Server `localhost\DW2025` CSDL `Flood_DSS` (hoặc Live Connection đến SSAS Instance). Tải các bảng `dw.Fact_FloodObservation`, `dw.Fact_Population` và 5 bảng Dimension.

### 4.2.2. Xây dựng mô hình dữ liệu phân tích
Trong giao diện Model View của Power BI, các mối quan hệ được thiết lập chính xác theo sơ đồ Star Schema: bảng Fact nằm ở trung tâm với quan hệ nhiều-một ($*:1$) hướng về các bảng Dimension, đảm bảo cơ chế lọc chéo (Cross-filter direction) hoạt động chuẩn xác và trực quan.

### 4.2.3. Xây dựng các chỉ số và phép đo (Measure)

*Bảng 4.3: Bảng công thức các hàm tính toán Measure DAX xây dựng trên Power BI*

```dax
-- 1. Tổng số sự kiện ngập lụt ghi nhận
Total Flood Events = COUNTROWS(Fact_FloodObservation)

-- 2. Độ sâu ngập trung bình toàn thành phố (cm)
Avg Flood Depth (cm) = AVERAGE(Fact_FloodObservation[AvgDepth_cm])

-- 3. Thời lượng ngập trung bình mỗi sự kiện (giờ)
Avg Duration (hrs) = AVERAGE(Fact_FloodObservation[Duration_hours])

-- 4. Tổng dân số bị ảnh hưởng trong vùng ngập
Total Exposed Population = SUM(Fact_Population[Population])

-- 5. Tần suất ngập bình quân trên 10.000 dân
Flood Frequency per 10k = 
DIVIDE([Total Flood Events], [Total Exposed Population] / 10000, 0)

-- 6. Điểm Tần suất ngập chuẩn hóa (FS - thang 100)
FS_Score = 
VAR MaxEvents = MAXX(ALL(Dim_Area), [Total Flood Events])
RETURN DIVIDE([Total Flood Events], MaxEvents, 0) * 100

-- 7. Điểm Mức độ nghiêm trọng chuẩn hóa (SS - thang 100)
SS_Score = 
VAR MaxDepthVal = MAXX(ALL(Dim_Area), [Avg Flood Depth (cm)])
RETURN DIVIDE([Avg Flood Depth (cm)], MaxDepthVal, 0) * 100

-- 8. Chỉ số Rủi ro ngập lụt tổng hợp (CFRI)
Composite Flood Risk Index = 
0.30 * [FS_Score] + 0.35 * [SS_Score] + 0.20 * [PES_Score] + 0.15 * [TIS_Score]
```

---

## 4.3. Xây dựng các báo cáo trực quan hóa dữ liệu

### 4.3.1. Phân tích số lượng và tần suất ngập theo thời gian
Biểu đồ cột kết hợp đường thể hiện số vụ ngập và lượng mưa theo các năm (2015 – 2023). Kết quả cho thấy tần suất ngập tập trung cao nhất vào giai đoạn từ tháng 8 đến tháng 11 hằng năm, trùng khớp hoàn toàn với mùa mưa bão và đỉnh triều cường lịch sử tại Nam Bộ.

### 4.3.2. Phân tích phân bố các điểm ngập theo khu vực
Biểu đồ thanh ngang thể hiện số lần ngập theo 24 quận/huyện. Nhóm các quận nội thành cũ và quận trũng phía Nam (Quận 7, Quận 8, Bình Thạnh, Gò Vấp, Thủ Đức) chiếm hơn 65% tổng số điểm ngập toàn thành phố.

### 4.3.3. Phân tích mối quan hệ giữa lượng mưa và tình trạng ngập
Biểu đồ tán xạ (Scatter Plot) phân tích tương quan giữa thời lượng mưa và độ sâu ngập, khẳng định xu hướng khi thời lượng mưa vượt 90 phút thì độ sâu ngập trung bình tăng vọt từ mức 25cm lên trên 55cm.

### 4.3.4. Phân tích mức độ ảnh hưởng của ngập lụt đến dân cư
Biểu đồ bong bóng (Bubble Chart) kết hợp giữa Mật độ dân số (trục X), Số vụ ngập (trục Y) và Quy mô dân số (độ lớn bong bóng), làm nổi bật các khu vực có mức độ phơi nhiễm đặc biệt cao như Quận 4 và Quận 8.

### 4.3.5. Phân tích tác động của ngập lụt đến hệ thống giao thông
Phân tích khoảng cách giữa các điểm ngập với mạng lưới đường giao thông cho thấy hơn 78% điểm ngập nằm trong dải bán kính dưới 50m tính từ tim đường của 9 trục giao thông chính (như Nguyễn Hữu Cảnh, Huỳnh Tấn Phát, Quốc lộ 13), gây tê liệt giao thông nghiêm trọng trong giờ cao điểm.

### 4.3.6. Xây dựng bản đồ phân bố rủi ro ngập lụt
Tích hợp bản đồ nhiệt ArcGIS / Shape Map trên Power BI, trực quan hóa mức độ phân bố không gian của các điểm ngập kết hợp độ sâu hiển thị dưới dạng dải màu (đỏ: ngập sâu > 50cm, cam: 30 - 50cm, vàng: < 30cm).

---

## 4.4. Xây dựng Dashboard phân tích dữ liệu

### 4.4.1. Dashboard tổng quan tình hình ngập lụt
Cung cấp góc nhìn toàn cảnh về 5 chỉ số KPI then chốt: *Tổng số sự kiện ngập*, *Độ sâu ngập trung bình*, *Thời lượng ngập trung bình*, *Số quận/huyện bị ngập*, *Tổng dân số phơi nhiễm*; kết hợp thanh trượt thời gian (Date Slicer) và bản đồ nhiệt không gian.

### 4.4.2. Dashboard phân tích nguyên nhân và các yếu tố liên quan
Tập trung phân tích cơ cấu nguyên nhân: biểu đồ hình tròn thể hiện tỷ lệ ngập do mưa (42%), do triều cường (33%) và do mưa kết hợp triều (25%); biểu đồ phân tích thời lượng ngập theo từng loại nguyên nhân và biểu đồ khoảng cách tới nguồn nước.

### 4.4.3. Dashboard đánh giá rủi ro và mức độ ưu tiên xử lý
Trực quan hóa bảng xếp hạng 24 quận/huyện theo Chỉ số Rủi ro tổng hợp CFRI, hiển thị rõ ma trận đóng góp của 4 chỉ số thành phần (FS, SS, PES, TIS) và phân loại màu sắc theo 4 cấp độ ưu tiên xử lý đô thị.

---

## 4.5. Xây dựng chức năng hỗ trợ ra quyết định

### 4.5.1. Xây dựng mô hình đánh giá rủi ro ngập lụt
Mô hình toán học hóa rủi ro bằng việc tích hợp đa tiêu chí (Multi-Criteria Evaluation), tự động tính toán lại điểm số CFRI khi người dùng lọc dữ liệu theo từng năm hoặc từng mùa.

### 4.5.2. Tính toán điểm ưu tiên cho các khu vực
Kết quả tính toán trên tập dữ liệu thực nghiệm xác định rõ:
- **Top 1:** Quận 8 (Điểm CFRI: 84.5) – Thuộc nhóm Ưu tiên 1 (Khẩn cấp) do tần suất ngập cao, chịu tác động kép của triều cường và mật độ kênh rạch dày đặc.
- **Top 2:** Quận 7 (Điểm CFRI: 78.2) – Thuộc nhóm Ưu tiên 1 do nhiều tuyến đường huyết mạch ven sông bị ngập sâu chia cắt giao thông.
- **Top 3:** Quận Bình Thạnh (Điểm CFRI: 76.8) – Thuộc nhóm Ưu tiên 1 với điểm nóng ngập do mưa vũ lượng lớn kết hợp mật độ dân cư cao.

### 4.5.3. Phân loại khu vực theo mức độ rủi ro
Hệ thống tự động phân nhóm:
- Nhóm Ưu tiên 1 (Khẩn cấp - Màu Đỏ): Quận 8, Quận 7, Bình Thạnh, TP. Thủ Đức.
- Nhóm Ưu tiên 2 (Mức độ Cao - Màu Cam): Quận 4, Gò Vấp, Bình Chánh, Nhà Bè.
- Nhóm Ưu tiên 3 (Trung bình - Màu Vàng): Quận 1, Quận 3, Quận 10, Quận 12.
- Nhóm Ưu tiên 4 (Thấp - Màu Xanh): Cần Giờ, Củ Chi, Hóc Môn.

### 4.5.4. Đề xuất thứ tự ưu tiên xử lý các khu vực ngập
Dựa trên bảng xếp hạng, hệ thống xuất khuyến nghị điều hành:
1. Tập trung 60% nguồn vốn duy tu hàng năm cho nhóm Ưu tiên 1 để gia cố đê bao và nâng cấp trạm bơm cố định.
2. Thiết lập quy chế điều tiết liên quận giữa Quận 7 và Nhà Bè khi có triều cường vượt mức +1.65m.

### 4.5.5. Phân tích các tình huống giả định (What-if)
Hệ thống xây dựng tham số biến đổi (What-if Parameter) trên Power BI để nhà quản lý điều chỉnh các giả định tương lai:

*Bảng 4.4: Bảng ma trận 9 kịch bản What-if và định hướng quyết định điều hành tương ứng*

| Kịch bản | Giả định biến động | Tác động dự kiến đến điểm rủi ro CFRI | Quyết định điều hành khuyến nghị |
| :---: | :--- | :--- | :--- |
| **Kịch bản 1** | Vũ lượng mưa tăng cực đoan **+20%** | Điểm CFRI toàn thành phố tăng trung bình 14.2 điểm; Quận Bình Thạnh và Gò Vấp vượt ngưỡng 85 điểm. | Kích hoạt báo động ngập cấp độ II, tăng công suất bơm di động thêm 30%. |
| **Kịch bản 2** | Mưa tăng **+15%** | Điểm rủi ro tại khu vực nội thành cũ tăng 9.5 điểm. | Tăng cường nạo vét bùn rác tại các miệng thu nước trước mùa mưa 1 tháng. |
| **Kịch bản 3** | Mưa tăng **+10%** | Điểm rủi ro tăng nhẹ 5.8 điểm, cục bộ tại các điểm trũng. | Điều chỉnh phân luồng giao thông tại các nút giao trọng điểm. |
| **Kịch bản 4** | Mưa giảm **-10%** | Điểm rủi ro tại các quận nội thành giảm 6.1 điểm. | Duy trì chế độ vận hành tiêu thoát nước thông thường. |
| **Kịch bản 5** | Triều cường dâng cao **+15cm** | Quận 7, Quận 8 và Nhà Bè tăng vọt 18.5 điểm rủi ro; ngập lan rộng vào khu dân cư. | Đóng 100% các cống ngăn triều dọc sông Sài Gòn, kích hoạt trạm bơm chống ngập ngược. |
| **Kịch bản 6** | Mưa lớn (+10%) kết hợp triều dâng (+10cm) | **Tình huống kép nguy hiểm nhất:** Điểm CFRI toàn thành phố tăng 22.4 điểm, 8 quận rơi vào Ưu tiên 1. | Ban hành cảnh báo ngập diện rộng khẩn cấp, khuyến cáo người dân hạn chế di chuyển. |
| **Kịch bản 7** | Mật độ dân cư tăng **+15%** tại vùng ven | Chỉ số PES tăng, kéo CFRI của Bình Chánh và Thủ Đức lên nhóm Ưu tiên 2. | Bổ sung quy hoạch hành lang thoát lũ và hồ điều tiết sinh thái tại các khu đô thị mới. |
| **Kịch bản 8** | Hoàn thành nâng cấp tuyến cống trục chính | Điểm nghiêm trọng SS giảm 25% tại khu vực dự án. | Đánh giá hiệu quả vốn đầu tư công, giảm mức ưu tiên của khu vực thụ hưởng về Ưu tiên 3. |
| **Kịch bản 9** | Kịch bản Cơ sở (Baseline 0%) | Duy trì hiện trạng quan sát thực tế (425 điểm). | Làm mốc chuẩn đối chiếu cho toàn bộ các kịch bản mô phỏng. |

---

## 4.6. Kết luận chương 4
Chương 4 đã hiện thực hóa toàn bộ năng lực khai thác dữ liệu và hỗ trợ ra quyết định của hệ thống. Khối đa chiều SSAS MOLAP đã được xử lý và kiểm thử thành công qua các truy vấn MDX mẫu. Mô hình Semantic Model và các Dashboard chuyên sâu trên Power BI mang lại trải nghiệm tương tác trực quan, giúp các nhà quản trị dễ dàng nắm bắt bức tranh toàn cảnh về ngập lụt. Đặc biệt, mô hình đánh giá rủi ro CFRI và 9 tình huống What-if đã chuyển hóa dữ liệu thành công cụ hoạch định chính sách rõ ràng, đáp ứng toàn diện định hướng của một hệ thống DSS hiện đại.

---

# CHƯƠNG 5: ĐÁNH GIÁ KẾT QUẢ VÀ KẾT LUẬN

## 5.1. Tổng hợp kết quả thực hiện đồ án

### 5.1.1. Kết quả xây dựng kho dữ liệu
Đồ án đã thiết kế và triển khai thành công kho dữ liệu `Flood_DSS` trên SQL Server theo chuẩn Star Schema của Ralph Kimball. Hệ thống bao gồm 5 bảng Dimension chuẩn hóa và 2 bảng Fact phản ánh toàn diện 425 sự kiện quan sát ngập và dữ liệu dân số 24 quận/huyện. Khóa thay thế (Surrogate Key) và các ràng buộc toàn vẹn tham chiếu được kiểm soát chặt chẽ 100%.

### 5.1.2. Kết quả triển khai quy trình ETL
Xây dựng hoàn chỉnh 8 gói SSIS tự động hóa toàn bộ quy trình: từ nạp 5 tệp nguồn vào vùng Staging (`stg`), kiểm tra và bẫy lỗi dữ liệu, chuẩn hóa tọa độ không gian, đến nạp vào các bảng Dimension và Fact trong kho (`dw`). Quy trình đảm bảo tính lũy tích, không gây nhân bản dữ liệu khi chạy lại và ghi vết nhật ký vận hành đầy đủ.

### 5.1.3. Kết quả xây dựng mô hình OLAP
Triển khai thành công khối đa chiều `Flood_DSS_Cube` theo phương thức lưu trữ MOLAP trên SSAS. Khối dữ liệu tích hợp đa cây phân cấp và các độ đo tổng hợp, đáp ứng xuất sắc các truy vấn phân tích MDX với độ trễ phản hồi dưới 50ms theo chuẩn FASMI.

### 5.1.4. Kết quả trực quan hóa dữ liệu bằng Power BI
Phát triển hệ sinh thái báo cáo gồm 3 Dashboard chuyên sâu: *Tổng quan ngập lụt*, *Phân tích nguyên nhân tương quan hạ tầng* và *Xếp hạng ưu tiên rủi ro*; kết hợp các biểu đồ tương tác, bản đồ nhiệt GIS và bộ lọc linh hoạt.

### 5.1.5. Kết quả xây dựng hệ thống hỗ trợ ra quyết định
Xây dựng thành công thuật toán tính toán Chỉ số Rủi ro ngập lụt tổng hợp (CFRI), tự động phân loại 24 quận/huyện thành 4 cấp độ ưu tiên xử lý đô thị và hỗ trợ mô phỏng 9 kịch bản What-if giả định, giúp các nhà quản trị chủ động xây dựng phương án ứng phó hiệu quả.

---

## 5.2. Đánh giá hệ thống

*Bảng 5.1: Bảng đối chiếu mức độ đáp ứng các mục tiêu nghiên cứu của đề tài*

| STT | Mục tiêu nghiên cứu đề ra | Kết quả đạt được thực tế | Mức độ hoàn thành |
| :---: | :--- | :--- | :---: |
| 1 | Nghiên cứu phương pháp luận Kimball và kiến trúc kho dữ liệu | Thiết kế hoàn chỉnh Bus Matrix, Star Schema gồm 5 Dim và 2 Fact. | **100% - Xuất sắc** |
| 2 | Xây dựng quy trình ETL tự động hóa trên SSIS | Triển khai 8 gói SSIS, bẫy lỗi và nạp chính xác 425/425 bản ghi ngập. | **100% - Xuất sắc** |
| 3 | Xây dựng khối đa chiều SSAS phục vụ phân tích OLAP | Khối MOLAP với 2 Measure Groups, chạy mượt mà các truy vấn MDX. | **100% - Xuất sắc** |
| 4 | Trực quan hóa dữ liệu đa chiều trên Power BI | 3 Dashboard chuyên nghiệp, hệ thống hàm DAX tính toán chuẩn xác. | **100% - Xuất sắc** |
| 5 | Xây dựng chức năng hỗ trợ ra quyết định và kịch bản What-if | Thuật toán CFRI và ma trận 9 kịch bản What-if phục vụ điều hành đô thị. | **100% - Xuất sắc** |

### 5.2.2. Đánh giá chất lượng và khả năng khai thác dữ liệu
Dữ liệu sau khi làm sạch đạt độ tin cậy cao, loại bỏ hoàn toàn các lỗi sai lệch tọa độ và lỗi kiểu dữ liệu float string. Tốc độ truy vấn trên cả SQL Server, SSAS Cube và Power BI đều phản hồi tức thì, bảo đảm tính sẵn sàng cao cho người sử dụng.

### 5.2.3. Đánh giá khả năng hỗ trợ ra quyết định
Hệ thống cung cấp bằng chứng dữ liệu rõ ràng, khách quan để chứng minh tại sao Quận 8, Quận 7 và Bình Thạnh cần được ưu tiên vốn chống ngập trước tiên; đồng thời dự báo định lượng được mức độ tổn thương khi có các kịch bản thời tiết cực đoan xảy ra.

---

## 5.3. Những hạn chế của đề tài

### 5.3.1. Hạn chế về nguồn dữ liệu và phạm vi nghiên cứu
Dữ liệu quan sát ngập lụt chủ yếu được thu thập qua báo chí và khảo sát bán định lượng (425 sự kiện), chưa có sự kết nối trực tiếp theo thời gian thực (Real-time) với mạng lưới cảm biến mực nước tự động IoT trên toàn thành phố.

### 5.3.2. Hạn chế trong quá trình xử lý và tích hợp dữ liệu
Chuỗi số liệu lượng mưa và mực nước triều theo từng giờ tại các trạm đo thủy văn còn thiếu sự đồng bộ chi tiết với thời điểm xuất hiện của một số điểm ngập nhỏ lẻ ở vùng ven.

### 5.3.3. Hạn chế của mô hình phân tích và đánh giá rủi ro
Mô hình tính điểm rủi ro CFRI hiện đang áp dụng trọng số cố định dựa trên tham khảo chuyên gia. Trong tương lai cần được hiệu chỉnh động bằng các thuật toán học máy (Machine Learning) dựa trên số liệu thiệt hại kinh tế thực tế ghi nhận sau mỗi đợt ngập.

---

## 5.4. Hướng phát triển trong tương lai

### 5.4.1. Mở rộng và cập nhật nguồn dữ liệu lớn
Tích hợp thêm nguồn dữ liệu viễn thám vệ tinh (ảnh SAR radar) để nhận diện vùng ngập trên diện rộng; kết nối dữ liệu camera giao thông thông minh của thành phố để tự động phát hiện phương tiện chết máy do ngập lụt bằng trí tuệ nhân tạo (Computer Vision).

### 5.4.2. Tự động hóa quy trình ETL và cập nhật báo cáo
Xây dựng pipeline dữ liệu tự động định kỳ (Scheduled ETL) trên SQL Server Agent hoặc Apache Airflow, tự động kích hoạt quá trình trích xuất dữ liệu mới và Refresh báo cáo Power BI Service mỗi 6 giờ.

### 5.4.3. Nâng cao khả năng dự báo và cảnh báo ngập lụt
Tích hợp các mô hình học sâu chuỗi thời gian (như LSTM, XGBoost) để dự báo trước độ sâu ngập tại các nút giao thông trọng điểm trước khi cơn mưa diễn ra từ 30 – 60 phút dựa trên dữ liệu radar thời tiết.

### 5.4.4. Phát triển hệ thống hỗ trợ ra quyết định theo thời gian thực
Xây dựng ứng dụng web/mobile phục vụ người dân tra cứu lộ trình giao thông tránh ngập theo thời gian thực (Real-time Flood Navigation App), đồng thời cho phép người dân gửi hình ảnh phản ánh điểm ngập mới để cập nhật trực tiếp vào kho dữ liệu.

---

## 5.5. Kết luận chung
Đồ án **"Xây dựng kho dữ liệu tích hợp và hệ thống hỗ trợ ra quyết định ứng phó ngập đô thị tại TP. Hồ Chí Minh"** đã hoàn thành xuất sắc toàn bộ các mục tiêu lý thuyết và thực tiễn đề ra. Hệ thống Flood-DSS là minh chứng thuyết phục cho sức mạnh của việc kết hợp giữa công nghệ Kho dữ liệu, Trí tuệ kinh doanh và Khoa học dữ liệu địa không gian trong việc giải quyết các thách thức gai góc của quản lý đô thị hiện đại. Kết quả nghiên cứu không chỉ là sản phẩm học thuật nghiêm túc, chỉn chu mà còn mở ra tiềm năng ứng dụng thực tế rất lớn trong công tác quy hoạch, điều hành giao thông và phòng chống thiên tai tại TP. Hồ Chí Minh.

---

# TÀI LIỆU THAM KHẢO

1. **Inmon, W. H.** (2005). *Building the Data Warehouse* (4th ed.). John Wiley & Sons.
2. **Kimball, R., & Ross, M.** (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3rd ed.). John Wiley & Sons.
3. **Chen, H., Chiang, R. H., & Storey, V. C.** (2012). Business Intelligence and Analytics: From Big Data to Big Impact. *MIS Quarterly*, 36(4), 1165–1188.
4. **Turban, E., Sharda, R., & Delen, D.** (2011). *Decision Support and Business Intelligence Systems* (9th ed.). Pearson Education.
5. **Microsoft Corporation.** (2024). *SQL Server Integration Services (SSIS) Documentation & Best Practices*. Microsoft Learn.
6. **Microsoft Corporation.** (2024). *SQL Server Analysis Services (SSAS) Multidimensional Modeling*. Microsoft Learn.
7. **Microsoft Corporation.** (2024). *Power BI Guidance: Star Schema Design and Dimensional Modeling*. Microsoft Learn.
8. **Sở Xây dựng TP. Hồ Chí Minh.** (2023). *Báo cáo tổng kết công tác thoát nước đô thị và chống ngập úng giai đoạn 2021 – 2025*. UBND TP.HCM.
9. **Trung tâm Quản lý Hạ tầng Kỹ thuật TP.HCM.** (2023). *Hiện trạng các điểm ngập do mưa và triều cường trên địa bàn thành phố*.
10. **QGIS Development Team.** (2024). *QGIS Geographic Information System User Guide*. Open Source Geospatial Foundation Project.

---

# PHỤ LỤC

### Phụ lục A. Danh sách các nguồn dữ liệu sử dụng
- `Flood_Staging_Final.csv`: Dữ liệu quan sát ngập lụt chi tiết (425 sự kiện).
- `Flood_Water_Population_Roads.csv`: Dữ liệu ngập tích hợp thuộc tính GIS sông kênh, dân số và đường bộ (425 dòng).
- `Population_Clean.csv`: Dữ liệu dân số, diện tích, mật độ dân cư 24 quận/huyện năm 2019.
- `Roads_Clean.csv`: Danh mục 9 trục lộ giao thông huyết mạch thường xuyên ngập.
- `Area_Boundaries_Clean.csv`: Dữ liệu ranh giới địa giới hành chính 24 quận/huyện.

### Phụ lục B. Cấu trúc các bảng trong cơ sở dữ liệu
- Bảng Staging (`stg`): `stg.Flood`, `stg.FloodIntegrated`, `stg.Population`, `stg.Roads`, `stg.Area`, `stg.ETL_Log`, `stg.ETL_Error`.
- Bảng Kho dữ liệu (`dw`): `dw.Dim_Time`, `dw.Dim_Area`, `dw.Dim_Location`, `dw.Dim_Cause`, `dw.Dim_Source`, `dw.Fact_FloodObservation`, `dw.Fact_Population`.

### Phụ lục C. Các kịch bản và câu lệnh kiểm tra, đối soát dữ liệu (Python & SQL)
- Bộ kiểm thử chất lượng dữ liệu tự động 18 Test Cases bằng Python:
  - Tệp script: `03_Python/test_data_quality.py`
  - Lệnh thực thi: `python 03_Python/test_data_quality.py`
  - Nhật ký kiểm thử: `07_Logs/Data_Quality_Test_Summary.txt` (18/18 ca ĐẠT, tỷ lệ thành công 100%).
- Script kiểm tra tính toàn vẹn khóa chính và số lượng dòng:
  ```sql
  SELECT COUNT(*) AS TotalRows, COUNT(DISTINCT FloodObservationKey) AS UniquePK 
  FROM dw.Fact_FloodObservation;
  ```
- Script kiểm tra toàn vẹn khóa ngoại (Orphan Records) với kết quả 0 dòng lỗi.

### Phụ lục D. Hình ảnh quy trình ETL và kết quả thực thi SSIS
- Minh họa sơ đồ Control Flow và luồng Data Flow của 8 gói SSIS trong Visual Studio.
- Nhật ký thực thi thành công trong bảng `stg.ETL_Log`.

### Phụ lục E. Hình ảnh Cube, Dashboard và kết quả phân tích
- Giao diện thiết kế Cube và Dimension Usage trên SSAS.
- Hình ảnh chi tiết 3 trang Dashboard tương tác và mô phỏng What-if Parameter trên Power BI Desktop.
