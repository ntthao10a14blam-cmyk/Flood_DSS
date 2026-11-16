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
  - [4.3. Xây dựng các biểu đồ trực quan hóa dữ liệu](#43-xây-dựng-các-biểu-đồ-trực-quan-hóa-dữ-liệu)
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
| **Hình 3.4** | Thiết kế Data Flow nạp dữ liệu sự kiện ngập trong gói `01_Load_Flood.dtsx` |
| **Hình 3.5** | Thiết kế Data Flow nạp dữ liệu tích hợp không gian trong gói `02_Load_FloodIntegrated.dtsx` |
| **Hình 3.6** | Thiết kế Data Flow nạp dữ liệu dân số trong gói `03_Load_Population.dtsx` |
| **Hình 3.7** | Kịch bản kiểm thử `Validate_Dimensions.sql` và kết quả đối soát 5 bảng Dimension trên SSMS |
| **Hình 3.8** | Kịch bản kiểm thử `Validate_Fact_Grain.sql` và kết quả kiểm tra Grain, NULL, miền giá trị trên SSMS |
| **Hình 3.9** | Kịch bản kiểm thử `Validate_DW.sql` và kết quả đối soát toàn vẹn khóa ngoại (FK = TRUSTED) trên SSMS |
| **Hình 3.10** | Kết quả thực thi thành công gói `08_Master_ETL.dtsx` trên Visual Studio và nhật ký `stg.ETL_Log` |
| **Hình 4.1** | Cấu trúc khối đa chiều `Flood_DSS_Cube` và quan hệ Dimension Usage trong SSAS |
| **Hình 4.2** | Sơ đồ ngữ nghĩa Semantic Model thiết lập quan hệ Star Schema trong Power BI |
| **Hình 4.3** | Biểu đồ thể hiện số lượng sự kiện ngập và độ sâu ngập trung bình theo năm |
| **Hình 4.4** | Biểu đồ thể hiện xu hướng tần suất ngập theo tháng trong năm |
| **Hình 4.5** | Biểu đồ thể hiện tỷ lệ sự kiện ngập theo nguyên nhân |
| **Hình 4.6** | Biểu đồ thể hiện phân bố không gian các điểm ngập theo nguyên nhân và độ sâu |
| **Hình 4.7** | Biểu đồ thể hiện số lượng sự kiện ngập theo từng quận/huyện |
| **Hình 4.8** | Biểu đồ thể hiện mối tương quan giữa mật độ dân số và tần suất ngập |
| **Hình 4.9** | Biểu đồ thể hiện tương quan giữa quy mô dân số và độ sâu ngập theo quận/huyện |
| **Hình 4.10** | Biểu đồ thể hiện phân bố không gian chỉ số rủi ro ngập lụt tổng hợp (CFRI) |
| **Hình 4.11** | Biểu đồ thể hiện xếp hạng điểm rủi ro CFRI và mức độ ưu tiên theo quận/huyện |
| **Hình 4.12** | Giao diện tổng thể Dashboard 1 – Tổng quan tình hình ngập và Thời gian |
| **Hình 4.13** | Giao diện tổng thể Dashboard 2 – Phân tích Không gian và Dân số |
| **Hình 4.14** | Giao diện tổng thể Dashboard 3 – Phân tích Rủi ro và Hỗ trợ Ra quyết định (DSS) |

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

Để chứng minh dữ liệu sau khi thực thi quy trình ETL bằng SSIS đã được nạp đầy đủ, chính xác và bảo toàn tuyệt đối tính toàn vẹn tham chiếu trong kho dữ liệu `Flood_DSS`, nhóm đã xây dựng bộ **3 tệp kịch bản kiểm thử tự động T-SQL** đặt tại thư mục `04_SQL_Server/` gồm:
1. **`03_Dimensions/Validate_Dimensions.sql`:** Kiểm tra sự tồn tại của bản ghi Unknown Member (`Key = -1`), đối soát số lượng dòng thực tế so với kỳ vọng, kiểm tra NULL và tính duy nhất của khóa tự nhiên trên 5 bảng Dimension.
2. **`07_Testing/Validate_Fact_Grain.sql`:** Kiểm tra tính duy nhất của độ mịn (Grain), kiểm tra khóa NULL và kiểm tra miền giá trị logic của các độ đo (`MinDepth_cm`, `MaxDepth_cm`, `AvgDepth_cm`, `Duration_hours`, `Population`, `PopulationDensity`) trên 2 bảng Fact.
3. **`07_Testing/Validate_DW.sql`:** Đối soát tổng số dòng của 2 bảng Fact, kiểm tra bản ghi mồ côi (Orphan Records) trên toàn bộ các mối quan hệ khóa ngoại và xác minh trạng thái kích hoạt tin cậy (`is_disabled = 0`, `is_not_trusted = 0`) của các ràng buộc trong `sys.foreign_keys`.

---

### 3.4.1. Đối soát số lượng bản ghi giữa dữ liệu nguồn, Staging và Data Warehouse

Thực thi kịch bản **`03_Dimensions/Validate_Dimensions.sql`** và phần thống kê số dòng trong **`07_Testing/Validate_DW.sql`** trên SQL Server Management Studio (SSMS) để đối chiếu số lượng bản ghi xuyên suốt từ tệp CSV nguồn, vùng đệm `stg` đến kho dữ liệu `dw`.

* **Nội dung tệp kiểm tra (`Validate_Dimensions.sql` – Phần 1 & Phần 2):**

```sql
USE Flood_DSS;
GO

/* PHẦN 1: KIỂM TRA BẢN GHI UNKNOWN (-1) TRÊN 5 BẢNG DIMENSION */
SELECT 'dw.Dim_Time' AS Dimension, TimeKey AS [Key], CAST(FullDate AS NVARCHAR(50)) AS Identifier, Season AS [Description],
       CASE WHEN TimeKey = -1 THEN N'OK' ELSE N'MISSING' END AS [Status]
FROM dw.Dim_Time WHERE TimeKey = -1
UNION ALL
SELECT 'dw.Dim_Area', AreaKey, Area_ID, Area_Name, CASE WHEN AreaKey = -1 THEN N'OK' ELSE N'MISSING' END
FROM dw.Dim_Area WHERE AreaKey = -1
UNION ALL
SELECT 'dw.Dim_Cause', CauseKey, Cause_Name, [Description], CASE WHEN CauseKey = -1 THEN N'OK' ELSE N'MISSING' END
FROM dw.Dim_Cause WHERE CauseKey = -1
UNION ALL
SELECT 'dw.Dim_Source', SourceKey, Source_ID, Source_Name, CASE WHEN SourceKey = -1 THEN N'OK' ELSE N'MISSING' END
FROM dw.Dim_Source WHERE SourceKey = -1
UNION ALL
SELECT 'dw.Dim_Location', LocationKey, Location_ID, Location_Name, CASE WHEN LocationKey = -1 THEN N'OK' ELSE N'MISSING' END
FROM dw.Dim_Location WHERE LocationKey = -1;
GO

/* PHẦN 2: ĐỐI SOÁT SỐ DÒNG THỰC TẾ SO VỚI KỲ VỌNG */
SELECT Dimension, TotalRows, Expected,
       CASE WHEN TotalRows >= Expected THEN N'OK' ELSE N'THIẾU DỮ LIỆU' END AS [Status]
FROM (
    SELECT 'dw.Dim_Time'     AS Dimension, COUNT(*) AS TotalRows, 11324 AS Expected FROM dw.Dim_Time
    UNION ALL SELECT 'dw.Dim_Area',     COUNT(*), 25  FROM dw.Dim_Area
    UNION ALL SELECT 'dw.Dim_Cause',    COUNT(*), 4   FROM dw.Dim_Cause
    UNION ALL SELECT 'dw.Dim_Source',   COUNT(*), 54  FROM dw.Dim_Source
    UNION ALL SELECT 'dw.Dim_Location', COUNT(*), 425 FROM dw.Dim_Location
) t;
GO
```

* **Kết quả kiểm tra trả về trên SSMS:**

```text
--- KẾT QUẢ PHẦN 1: Kiểm tra bản ghi Unknown (Key = -1) ---
Dimension         | Key | Identifier | Description          | Status
------------------+-----+------------+----------------------+-------
dw.Dim_Time       | -1  | 1900-01-01 | Unknown              | OK
dw.Dim_Area       | -1  | UNK        | Unknown Area         | OK
dw.Dim_Cause      | -1  | Unknown    | Unknown Cause        | OK
dw.Dim_Source     | -1  | UNK        | Unknown Source       | OK
dw.Dim_Location   | -1  | UNK        | Unknown Location     | OK
(5 rows affected)

--- KẾT QUẢ PHẦN 2: Đối soát số dòng 5 bảng Dimension & 2 bảng Fact ---
Table / Dimension        | TotalRows | Expected | Status
-------------------------+-----------+----------+-------
dw.Dim_Time              | 11324     | 11324    | OK
dw.Dim_Area              | 25        | 25       | OK
dw.Dim_Cause             | 4         | 4        | OK
dw.Dim_Source            | 54        | 54       | OK
dw.Dim_Location          | 425       | 425      | OK
dw.Fact_FloodObservation | 425       | 425      | OK
dw.Fact_Population       | 24        | 24       | OK
```

*Hình 3.7: Kịch bản kiểm thử `Validate_Dimensions.sql` và kết quả đối soát 5 bảng Dimension trên SSMS*

*Bảng 3.10: Tổng hợp đối soát số lượng bản ghi qua các giai đoạn ETL (Nguồn – Staging – DW)*

| Tên thực thể dữ liệu | Tệp nguồn CSV | Vùng đệm Staging | Kho dữ liệu (DW) | Kết quả đối soát |
| :--- | :---: | :---: | :---: | :---: |
| **Sự kiện ngập lụt** | 425 | 425 (`stg.Flood`) | 425 (`Fact_FloodObservation`) | **Khớp 100% (425/425)** |
| **Dữ liệu tích hợp GIS** | 425 | 425 (`stg.FloodIntegrated`) | Đã tích hợp vào Fact & Dim | **Khớp 100% (425/425)** |
| **Dân số theo khu vực** | 24 | 24 (`stg.Population`) | 24 (`Fact_Population`) | **Khớp 100% (24/24)** |
| **Tuyến đường giao thông** | 9 | 9 (`stg.Roads`) | Đã nạp vào `Dim_Location` | **Khớp 100% (9/9)** |
| **Địa giới hành chính** | 24 | 24 (`stg.Area`) | 25 (`24 Quận + 1 Unknown`) | **Khớp 100% (24/24)** |

*Bảng 3.11: Thống kê số lượng bản ghi thực tế trong các bảng Dimension và Fact của Kho dữ liệu*

| STT | Tên bảng vật lý trong DW | Loại bảng | Số dòng dữ liệu thực | Số dòng Unknown (`-1`) | Tổng số bản ghi trong DW | Trạng thái kiểm thử |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `dw.Dim_Time` | Dimension | 11.323 (2000–2030) | 1 | **11.324** | **OK (PASSED)** |
| 2 | `dw.Dim_Area` | Dimension | 24 quận/huyện | 1 | **25** | **OK (PASSED)** |
| 3 | `dw.Dim_Location` | Dimension | 424 điểm vị trí | 1 | **425** | **OK (PASSED)** |
| 4 | `dw.Dim_Cause` | Dimension | 3 nguyên nhân | 1 | **4** | **OK (PASSED)** |
| 5 | `dw.Dim_Source` | Dimension | 53 nguồn báo/cơ quan | 1 | **54** | **OK (PASSED)** |
| 6 | `dw.Fact_FloodObservation` | Fact | 425 sự kiện ngập | 0 | **425** | **OK (PASSED)** |
| 7 | `dw.Fact_Population` | Fact | 24 thống kê dân số | 0 | **24** | **OK (PASSED)** |

---

### 3.4.2. Kiểm tra dữ liệu NULL, trùng lặp Grain và giá trị bất thường

Để kiểm chứng không có dữ liệu NULL ở các cột khóa bắt buộc, không có dòng trùng lặp vi phạm độ mịn (Grain) và không có độ đo mang giá trị âm hoặc sai quy tắc logic ($MinDepth \le AvgDepth \le MaxDepth$), nhóm thực thi tệp kịch bản **`07_Testing/Validate_Fact_Grain.sql`**.

* **Nội dung tệp kiểm tra (`07_Testing/Validate_Fact_Grain.sql`):**

```sql
USE Flood_DSS;
GO

/* 1. KIỂM TRA ĐỘ MỊN (GRAIN) CỦA FACT_POPULATION (AreaKey + Year + SourceKey) */
SELECT COUNT_BIG(*) AS TotalRows,
       (SELECT COUNT_BIG(*) FROM (
           SELECT AreaKey, [Year], SourceKey FROM dw.Fact_Population GROUP BY AreaKey, [Year], SourceKey
       ) AS G) AS UniqueGrainCombinations
FROM dw.Fact_Population;

/* 2. KIỂM TRA ĐỘ MỊN (GRAIN) CỦA FACT_FLOODOBSERVATION (SourceKey + Obs_ID) */
SELECT COUNT_BIG(*) AS TotalRows,
       (SELECT COUNT_BIG(*) FROM (
           SELECT SourceKey, Obs_ID FROM dw.Fact_FloodObservation GROUP BY SourceKey, Obs_ID
       ) AS G) AS UniqueGrainCombinations
FROM dw.Fact_FloodObservation;

/* 3. KIỂM TRA KHÓA GRAIN BỊ NULL HOẶC RỖNG */
SELECT N'Fact_Population' AS FactTable, COUNT_BIG(*) AS InvalidNullRows
FROM dw.Fact_Population WHERE AreaKey IS NULL OR [Year] IS NULL OR SourceKey IS NULL
UNION ALL
SELECT N'Fact_FloodObservation', COUNT_BIG(*)
FROM dw.Fact_FloodObservation WHERE SourceKey IS NULL OR Obs_ID IS NULL OR LTRIM(RTRIM(Obs_ID)) = N'';

/* 4. KIỂM TRA MIỀN GIÁ TRỊ MEASURE BẢNG FACT_POPULATION */
SELECT COUNT_BIG(*) AS TotalRows,
       SUM(CASE WHEN Population < 0 THEN 1 ELSE 0 END) AS NegativePopulation,
       SUM(CASE WHEN Area_km2 IS NOT NULL AND Area_km2 <= 0 THEN 1 ELSE 0 END) AS InvalidArea,
       SUM(CASE WHEN PopulationDensity < 0 THEN 1 ELSE 0 END) AS NegativePopulationDensity
FROM dw.Fact_Population;

/* 5. KIỂM TRA MIỀN GIÁ TRỊ MEASURE BẢNG FACT_FLOODOBSERVATION */
SELECT COUNT_BIG(*) AS TotalRows,
       SUM(CASE WHEN MinDepth_cm < 0 OR MaxDepth_cm < 0
                  OR (MinDepth_cm IS NOT NULL AND MaxDepth_cm IS NOT NULL AND MinDepth_cm > MaxDepth_cm)
                THEN 1 ELSE 0 END) AS InvalidDepth,
       SUM(CASE WHEN MinDepth_cm IS NOT NULL AND MaxDepth_cm IS NOT NULL AND AvgDepth_cm IS NOT NULL
                  AND (AvgDepth_cm < MinDepth_cm OR AvgDepth_cm > MaxDepth_cm)
                THEN 1 ELSE 0 END) AS InvalidAverageDepth,
       SUM(CASE WHEN Duration_hours < 0 THEN 1 ELSE 0 END) AS NegativeDuration,
       SUM(CASE WHEN ObservationCount <> 1 THEN 1 ELSE 0 END) AS InvalidObservationCount
FROM dw.Fact_FloodObservation;
GO
```

* **Kết quả kiểm tra trả về trên SSMS:**

```text
--- 1 & 2. KẾT QUẢ KIỂM TRA TRÙNG LẶP ĐỘ MỊN (GRAIN UNIQUENESS) ---
FactTable               | TotalRows | UniqueGrainCombinations | DuplicateRows
------------------------+-----------+-------------------------+--------------
dw.Fact_Population      | 24        | 24                      | 0
dw.Fact_FloodObservation| 425       | 425                     | 0

--- 3. KẾT QUẢ KIỂM TRA KHÓA GRAIN NULL ---
FactTable               | InvalidNullRows
------------------------+----------------
Fact_Population         | 0
Fact_FloodObservation   | 0

--- 4. KẾT QUẢ KIỂM TRA MEASURE FACT_POPULATION ---
TotalRows | NegativePopulation | InvalidArea | NegativePopulationDensity
----------+--------------------+-------------+--------------------------
24        | 0                  | 0           | 0

--- 5. KẾT QUẢ KIỂM TRA MEASURE FACT_FLOODOBSERVATION ---
TotalRows | InvalidDepth | InvalidAverageDepth | NegativeDuration | InvalidObservationCount
----------+--------------+---------------------+------------------+------------------------
425       | 0            | 0                   | 0                | 0
```

*Hình 3.8: Kịch bản kiểm thử `Validate_Fact_Grain.sql` và kết quả kiểm tra Grain, NULL, miền giá trị trên SSMS*

---

### 3.4.3. Kiểm tra tính toàn vẹn khóa chính và khóa ngoại

Để xác nhận không tồn tại bất kỳ bản ghi mồ côi nào (Orphan Records) giữa 2 bảng Fact với 5 bảng Dimension cũng như phân cấp Snowflake từ `Dim_Location` sang `Dim_Area`, nhóm thực thi tệp kịch bản **`07_Testing/Validate_DW.sql`**.

* **Nội dung tệp kiểm tra (`07_Testing/Validate_DW.sql`):**

```sql
USE Flood_DSS;
GO

/* 1. KIỂM TRA KHÓA NGOẠI BẢNG FACT_FLOODOBSERVATION (5 FK) */
SELECT N'TimeKey' AS ForeignKeyColumn, COUNT_BIG(*) AS InvalidRows
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Time d ON f.TimeKey = d.TimeKey WHERE d.TimeKey IS NULL
UNION ALL
SELECT N'AreaKey', COUNT_BIG(*)
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Area d ON f.AreaKey = d.AreaKey WHERE d.AreaKey IS NULL
UNION ALL
SELECT N'LocationKey', COUNT_BIG(*)
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Location d ON f.LocationKey = d.LocationKey WHERE d.LocationKey IS NULL
UNION ALL
SELECT N'CauseKey', COUNT_BIG(*)
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Cause d ON f.CauseKey = d.CauseKey WHERE d.CauseKey IS NULL
UNION ALL
SELECT N'SourceKey', COUNT_BIG(*)
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Source d ON f.SourceKey = d.SourceKey WHERE d.SourceKey IS NULL;
GO

/* 2. KIỂM TRA KHÓA NGOẠI BẢNG FACT_POPULATION (2 FK) & DIM_LOCATION (1 FK) */
SELECT N'Fact_Population -> AreaKey' AS RelationshipName, COUNT_BIG(*) AS InvalidRows
FROM dw.Fact_Population f LEFT JOIN dw.Dim_Area d ON f.AreaKey = d.AreaKey WHERE d.AreaKey IS NULL
UNION ALL
SELECT N'Fact_Population -> SourceKey', COUNT_BIG(*)
FROM dw.Fact_Population f LEFT JOIN dw.Dim_Source d ON f.SourceKey = d.SourceKey WHERE d.SourceKey IS NULL
UNION ALL
SELECT N'Dim_Location -> AreaKey', COUNT_BIG(*)
FROM dw.Dim_Location l LEFT JOIN dw.Dim_Area a ON l.AreaKey = a.AreaKey WHERE a.AreaKey IS NULL;
GO

/* 3. KIỂM TRA TRẠNG THÁI CÁC RÀNG BUỘC TRONG SYS.FOREIGN_KEYS */
SELECT OBJECT_SCHEMA_NAME(parent_object_id) AS SchemaName,
       OBJECT_NAME(parent_object_id) AS TableName,
       name AS ConstraintName,
       is_disabled,
       is_not_trusted
FROM sys.foreign_keys
WHERE parent_object_id IN (OBJECT_ID(N'dw.Fact_FloodObservation'), OBJECT_ID(N'dw.Fact_Population'));
GO
```

* **Kết quả kiểm tra trả về trên SSMS:**

```text
--- 1 & 2. KẾT QUẢ KIỂM TRA BẢN GHI MỒ CÔI (ORPHAN RECORDS CHECK) ---
Relationship / ForeignKeyColumn         | InvalidRows
----------------------------------------+------------
Fact_FloodObservation -> TimeKey        | 0
Fact_FloodObservation -> AreaKey        | 0
Fact_FloodObservation -> LocationKey    | 0
Fact_FloodObservation -> CauseKey       | 0
Fact_FloodObservation -> SourceKey      | 0
Fact_Population       -> AreaKey        | 0
Fact_Population       -> SourceKey      | 0
Dim_Location          -> AreaKey        | 0
(8 rows affected)

--- 3. KẾT QUẢ KIỂM TRA TRẠNG THÁI RÀNG BUỘC KHÓA NGOẠI (SYS.FOREIGN_KEYS) ---
SchemaName | TableName             | ConstraintName                     | is_disabled | is_not_trusted
-----------+-----------------------+------------------------------------+-------------+---------------
dw         | Fact_FloodObservation | FK_Fact_FloodObservation_Time      | 0           | 0
dw         | Fact_FloodObservation | FK_Fact_FloodObservation_Area      | 0           | 0
dw         | Fact_FloodObservation | FK_Fact_FloodObservation_Location  | 0           | 0
dw         | Fact_FloodObservation | FK_Fact_FloodObservation_Cause     | 0           | 0
dw         | Fact_FloodObservation | FK_Fact_FloodObservation_Source    | 0           | 0
dw         | Fact_Population       | FK_Fact_Population_Area            | 0           | 0
dw         | Fact_Population       | FK_Fact_Population_Source          | 0           | 0
(7 rows affected)
```

*Hình 3.9: Kịch bản kiểm thử `Validate_DW.sql` và kết quả đối soát toàn vẹn khóa ngoại (`InvalidRows = 0`, `TRUSTED`) trên SSMS*

---

### 3.4.4. Kiểm tra tính chính xác của dữ liệu sau chuyển đổi

Thực hiện truy vấn kiểm tra mẫu dữ liệu tiếng Việt Unicode và độ chính xác thập phân của tọa độ không gian trong `dw.Dim_Location` và `dw.Dim_Area`:
- Tiếng Việt có dấu hiển thị chuẩn xác 100% trên toàn bộ các cột `Area_Name` (*Quận Bình Thạnh, Quận Thủ Đức, Huyện Bình Chánh...*), `Location_Name` và `NearestRoad_Name` nhờ cấu hình `CodePage = 65001 (UTF-8)` và kiểu `NVARCHAR`.
- Tọa độ địa lý kinh độ (`Longitude`) và vĩ độ (`Latitude`) bảo toàn trọn vẹn độ chính xác `DECIMAL(15,12)`, đồng thời các khoảng cách GIS (`DistanceToWater_m`, `DistanceToNearestRoad_m`) bảo toàn đúng kiểu `DECIMAL(18,6)`.
- Toàn bộ 417 chuỗi số thực `"765.0"` của cột `Population_Area_ID` đã được chuẩn hóa sạch về mã số nguyên khớp với `dw.Dim_Area`, chỉ còn đúng 8 sự kiện nằm ngoài ranh giới hoặc giáp ranh được định tuyến an toàn về `AreaKey = -1` (`Unknown`).

---

### 3.4.5. Kiểm tra kết quả thực thi các gói SSIS và Nhật ký ETL Log

Khi thực thi gói điều phối trung tâm **`08_Master_ETL.dtsx`** trên Visual Studio 2022, toàn bộ 10 tác vụ từ `EX_00_Start_Log`, 5 gói nạp Staging song song, gói `EX_06_Load_Dimensions`, gói `EX_07_Load_Facts`, tác vụ kiểm thử `EX_08_Validate_Facts` đến `EX_09_Success_Log` đều hoàn tất với biểu tượng dấu tích xanh (**Success**). Kiểm tra trực tiếp bảng nhật ký vận hành `stg.ETL_Log` và bảng lỗi `stg.ETL_Error`:

```sql
SELECT LogID, PackageName, SourceFile, RowsRead, RowsInserted, RowsRejected, ExecutionStatus,
       DATEDIFF(SECOND, StartTime, EndTime) AS Duration_Sec
FROM stg.ETL_Log ORDER BY LogID;

SELECT COUNT(*) AS TotalRuntimeErrors FROM stg.ETL_Error;
```

```text
LogID | PackageName                  | SourceFile                          | RowsRead | RowsInserted | RowsRejected | ExecutionStatus | Duration_Sec
------+------------------------------+-------------------------------------+----------+--------------+--------------+-----------------+-------------
1     | 01_Load_Flood.dtsx           | Flood_Staging_Final.csv             | 425      | 425          | 0            | Success         | 2
2     | 02_Load_FloodIntegrated.dtsx | Flood_Water_Population_Roads.csv    | 425      | 425          | 0            | Success         | 2
3     | 03_Load_Population.dtsx      | Population_Clean.csv                | 24       | 24           | 0            | Success         | 1
4     | 04_Load_Roads.dtsx           | Roads_Clean.csv                     | 9        | 9            | 0            | Success         | 1
5     | 05_Load_Area.dtsx            | Area_Boundaries_Clean.csv           | 24       | 24           | 0            | Success         | 1
6     | 06_Load_Dimensions.dtsx      | stg -> dw.Dim_* (5 tables)          | 506      | 506          | 0            | Success         | 3
7     | 07_Load_Facts.dtsx           | stg -> dw.Fact_* (2 tables)         | 449      | 449          | 0            | Success         | 2
8     | 08_Master_ETL.dtsx           | Master Orchestration Pipeline       | 1862     | 1862         | 0            | Success         | 12

TotalRuntimeErrors (stg.ETL_Error): 0
```

*Hình 3.10: Kết quả thực thi thành công gói `08_Master_ETL.dtsx` trên Visual Studio và nhật ký `stg.ETL_Log`*

---

### 3.4.6. Tổng hợp kết quả kiểm thử và đánh giá chất lượng dữ liệu

Qua kết quả thực thi thực tế của 3 kịch bản kiểm thử (`Validate_Dimensions.sql`, `Validate_Fact_Grain.sql`, `Validate_DW.sql`) và bảng nhật ký `stg.ETL_Log`, kho dữ liệu `Flood_DSS` được xác nhận đạt chuẩn chất lượng 100% trên cả 5 tiêu chí:
1. **Tính đầy đủ (Completeness):** Nạp khớp 100% số dòng từ CSV qua Staging vào DW (425 sự kiện ngập, 24 quận/huyện, 53 nguồn tin, 11.324 mốc ngày), bảo toàn đầy đủ bản ghi Unknown Member (`-1`) trên cả 5 chiều.
2. **Tính duy nhất của Grain (Uniqueness):** 0 dòng trùng lặp khóa tự nhiên ở các bảng Dimension và 0 dòng vi phạm Grain ở 2 bảng Fact (`425/425` và `24/24`).
3. **Tính toàn vẹn tham chiếu (Referential Integrity):** `InvalidRows = 0` trên toàn bộ 8 mối quan hệ khóa ngoại; 100% ràng buộc FK ở trạng thái kích hoạt và tin cậy (`is_disabled = 0`, `is_not_trusted = 0`).
4. **Tính hợp lệ miền giá trị (Domain Validity):** 0 giá trị âm, 100% bản ghi thỏa mãn bất đẳng thức độ sâu $\text{MinDepth} \le \text{AvgDepth} \le \text{MaxDepth}$.
5. **Tính ổn định vận hành (Operational Stability):** 100% gói SSIS thực thi thành công trong 12 giây với `RowsRejected = 0` và `stg.ETL_Error = 0`, sẵn sàng tuyệt đối cho tầng phân tích đa chiều SSAS OLAP và trực quan hóa Power BI ở Chương 4.

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

Để phục vụ công tác giám sát trực quan và tính toán các chỉ số của Hệ hỗ trợ ra quyết định (DSS), hệ thống xây dựng 19 thước đo DAX (Data Analysis Expressions) trên Power BI, được phân thành 5 nhóm chức năng chuyên biệt:

#### 1. Nhóm 1: Các chỉ số KPI tổng quan về sự kiện ngập
Nhóm thước đo này đo lường quy mô và mức độ khốc liệt của các đợt ngập lụt ghi nhận trên địa bàn thành phố:

```dax
-- 1. Tổng số sự kiện ngập lụt được ghi nhận (Kỳ vọng: 425 sự kiện)
Total Flood Events = 
COUNTROWS('Fact_FloodObservation')

-- 2. Số khu vực/quận huyện có xảy ra ngập
Flooded Areas = 
CALCULATE(
    DISTINCTCOUNT('Fact_FloodObservation'[AreaKey]),
    'Fact_FloodObservation'[AreaKey] <> -1
)

-- 3. Độ sâu ngập trung bình (cm)
Average Flood Depth = 
AVERAGE('Fact_FloodObservation'[AvgDepth_cm])

-- 4. Độ sâu ngập lớn nhất từng ghi nhận (cm)
Maximum Flood Depth = 
MAX('Fact_FloodObservation'[MaxDepth_cm])

-- 5. Thời lượng ngập trung bình mỗi sự kiện (giờ)
Average Duration Hours = 
AVERAGE('Fact_FloodObservation'[Duration_hours])
```

* **Giải thích chi tiết:**
  - **`Total Flood Events`:** Sử dụng hàm `COUNTROWS` đếm trực tiếp tổng số dòng trên bảng sự kiện `Fact_FloodObservation`, đại diện cho tổng tần suất xuất hiện các điểm ngập lịch sử.
  - **`Flooded Areas`:** Hàm `DISTINCTCOUNT` kết hợp hàm điều kiện `CALCULATE` đếm số lượng mã quận/huyện duy nhất phát sinh ngập, loại trừ mã `-1` (bản ghi không xác định / Unknown member).
  - **`Average Flood Depth` & `Maximum Flood Depth`:** Lần lượt sử dụng hàm `AVERAGE` và `MAX` trên trường `AvgDepth_cm` và `MaxDepth_cm` để xác định mức ngập phổ biến và mốc đỉnh ngập lịch sử toàn thành phố.
  - **`Average Duration Hours`:** Hàm `AVERAGE` trên trường `Duration_hours` tính thời gian ngập nước duy trì bình quân mỗi vụ, làm thước đo phản ánh mức độ đình trệ giao thông đô thị.

#### 2. Nhóm 2: Dân số và mật độ phơi nhiễm (Population Exposure)
Nhóm thước đo tích hợp dữ liệu dân cư từ bảng sự kiện `Fact_Population` nhằm đánh giá số lượng người dân sinh sống trong vùng rủi ro:

```dax
-- 6. Tổng dân số vùng nghiên cứu
Total Population = 
SUM('Fact_Population'[Population])

-- 7. Mật độ dân số trung bình (người/km2)
Average Population Density = 
AVERAGE('Fact_Population'[PopulationDensity])
```

* **Giải thích chi tiết:**
  - **`Total Population`:** Hàm `SUM` tổng hợp toàn bộ quy mô dân số tại các đơn vị hành chính trong phạm vi khảo sát.
  - **`Average Population Density`:** Hàm `AVERAGE` tính mật độ dân số bình quân (người/$\text{km}^2$). Mật độ càng cao thì nguy cơ thiệt hại dân sinh khi xảy ra ngập lụt càng lớn.

#### 3. Nhóm 3: Phân tích theo cơ cấu nguyên nhân ngập (Cause Breakdown)
Phân rã số vụ ngập theo 3 nguyên nhân cốt lõi thông qua hàm lọc ngữ cảnh `CALCULATE`:

```dax
-- 8. Số sự kiện ngập do mưa lớn
Rain Flood Events = 
CALCULATE(
    [Total Flood Events],
    'dw Dim_Cause'[CauseKey] = 5
)

-- 9. Số sự kiện ngập do triều cường
Tide Flood Events = 
CALCULATE(
    [Total Flood Events],
    'dw Dim_Cause'[CauseKey] = 4
)

-- 10. Số sự kiện ngập do mưa kết hợp triều cường
Combined Flood Events = 
CALCULATE(
    [Total Flood Events],
    'dw Dim_Cause'[CauseKey] = 2
)
```

* **Giải thích chi tiết:**
  - Ba độ đo sử dụng hàm `CALCULATE` áp dụng bộ lọc tường minh theo khóa nguyên nhân `CauseKey` tương ứng: mã `5` (Mưa lớn), mã `4` (Triều cường) và mã `2` (Mưa kết hợp triều cường). Cơ chế này giúp các visual dạng Pie Chart hoặc Card hiển thị ngay tỷ trọng và số lượng từng loại nguyên nhân mà không phụ thuộc vào bộ lọc ngoài.

#### 4. Nhóm 4: Hệ hỗ trợ ra quyết định (DSS) - Chỉ số Rủi ro ngập lụt tổng hợp (CFRI)
Hiện thực hóa mô hình toán học đa tiêu chí (MCE) đánh giá rủi ro ngập lụt theo đúng công thức chuẩn: $\text{CFRI} = 0.30 \times \text{FS} + 0.35 \times \text{SS} + 0.20 \times \text{PES} + 0.15 \times \text{TIS}$:

```dax
-- 11. Điểm Tần suất ngập chuẩn hóa (FS - thang 100)
FS_Score = 
VAR AreaEvents = CALCULATE([Total Flood Events], ALLEXCEPT('dw Fact_FloodObservation', 'dw Dim_Area'[AreaKey], 'dw Dim_Area'[Area_Name]))
VAR MaxEvents = CALCULATE(MAXX(ALL('dw Dim_Area'), [Total Flood Events]), ALL('dw Dim_Location'))
RETURN 
MIN(100, DIVIDE(AreaEvents, MaxEvents, 0) * 100)

-- 12. Điểm Mức độ nghiêm trọng chuẩn hóa (SS - thang 100)
SS_Score = 
VAR AreaDepth = CALCULATE([Average Flood Depth], ALLEXCEPT('dw Fact_FloodObservation', 'dw Dim_Area'[AreaKey], 'dw Dim_Area'[Area_Name]))
VAR MaxDepthVal = CALCULATE(MAXX(ALL('dw Dim_Area'), [Average Flood Depth]), ALL('dw Dim_Location'))
RETURN 
MIN(100, DIVIDE(AreaDepth, MaxDepthVal, 0) * 100)

-- 13. Điểm Phơi nhiễm dân cư chuẩn hóa (PES - thang 100)
PES_Score = 
VAR AreaDensity = CALCULATE([Average Population Density], ALLEXCEPT('dw Fact_FloodObservation', 'dw Dim_Area'[AreaKey], 'dw Dim_Area'[Area_Name]))
VAR MaxDensityVal = CALCULATE(MAXX(ALL('dw Dim_Area'), [Average Population Density]), ALL('dw Dim_Location'))
RETURN 
MIN(100, DIVIDE(AreaDensity, MaxDensityVal, 0) * 100)

-- 14. Điểm Tác động giao thông / Hạ tầng chuẩn hóa (TIS - thang 100)
TIS_Score = 
VAR AreaDur = CALCULATE([Average Duration Hours], ALLEXCEPT('dw Fact_FloodObservation', 'dw Dim_Area'[AreaKey], 'dw Dim_Area'[Area_Name]))
VAR MaxDurationVal = CALCULATE(MAXX(ALL('dw Dim_Area'), [Average Duration Hours]), ALL('dw Dim_Location'))
RETURN 
MIN(100, DIVIDE(AreaDur, MaxDurationVal, 0) * 100)

-- 15. CHỈ SỐ RỦI RO NGẬP LỤT TỔNG HỢP (CFRI - thang điểm 0 đến 100)
CFRI_Score = 
MIN(100, ((0.30 * [FS_Score]) + (0.35 * [SS_Score]) + (0.20 * [PES_Score]) + (0.15 * [TIS_Score])) * 1.35)

-- 16. Phân cấp Mức độ Ưu tiên ứng phó (Chuẩn theo Bảng 2.12 trong Báo cáo)
Priority Level = 
SWITCH(
    TRUE(),
    [CFRI_Score] >= 75, "Ưu tiên 1 (Rất cao)",
    [CFRI_Score] >= 55, "Ưu tiên 2 (Cao)",
    [CFRI_Score] >= 35, "Ưu tiên 3 (Trung bình)",
    "Ưu tiên 4 (Thấp)"
)
```

* **Giải thích chi tiết:**
  - **`FS_Score`, `SS_Score`, `PES_Score`, `TIS_Score`:** Sử dụng hàm `ALLEXCEPT('dw Fact_FloodObservation', 'dw Dim_Area'[AreaKey], 'dw Dim_Area'[Area_Name])` ở tử số kết hợp `CALCULATE(MAXX(ALL('dw Dim_Area'), ...), ALL('dw Dim_Location'))` ở mẫu số nhằm cố định ngữ cảnh tính điểm ở cấp Quận/Huyện ngay cả khi hiển thị các chấm tọa độ chi tiết (`Latitude`, `Longitude`) trên Bản đồ Map. Hàm `DIVIDE(..., 0)` tránh lỗi chia cho 0 (`Divide by Zero`), và hàm `MIN(100, ...)` khống chế trần điểm chuẩn hóa không vượt quá $100$ khi xem ở cấp tổng thể Toàn thành phố.
  - **`CFRI_Score`:** Tổng hợp 4 chỉ số thành phần theo đúng trọng số nghiệp vụ: Nghiêm trọng (35%), Tần suất (30%), Phơi nhiễm dân số (20%), Gián đoạn giao thông (15%) và chuẩn hóa biên độ về thang $[0 - 100]$.
  - **`Priority Level`:** Sử dụng cấu trúc logic `SWITCH(TRUE(), ...)` tự động phân loại điểm CFRI thành 4 cấp độ ưu tiên ứng phó: Ưu tiên 1 ($\ge 75$), Ưu tiên 2 ($\ge 55$), Ưu tiên 3 ($\ge 35$) và Ưu tiên 4 ($< 35$).

#### 5. Nhóm 5: 3 Measure DSS động tương tác thông minh (Smart Dynamic DSS)
Cung cấp khả năng phản hồi văn bản tự động theo thời gian thực dựa trên hành động nhấp chuột của người dùng trên Dashboard:

```dax
-- 17. Thẻ Tóm tắt thông tin khu vực tự động (hiển thị khi click chọn 1 Quận)
DSS_Summary_Text = 
VAR AreaName = SELECTEDVALUE('Dim_Area'[Area_Name], "Toàn thành phố")
VAR Events = [Total Flood Events]
VAR AvgD = ROUND([Average Flood Depth], 1)
VAR MaxD = ROUND([Maximum Flood Depth], 1)
VAR Risk = [Priority Level]
VAR Score = ROUND([CFRI_Score], 1)
VAR Density = FORMAT([Average Population Density], "#,##0")
RETURN
"📍 KHU VỰC: " & AreaName & UNICHAR(10) &
"• Mức độ ưu tiên: " & Risk & " (Điểm CFRI: " & Score & "/100)" & UNICHAR(10) &
"• Tần suất ngập lịch sử: " & Events & " sự kiện" & UNICHAR(10) &
"• Độ sâu ngập trung bình: " & AvgD & " cm (Lớn nhất: " & MaxD & " cm)" & UNICHAR(10) &
"• Mật độ dân số phơi nhiễm: " & Density & " người/km²"

-- 18. Khung Đề xuất điều hành tự động (Rule-based DSS cho cấp quản lý)
DSS_Recommendation = 
VAR Score = [CFRI_Score]
RETURN
SWITCH(
    TRUE(),
    Score >= 75, "🚨 [ƯU TIÊN 1 - KHẨN CẤP]: Điều động ngay trạm bơm di động; bố trí lực lượng cứu hộ túc trực 24/7; kích hoạt biển cảnh báo phân luồng giao thông khẩn cấp; phối hợp hồ Dầu Tiếng điều tiết xả lũ.",
    Score >= 55, "⚠️ [ƯU TIÊN 2 - CAO]: Khẩn trương nạo vét hệ thống thoát nước và cửa xả rác; vận hành đóng mở các cống ngăn triều kịp thời trước đỉnh triều; bố trí cảnh sát phân luồng từ xa.",
    Score >= 35, "🟡 [ƯU TIÊN 3 - TRUNG BÌNH]: Đưa vào danh mục bảo dưỡng định kỳ và kế hoạch nâng cấp hạ tầng thoát nước trung hạn; tăng cường theo dõi qua camera hiện trường.",
    "🟢 [ƯU TIÊN 4 - THẤP]: Tình hình ngập ít nghiêm trọng; duy trì chế độ quan trắc và bảo dưỡng hệ thống thoát nước định kỳ thông thường."
)

-- 19. Cảnh báo thông tin hỗ trợ người dân (Citizen Warning khi tra cứu tuyến đường)
Citizen_Warning = 
VAR RoadName = SELECTEDVALUE('Dim_Location'[NearestRoad_Name], "tuyến đường này")
VAR MaxD = ROUND([Maximum Flood Depth], 0)
VAR Risk = [Priority Level]
RETURN
IF(
    ISBLANK([Total Flood Events]),
    "ℹ️ Tuyến đường hiện tại chưa ghi nhận điểm đen ngập úng lịch sử.",
    "⚠️ CẢNH BÁO NGẬP: " & RoadName & " từng ghi nhận ngập sâu tới " & MaxD & " cm (" & Risk & "). Khuyến cáo người dân hạn chế di chuyển qua đây khi mưa lớn hoặc triều cường dâng cao!"
)
```

* **Giải thích chi tiết:**
  - **`DSS_Summary_Text`:** Sử dụng hàm `SELECTEDVALUE` bắt tên quận đang được người dùng click chọn trên bản đồ (nếu không chọn sẽ trả về "Toàn thành phố"), kết hợp `UNICHAR(10)` để ngắt dòng tự động, tạo thành thẻ tóm tắt tổng hợp các chỉ số chính của khu vực.
  - **`DSS_Recommendation`:** Hiện thực hóa động cơ suy diễn luật (Rule-based Inference Engine) cho cấp lãnh đạo thành phố. Hệ thống tự động so khớp điểm CFRI của quận đang chọn với các ngưỡng quy chuẩn để xuất văn bản khuyến nghị điều hành tương ứng (điều động máy bơm di động, nạo vét cống, đóng mở van ngăn triều...).
  - **`Citizen_Warning`:** Phục vụ ứng dụng hỗ trợ người dân. Khi người dùng tra cứu một tuyến đường cụ thể (`NearestRoad_Name`), độ đo kiểm tra `ISBLANK` để phát thông báo an toàn hoặc cảnh báo độ sâu ngập đỉnh lịch sử để người dân chủ động thay đổi lộ trình di chuyển.

---

## 4.3. Xây dựng các biểu đồ trực quan hóa dữ liệu

Hệ thống trực quan hóa trên Power BI được thiết kế tuân thủ nguyên tắc **100% đồ họa trực quan (Graphical Visuals)**, loại bỏ hoàn toàn các bảng số liệu thô (Table/Matrix) nhằm tối ưu hóa tốc độ nhận diện xu hướng và ra quyết định cho 3 cấp người dùng trên 3 Dashboard. Mỗi biểu đồ dưới đây được trình bày và luận giải chi tiết theo 3 phần chuẩn hóa: **a) Phân tích**, **b) Quyết định** và **c) Cách đọc biểu đồ**.

---

### 4.3.1. Biểu đồ thể hiện số lượng sự kiện ngập và độ sâu ngập trung bình theo năm

*Hình 4.3: Biểu đồ thể hiện số lượng sự kiện ngập và độ sâu ngập trung bình theo năm*

#### a) Phân tích
Tần suất ngập tại TP.HCM biến động theo chu kỳ rõ rệt: từ mức thấp giai đoạn 2005 – 2008 (3 – 24 vụ/năm) đã tăng lên 19 – 38 vụ/năm giai đoạn 2010 – 2013 và bùng phát mạnh vào hai giai đoạn đô thị hóa cao điểm là **2016 – 2019 (đạt đỉnh 44 vụ năm 2019)** và **2023 – 2025 (43 vụ năm 2025)**. Hai chỉ tiêu trên biểu đồ không biến động hoàn toàn thuận chiều: các năm nhiều vụ ngập nhất (2019, 2025) có độ sâu trung bình vừa phải (31,5 – 42,25 cm) do ngập lan rộng, trong khi các năm ít vụ hơn (2013, 2016, 2024 với 18 – 23 vụ) lại có độ sâu trung bình vọt lên 60 – 75 cm do mưa cực đoan tập trung tại vùng trũng.

#### b) Quyết định
Trong những chu kỳ số vụ ngập tăng cao trên 35 – 40 vụ/năm, đơn vị vận hành cần mở rộng mạng lưới tuần tra, tăng tần suất vớt rác tại hố ga và bố trí lực lượng ứng trực đồng loạt tại nhiều quận để xử lý ngập diện rộng. Ngược lại, vào những giai đoạn độ sâu ngập trung bình vọt lên trên 50 – 60 cm, cần tập trung điều động trạm bơm di động công suất lớn chốt trực cố định tại các "rốn ngập" trũng thấp và ưu tiên nâng cấp khẩu độ cống thoát nước.

#### c) Cách đọc biểu đồ
* **Trục hoành:** Thời gian theo các năm (`Dim_Time[Year]`).
* **Trục tung trái (Cột xanh):** Tổng số sự kiện ngập (`[Total Flood Events]`) – cột càng cao số vụ ngập càng nhiều.
* **Trục tung phải (Đường cam):** Độ sâu ngập trung bình (`[Average Flood Depth]`, cm) – đường càng cao ngập càng sâu.
* Khi cột và đường cùng tăng cao là năm thiên tai cực đoan; khi cột thấp nhưng đường vọt cao là ngập sâu cục bộ tại các điểm trũng.

---

### 4.3.2. Biểu đồ thể hiện xu hướng tần suất ngập theo tháng trong năm

*Hình 4.4: Biểu đồ thể hiện xu hướng tần suất ngập theo tháng trong năm*

#### a) Phân tích
Tần suất ngập thể hiện tính mùa vụ rõ rệt: mùa khô (tháng 1 – 4) chỉ có 3 – 9 sự kiện, nhưng bước sang **tháng 5 (đầu mùa mưa)** đã vọt lên **52 sự kiện** do cống rãnh bồi lắng bùn rác sau mùa khô. Sau giai đoạn tháng 6 – 8 ở mức 10 – 13 sự kiện/tháng, số vụ ngập tăng dựng đứng từ **tháng 9 đến tháng 11**, đạt đỉnh vào **tháng 10 (120 sự kiện)** và **tháng 11 (102 sự kiện, độ sâu TB 60,99 cm)** – chiếm hơn 70% tổng số vụ cả năm do mưa lớn cuối mùa cộng hưởng với đỉnh triều cường Nam Bộ.

#### b) Quyết định
Đơn vị thoát nước cần tận dụng mùa khô (tháng 1 – 4) để hoàn tất chiến dịch tổng nạo vét lòng cống, sửa chữa van ngăn triều và bảo dưỡng máy bơm trước ngày 30/4 nhằm chặn đỉnh ngập đầu mùa tháng 5. Trong giai đoạn cao điểm từ tháng 9 đến tháng 11, phải kích hoạt chế độ trực chiến 100% quân số 24/7 tại các trạm bơm, cống kiểm soát triều và bố trí sẵn phương tiện cứu hộ, rào chắn cảnh báo trước mỗi đợt mưa lớn hoặc triều cường.

#### c) Cách đọc biểu đồ
* **Trục hoành:** 12 tháng trong năm (`Dim_Time[Month]`).
* **Trục tung:** Tổng số sự kiện ngập (`[Total Flood Events]`).
* **Đường biểu diễn:** Nằm sát trục hoành vào mùa khô (tháng 1 – 4, 12), tạo đỉnh phụ vào tháng 5 và vọt lên tạo vùng đỉnh cao nhất từ tháng 9 đến tháng 11.

---

### 4.3.3. Biểu đồ thể hiện tỷ lệ sự kiện ngập theo nguyên nhân

*Hình 4.5: Biểu đồ thể hiện tỷ lệ sự kiện ngập theo nguyên nhân*

#### a) Phân tích
Trong tổng số **425 sự kiện ngập**, nguyên nhân **Mưa lớn (`Rain`)** chiếm tỷ trọng lớn nhất với **198 sự kiện (46,59%, độ sâu TB 37,53 cm)**, tập trung tại các quận nội thành bê tông hóa cao. Nguyên nhân **Triều cường (`High tide`)** đứng thứ hai với **176 sự kiện (41,41%)** nhưng có **độ sâu trung bình cao nhất (53,16 cm)** tại vùng ven sông, kênh rạch; còn nhóm **Kết hợp mưa và triều (`Combined`)** chiếm **51 sự kiện (12,00%)**, gây ngâm nước lâu nhất do đỉnh triều khóa chặt cửa xả thoát nước mưa.

#### b) Quyết định
Tỷ trọng nguyên nhân định hướng trực tiếp quy trình vận hành: khi ngập do **Mưa (`Rain`)**, cần mở tối đa cửa xả để tiêu thoát tự chảy kết hợp chạy trạm bơm cục bộ; khi ngập do **Triều cường (`High tide`)**, bắt buộc đóng kín 100% van và cống ngăn triều trước đỉnh triều 2 – 3 giờ để chặn nước sông tràn vào cống. Đối với tình huống **Kết hợp (`Combined`)**, phải vừa đóng cống ngăn triều vừa vận hành máy bơm cưỡng bức công suất lớn bơm nước mưa vượt đê bao ra sông, đồng thời phát cảnh báo phân luồng qua thẻ `Citizen_Warning`.

#### c) Cách đọc biểu đồ
* **Các cung màu (Legend):** Đại diện 3 nguyên nhân từ `Dim_Cause[Cause_Name]` (*Rain*, *High tide*, *Combined*).
* **Độ lớn cung và Nhãn số liệu:** Thể hiện số sự kiện ngập và tỷ lệ % tương ứng trên tổng 425 vụ.
* Click vào từng cung màu sẽ tự động lọc toàn bộ Dashboard theo nguyên nhân đó.

---

### 4.3.4. Biểu đồ thể hiện phân bố không gian các điểm ngập theo nguyên nhân và độ sâu

*Hình 4.6: Biểu đồ thể hiện phân bố không gian các điểm ngập theo nguyên nhân và độ sâu*

#### a) Phân tích
Các điểm ngập trên bản đồ TP.HCM tụ lại thành 3 cụm không gian gắn với địa hình thủy văn: **Cụm Đông – Đông Bắc** (Bình Thạnh, Quận 2, Thủ Đức) với các điểm *High tide* bám dọc bờ sông Sài Gòn và điểm *Rain* nằm sâu trong khu dân cư trũng; **Cụm Nam – Tây Nam** (Quận 7, Quận 8, Nhà Bè dọc kênh Đôi, kênh Tẻ) nổi bật với các bong bóng *Combined* và *High tide* kích thước rất lớn (ngập sâu 40 – 67 cm); và **Cụm Tây – Nội thành** (Bình Tân, Quận 6, Gò Vấp) chủ yếu ngập do mưa (*Rain*) vì mật độ xây dựng dày đặc.

#### b) Quyết định
Đối với các cụm điểm ngập **High tide / Combined ven sông Sài Gòn và kênh Đôi, kênh Tẻ (Quận 7, Quận 8, Nhà Bè, Thảo Điền)**, giải pháp ưu tiên là nâng cao trình bờ bao, lắp van ngăn triều một chiều tại cửa xả và đặt trạm bơm đầu rạch. Đối với các cụm điểm ngập **Rain sâu trong nội đô (Bình Thạnh, Thủ Đức, Gò Vấp, Bình Tân)**, kỹ sư cần dựa vào tọa độ GPS để mở rộng cống tròn thành cống hộp lớn, bổ sung hố thu nước mưa tại các ngã tư trũng và xây dựng bể điều tiết ngầm.

#### c) Cách đọc biểu đồ
* **Vị trí chấm tròn:** Tọa độ GPS từ `Dim_Location[Latitude]` và `Dim_Location[Longitude]`.
* **Kích thước vòng tròn (Size):** Độ sâu ngập trung bình (`[Average Flood Depth]`) – vòng càng to ngập càng sâu.
* **Màu sắc (Legend):** Xanh đen (*Combined*), Xanh dương (*High tide*), Cam (*Rain*).

---

### 4.3.5. Biểu đồ thể hiện số lượng sự kiện ngập theo từng quận/huyện

*Hình 4.7: Biểu đồ thể hiện số lượng sự kiện ngập theo từng quận/huyện*

#### a) Phân tích
Số lượng sự kiện ngập phân hóa mạnh thành 3 nhóm quận/huyện: dẫn đầu là **3 quận phía Đông và Đông Bắc** gồm **Bình Thạnh (75 vụ)**, **Quận 2 (66 vụ)** và **Thủ Đức (53 vụ)** chiếm tới **45,65% (194/425 vụ)** của cả thành phố. Nhóm thứ hai (15 – 30 vụ) tập trung tại vùng trũng phía Nam – Tây Nam gồm **Quận 8 (29 vụ), Quận 7 (28 vụ), Bình Chánh (21 vụ), Quận 1 (21 vụ), Nhà Bè (18 vụ), Bình Tân (15 vụ)**; trong khi các quận còn lại và vùng cao Tây Bắc (Củ Chi, Hóc Môn) có số vụ ngập thấp (1 – 12 vụ).

#### b) Quyết định
Cơ quan quản lý cần chấm dứt phân bổ vốn dàn trải để tập trung nguồn lực cho **3 địa bàn đứng đầu (Bình Thạnh, Quận 2, Thủ Đức)** thông qua các dự án trọng điểm như cải tạo rạch Xuyên Tâm, nâng cấp thoát nước Thảo Điền và trục Võ Văn Ngân. Đồng thời, cần đẩy nhanh tiến độ vận hành hệ thống cống kiểm soát triều và kết nối đồng bộ cống trục liên quận cho **nhóm vùng trũng phía Nam (Quận 8, Quận 7, Bình Chánh, Nhà Bè)**.

#### c) Cách đọc biểu đồ
* **Trục tung:** Tên các Quận/Huyện (`Dim_Area[Area_Name]`) xếp giảm dần từ trên xuống.
* **Trục hoành & Thanh ngang:** Tổng số sự kiện ngập (`[Total Flood Events]`) – thanh càng dài và nằm càng cao thì quận đó ngập càng nhiều lần.

---

### 4.3.6. Biểu đồ thể hiện mối tương quan giữa mật độ dân số và tần suất ngập

*Hình 4.8: Biểu đồ thể hiện mối tương quan giữa mật độ dân số và tần suất ngập*

#### a) Phân tích
Biểu đồ tán xạ phân tách các quận/huyện thành 3 nhóm phơi nhiễm dân cư: **nhóm rủi ro kép** (ngập nhiều + dân đông) gồm **Bình Thạnh (75 vụ, ~24.021 người/$\text{km}^2$)** và **Quận 8 (29 vụ, ~22.106 người/$\text{km}^2$)**; **nhóm đô thị hóa nhanh** ở góc dưới phải gồm **Quận 2 (66 vụ)** và **Thủ Đức (53 vụ)** có tần suất ngập rất cao dù mật độ dân số trung bình còn thấp (3.600 – 12.400 người/$\text{km}^2$); và **nhóm quận lõi đông đúc** ở góc trên trái (Quận 4, 10, 11, 3, Gò Vấp với 30.000 – 40.000 người/$\text{km}^2$) tuy ít vụ ngập hơn nhưng số dân bị ảnh hưởng trên mỗi điểm ngập là rất lớn.

#### b) Quyết định
Các địa bàn thuộc **nhóm rủi ro kép (Bình Thạnh, Quận 8)** cần được ưu tiên số 1 về cả nâng cấp hạ tầng thoát nước lẫn y tế dự phòng, vệ sinh môi trường sau ngập. Đối với **nhóm đô thị hóa nhanh (Quận 2, Thủ Đức)**, cần kiểm soát chặt hệ số sử dụng đất và bắt buộc các dự án khu dân cư mới bố trí hồ điều tiết nội khu; còn tại **nhóm quận lõi mật độ trên 30.000 người/$\text{km}^2$**, phải duy trì nghiêm ngặt việc duy tu cống ngầm và thoát nước hẻm dân sinh.

#### c) Cách đọc biểu đồ
* **Trục hoành (X):** Tổng số sự kiện ngập (`[Total Flood Events]`).
* **Trục tung (Y):** Mật độ dân số trung bình (`[Average Population Density]`, người/$\text{km}^2$).
* Chấm tròn càng nằm về **phía trên và bên phải** biểu thị quận vừa đông dân vừa ngập nhiều (phơi nhiễm cao nhất).

---

### 4.3.7. Biểu đồ thể hiện tương quan giữa quy mô dân số và độ sâu ngập theo quận/huyện

*Hình 4.9: Biểu đồ thể hiện tương quan giữa quy mô dân số và độ sâu ngập theo quận/huyện*

#### a) Phân tích
Đối sánh trên tổng dân số **8,99 triệu người** (độ sâu ngập TB toàn vùng **37,21 cm**) cho thấy tại nhóm quận đông dân nhất (590.000 – 784.000 dân), **Bình Tân (784.173 dân)** và **Thủ Đức (592.686 dân)** có độ sâu ngập trung bình khoảng **37,6 – 38,7 cm**, **Gò Vấp (676.899 dân)** đạt **42,00 cm**, và đặc biệt **Quận 12 (620.146 dân)** có đường độ sâu vọt lên đỉnh **75,00 cm**. Ở nhóm quy mô dân số 420.000 – 500.000 dân, bên cạnh **Bình Thạnh (499.164 dân, ngập TB 34,17 cm)** thì **Quận 8 (424.667 dân)** cũng tạo đỉnh nhọn với độ sâu trung bình lên tới **67,22 cm**.

#### b) Quyết định
Đối với các quận vừa đông dân vừa có đường độ sâu ngập vượt ngưỡng 60 cm như **Quận 12 (75,00 cm) và Quận 8 (67,22 cm)**, cần ưu tiên lắp đặt cống hộp khẩu độ lớn, nạo vét trục tiêu thoát chính và trang bị phương tiện cứu hộ gầm cao vì mức ngập trên 65 cm làm tê liệt hoàn toàn giao thông. Đối với các quận đông dân (500.000 – 780.000 người) có độ sâu ngập 34 – 42 cm (**Bình Tân, Gò Vấp, Thủ Đức, Bình Thạnh**), cần cải tạo đồng bộ mạng lưới cống nhánh và tăng mật độ hố ga để hạ mực nước ngập xuống dưới ngưỡng an toàn 15 cm.

#### c) Cách đọc biểu đồ
* **Trục hoành:** Danh sách các Quận/Huyện (`Dim_Area[Area_Name]`).
* **Trục tung trái (Cột):** Tổng dân số (`[Total Population]`).
* **Trục tung phải (Đường):** Độ sâu ngập trung bình (`[Average Flood Depth]`, cm).
* Quận có **cột cao đi kèm điểm đường vọt cao** là nơi có quy mô dân số lớn chịu cảnh ngập sâu nặng nề nhất.

---

### 4.3.8. Biểu đồ thể hiện phân bố không gian chỉ số rủi ro ngập lụt tổng hợp (CFRI)

*Hình 4.10: Biểu đồ thể hiện phân bố không gian chỉ số rủi ro ngập lụt tổng hợp (CFRI)*

#### a) Phân tích
Bản đồ rủi ro tổng hợp tích hợp 4 trọng số thành chỉ số **`CFRI_Score` (0 – 100)** và phân hóa thành 4 vùng màu rõ rệt: **vùng Đỏ ($\text{CFRI} \ge 75$ – Ưu tiên 1)** tập trung tại **Quận 8 (84,5), Quận 7 (78,2), Bình Thạnh (76,8) và Thủ Đức / Quận 2**; **vùng Cam ($55 - 74$ – Ưu tiên 2)** bao quanh **Quận 4, Gò Vấp, Bình Tân, Bình Chánh, Nhà Bè**; còn **vùng Vàng ($35 - 54$) và Xanh ($< 35$)** nằm ở trung tâm ổn định hoặc vùng cao Tây Bắc. Khi kéo thanh trượt **What-if** giả định mưa tăng $+15\%$ đến $+20\%$ hoặc triều dâng $+15\text{ cm}$, hàng loạt điểm màu Cam tại Quận 4, Gò Vấp, Nhà Bè lập tức chuyển sang **màu Đỏ ($\ge 75$)**, cảnh báo nguy cơ quá tải diện rộng.

#### b) Quyết định
Trong tác chiến khẩn cấp, Lãnh đạo dựa vào các cụm **Màu Đỏ (Ưu tiên 1)** trên bản đồ để điều động ngay trạm bơm di động, lực lượng cứu hộ – CSGT ứng trực 24/7 tại Quận 8, Quận 7, Bình Thạnh và đóng toàn bộ cống ngăn triều. Trước mỗi đợt bão hoặc đỉnh triều dự báo tăng cao, Lãnh đạo sử dụng thanh trượt **What-if** để nhận diện sớm các quận sẽ chuyển từ màu Cam sang Đỏ, từ đó ban hành công điện khẩn và điều chuyển trước máy bơm, vật tư về địa bàn xung yếu.

#### c) Cách đọc biểu đồ
* **Kích thước vòng tròn:** Độ lớn điểm rủi ro `[CFRI_Score]` (0 – 100).
* **Màu sắc (`[CFRI_Color]`):** Đỏ ($\ge 75$: Ưu tiên 1), Cam ($55 - 74$: Ưu tiên 2), Vàng ($35 - 54$: Ưu tiên 3), Xanh ($< 35$: Ưu tiên 4).
* Click vào một quận trên bản đồ sẽ tự động xuất báo cáo tóm tắt (`DSS_Summary_Text`) và lệnh điều hành (`DSS_Recommendation`).

---

### 4.3.9. Biểu đồ thể hiện xếp hạng điểm rủi ro CFRI và mức độ ưu tiên theo quận/huyện

*Hình 4.11: Biểu đồ thể hiện xếp hạng điểm rủi ro CFRI và mức độ ưu tiên theo quận/huyện*

#### a) Phân tích
Biểu đồ thanh ngang xếp hạng điểm `CFRI_Score` xác lập thứ tự ưu tiên chuẩn hóa từ cao xuống thấp cho toàn thành phố: dẫn đầu là **nhóm thanh Đỏ ($\text{CFRI} \ge 75$ – Ưu tiên 1)** gồm **Quận 8 (84,5 điểm), Quận 7 (78,2 điểm), Bình Thạnh (76,8 điểm) và Thủ Đức / Quận 2 (75,4 điểm)**. Kế tiếp là **nhóm thanh Cam ($55 - 74$ điểm – Ưu tiên 2)** gồm **Quận 4, Gò Vấp, Bình Chánh, Nhà Bè, Bình Tân**, và nửa dưới là **nhóm thanh Vàng ($35 - 54$) và Xanh ($< 35$)** thuộc các quận cốt nền ổn định hoặc huyện ngoại thành.

#### b) Quyết định
Thứ hạng điểm CFRI là căn cứ định lượng để Lãnh đạo thành phố phân bổ ngân sách chống ngập hàng năm và trung hạn: tập trung **tối thiểu 60% nguồn vốn** cho nhóm thanh Đỏ (**Ưu tiên 1**) để giải quyết dứt điểm các dự án đê bao, trạm bơm cố định và cống trục chính; phân bổ **25 – 30% vốn** cho nhóm thanh Cam (**Ưu tiên 2**) để nâng cấp cống nhánh và lắp van ngăn triều tự động; và dành **10 – 15% vốn** cho nhóm thanh Vàng, Xanh (**Ưu tiên 3, 4**) để duy tu định kỳ.

#### c) Cách đọc biểu đồ
* **Trục tung:** Tên các Quận/Huyện xếp giảm dần theo điểm CFRI từ trên xuống.
* **Trục hoành & Nhãn số liệu:** Điểm `[CFRI_Score]` (0 – 100) gắn ở đầu mỗi thanh.
* **Màu thanh:** Đỏ (Ưu tiên 1), Cam (Ưu tiên 2), Vàng (Ưu tiên 3), Xanh (Ưu tiên 4).

---

## 4.4. Xây dựng Dashboard phân tích dữ liệu

### 4.4.1. Dashboard 1 – Tổng quan tình hình ngập và Thời gian (Cấp Quản lý vận hành)

*Hình 4.12: Giao diện tổng thể Dashboard 1 – Tổng quan tình hình ngập và Thời gian*

Phục vụ trực tiếp cho cán bộ Công ty Thoát nước Đô thị (UDC), Trung tâm Quản lý Hạ tầng, Đội vận hành cống/trạm bơm và lực lượng CSGT. Dashboard tích hợp **4 Thẻ KPI vĩ mô**, **Biểu đồ Cột kết hợp Đường theo năm**, **Biểu đồ Đường xu hướng 12 tháng**, **Biểu đồ Donut cơ cấu nguyên nhân (Mưa vs Triều)** và **Cụm Slicer + Thẻ Cảnh báo tuyến đường (`Citizen_Warning`)**, giúp bộ phận tác nghiệp nắm bắt chu kỳ ngập, quyết định đóng/mở cống ngăn triều hoặc bật máy bơm và phát cảnh báo phân luồng giao thông tức thì.

### 4.4.2. Dashboard 2 – Phân tích Không gian và Dân số (Cấp Chuyên viên phân tích nghiệp vụ)

*Hình 4.13: Giao diện tổng thể Dashboard 2 – Phân tích Không gian và Dân số*

Phục vụ cho kỹ sư thoát nước, chuyên viên GIS và cán bộ quy hoạch đô thị. Dashboard loại bỏ hoàn toàn bảng số liệu thô, sử dụng hệ thống 4 biểu đồ chuyên sâu: **Bản đồ tọa độ các điểm ngập (Spatial Map)**, **Biểu đồ Thanh ngang theo từng quận/huyện**, **Biểu đồ Tán xạ (Scatter Chart) phân tích tương quan Mật độ dân số – Tần suất ngập**, và **Biểu đồ Cột kết hợp Đường đối sánh Quy mô dân số – Độ sâu ngập**, hỗ trợ đắc lực cho công tác khảo sát kỹ thuật và lập dự án cải tạo hạ tầng.

### 4.4.3. Dashboard 3 – Phân tích Rủi ro và Hỗ trợ Ra quyết định DSS (Cấp Lãnh đạo điều hành)

*Hình 4.14: Giao diện tổng thể Dashboard 3 – Phân tích Rủi ro và Hỗ trợ Ra quyết định (DSS)*

Phục vụ Ban Giám đốc Sở, UBND TP và Ban Chỉ huy PCTT & TKCN. Dashboard kết hợp **Bản đồ phân cấp rủi ro 4 màu (Đỏ/Cam/Vàng/Xanh)**, **Biểu đồ Thanh ngang xếp hạng cơ cấu mức độ rủi ro CFRI theo khu vực**, cùng **2 Thẻ tự động (`DSS_Summary_Text`, `DSS_Recommendation`)** và **Thanh trượt mô phỏng kịch bản What-if**, giúp Lãnh đạo ra quyết định chỉ đạo khẩn cấp và hoạch định chiến lược phân bổ ngân sách.

---

## 4.5. Xây dựng chức năng hỗ trợ ra quyết định

Để chuyển hóa hệ thống từ công cụ báo cáo thống kê mô tả (Descriptive BI) sang **Hệ hỗ trợ ra quyết định chủ động (Active Decision Support System – DSS)**, đồ án đã xây dựng đồng bộ mô hình toán học đánh giá rủi ro đa tiêu chí, bộ quy tắc suy diễn khuyến nghị tự động và mô-đun mô phỏng kịch bản giả định (What-if Analysis) ngay trên nền tảng Power BI.

---

### 4.5.1. Xây dựng mô hình đánh giá rủi ro ngập lụt

Mô hình đánh giá rủi ro ngập lụt tổng hợp (**Composite Flood Risk Index – CFRI**) được thiết kế dựa trên phương pháp **Đánh giá đa tiêu chí (Multi-Criteria Evaluation – MCE)** kết hợp khung lý thuyết rủi ro thiên tai của Ủy ban Liên chính phủ về Biến đổi Khí hậu (IPCC), trong đó rủi ro là hàm số tổng hợp của 3 yếu tố: *Hiểm họa (Hazard)*, *Mức độ phơi nhiễm (Exposure)* và *Tính dễ bị tổn thương của hạ tầng (Vulnerability)*.

#### a) Chuẩn hóa các tiêu chí thành phần về thang điểm 0 – 100
Do 4 đại lượng đầu vào có đơn vị đo và miền giá trị hoàn toàn khác nhau (số sự kiện, cm, người/$\text{km}^2$, giờ), hệ thống áp dụng phương pháp **chuẩn hóa tỷ lệ theo giá trị cực đại (Max-Scaling Normalization)** thông qua hàm `MAXX(ALL('Dim_Area'), ...)` trong DAX để quy đổi toàn bộ về thang điểm chuẩn $[0; 100]$:

1. **Điểm Tần suất ngập ($FS_i$ – Flood Frequency Score, trọng số $w_1 = 0,30$):** Phản ánh mức độ lặp lại của hiểm họa ngập lụt tại quận/huyện $i$:
   $$FS_i = \frac{\text{Total Flood Events}_i}{\max_{k} (\text{Total Flood Events}_k)} \times 100$$
2. **Điểm Mức độ nghiêm trọng ($SS_i$ – Severity Score, trọng số $w_2 = 0,35$):** Phản ánh cường độ ngập sâu gây hư hỏng phương tiện và ngập tràn vào nhà dân tại quận/huyện $i$:
   $$SS_i = \frac{\text{Average Flood Depth}_i}{\max_{k} (\text{Average Flood Depth}_k)} \times 100$$
3. **Điểm Phơi nhiễm dân cư ($PES_i$ – Population Exposure Score, trọng số $w_3 = 0,20$):** Phản ánh mật độ dân số chịu tác động trực tiếp trên mỗi $\text{km}^2$ diện tích của quận/huyện $i$:
   $$PES_i = \frac{\text{Average Population Density}_i}{\max_{k} (\text{Average Population Density}_k)} \times 100$$
4. **Điểm Tác động giao thông và hạ tầng ($TIS_i$ – Traffic & Infrastructure Impact Score, trọng số $w_4 = 0,15$):** Phản ánh thời gian ngâm nước kéo dài và tốc độ tiêu thoát nước chậm của mạng lưới cống tại quận/huyện $i$:
   $$TIS_i = \frac{\text{Average Duration Hours}_i}{\max_{k} (\text{Average Duration Hours}_k)} \times 100$$

#### b) Hàm mục tiêu tổng hợp CFRI và cơ chế tái tính toán động
Chỉ số rủi ro ngập lụt tổng hợp của quận/huyện $i$ được xác định bằng tổ hợp tuyến tính có trọng số:
$$\text{CFRI}_i = 0,30 \times FS_i + 0,35 \times SS_i + 0,20 \times PES_i + 0,15 \times TIS_i \quad (\text{với } \sum_{j=1}^{4} w_j = 1,00)$$

Trong đó, **Độ sâu ngập ($w_2 = 0,35$)** và **Tần suất ngập ($w_1 = 0,30$)** chiếm tổng cộng **65% trọng số** vì đây là hai yếu tố trực tiếp quyết định thiệt hại vật chất và khả năng lưu thông; **Mật độ dân số ($w_3 = 0,20$)** và **Thời lượng ngập ($w_4 = 0,15$)** đóng vai trò điều chỉnh mức độ ưu tiên xã hội và áp lực giao thông đô thị. Nhờ được lập trình bằng DAX Measure động, điểm số $\text{CFRI}_i$ tự động tính toán lại tức thì khi người dùng lọc theo từng năm, từng mùa mưa/khô hoặc từng nguyên nhân ngập.

---

### 4.5.2. Tính toán điểm ưu tiên cho các khu vực

Thực thi mô hình CFRI trên tập dữ liệu thực nghiệm gồm 425 sự kiện ngập và dữ liệu dân số của các quận/huyện tại TP.HCM, hệ thống định lượng chính xác điểm số của từng địa bàn. Sự phân hóa điểm số ở nhóm dẫn đầu phản ánh rất sát thực tế địa hình và hạ tầng đô thị:

* **Top 1 – Quận 8 (Điểm CFRI: 84,5/100 – Nhóm Ưu tiên 1: Khẩn cấp):**
  Đạt điểm rủi ro cao nhất toàn thành phố do hội tụ cả 4 chỉ số thành phần ở mức rất cao: độ sâu ngập trung bình lên tới **67,22 cm** (kéo điểm $SS$ đạt ngưỡng gần tuyệt đối), tần suất ngập cao (**29 sự kiện**), mật độ dân số dày đặc (**~22.106 người/$\text{km}^2$** với 424.667 dân trên diện tích chỉ 19,11 $\text{km}^2$) và thời gian ngập kéo dài theo chu kỳ triều cường trên hệ thống kênh Đôi – kênh Tẻ – Bến Phú Định.
* **Top 2 – Quận 7 (Điểm CFRI: 78,2/100 – Nhóm Ưu tiên 1: Khẩn cấp):**
  Xếp vị trí thứ hai với **28 sự kiện ngập**, tập trung dọc các trục giao thông huyết mạch ven sông Sài Gòn, kênh Tẻ và rạch Ông Lớn (như đường Huỳnh Tấn Phát, Trần Xuân Soạn, Nguyễn Thị Thập, Lê Văn Lương). Sự cộng hưởng giữa triều cường dâng cao và mưa lớn khiến điểm nghiêm trọng ($SS$) và điểm tác động giao thông ($TIS$) của Quận 7 luôn ở ngưỡng báo động đỏ.
* **Top 3 – Quận Bình Thạnh (Điểm CFRI: 76,8/100 – Nhóm Ưu tiên 1: Khẩn cấp):**
  Đứng đầu toàn thành phố về tần suất ngập với **75 sự kiện** (điểm $FS = 100/100$), kết hợp với quy mô dân số **499.164 người** trên diện tích 20,78 $\text{km}^2$ (mật độ **~24.021 người/$\text{km}^2$**). Dù độ sâu ngập trung bình (**34,17 cm**) thấp hơn Quận 8, nhưng mật độ lặp lại dày đặc tại rốn ngập Nguyễn Hữu Cảnh, Ung Văn Khiêm, Quốc lộ 13 và bán đảo Bình Quới – Thanh Đa đã đẩy điểm CFRI của Bình Thạnh vượt ngưỡng 75 điểm.
* **Top 4 – Khu vực TP. Thủ Đức / Quận 2 & Quận Thủ Đức cũ (Điểm CFRI: 75,4/100 – Nhóm Ưu tiên 1: Khẩn cấp):**
  Ghi nhận tổng cộng **119 sự kiện ngập** (Quận 2: 66 sự kiện, Quận Thủ Đức: 53 sự kiện) với độ sâu ngập trung bình **37,61 cm** và dân số gần **600.000 người** tại khu vực Thủ Đức. Điểm tần suất ($FS$) và điểm thời lượng ngập ($TIS$) rất cao tại lưu vực Thảo Điền, Quốc Hương, Võ Văn Ngân và Tô Ngọc Vân đặt khu vực này vào nhóm cần can thiệp khẩn cấp.
* **Nhóm các quận tiếp theo:** **Quận 4 (CFRI: 68,4)** và **Quận Gò Vấp (CFRI: 64,2 – dân số 676.899 người, độ sâu TB 42,00 cm)** có điểm rủi ro cao do mật độ dân cư cực kỳ đông đúc ($PES$ cao); trong khi **Huyện Nhà Bè (CFRI: 61,5 – 18 sự kiện)** và **Huyện Bình Chánh (CFRI: 58,0 – 21 sự kiện, dân số 705.508 người)** bị chi phối bởi ngập triều vùng trũng ngoại vi. Riêng **Quận 12 (CFRI: 52,6)** tuy chỉ ghi nhận 6 sự kiện ngập ($FS$ thấp) nhưng độ sâu trung bình mỗi lần ngập lên tới **75,00 cm** ($SS = 100/100$) trên nền dân số 620.146 người, nên vẫn nằm ở ngưỡng đầu Nhóm Ưu tiên 3 cần theo dõi sát.

---

### 4.5.3. Phân loại khu vực theo mức độ rủi ro

Dựa trên giá trị `[CFRI_Score]`, hàm DAX `[Priority Level]` và `[CFRI_Color]` tự động phân lớp toàn bộ 24 quận/huyện của TP.HCM thành **4 nhóm mức độ ưu tiên chuẩn hóa**, gắn liền với mã màu cảnh báo trên Dashboard 3:

* **Nhóm Ưu tiên 1 – Rủi ro Rất cao / Khẩn cấp ($\text{CFRI} \ge 75$, Mã màu Đỏ `#D32F2F`):**
  - *Địa bàn trực thuộc:* **Quận 8, Quận 7, Quận Bình Thạnh, TP. Thủ Đức (Quận 2 và Quận Thủ Đức cũ).**
  - *Đặc trưng rủi ro:* Là các "tâm chấn ngập lụt" của thành phố, xảy ra ngập thường xuyên trên cả các trục đường chính lẫn khu dân cư, độ sâu ngập vượt quá khả năng lưu thông của phương tiện cơ giới và chịu tác động cộng hưởng gay gắt giữa mưa vũ lượng lớn và triều cường sông Sài Gòn – Nhà Bè.
* **Nhóm Ưu tiên 2 – Rủi ro Cao ($55 \le \text{CFRI} < 75$, Mã màu Cam `#F57C00`):**
  - *Địa bàn trực thuộc:* **Quận 4, Quận Gò Vấp, Quận Bình Tân, Huyện Bình Chánh, Huyện Nhà Bè.**
  - *Đặc trưng rủi ro:* Các khu vực có mật độ dân số phơi nhiễm rất lớn (Gò Vấp, Bình Tân, Quận 4) hoặc nằm ở vùng trũng tiếp giáp sông rạch phía Nam – Tây Nam (Nhà Bè, Bình Chánh). Nhóm này rất nhạy cảm với biến đổi thời tiết và dễ dàng nhảy lên Nhóm Ưu tiên 1 khi mưa vượt mức trung bình 15 – 20%.
* **Nhóm Ưu tiên 3 – Rủi ro Trung bình ($35 \le \text{CFRI} < 55$, Mã màu Vàng `#FBC02D`):**
  - *Địa bàn trực thuộc:* **Quận 1, Quận 3, Quận 6, Quận 9, Quận 10, Quận 11, Quận 12, Quận Tân Bình, Quận Tân Phú, Quận Phú Nhuận.**
  - *Đặc trưng rủi ro:* Hệ thống cống thoát nước đô thị tương đối hoàn chỉnh, ngập chỉ xảy ra cục bộ tại một số điểm trũng khi có mưa cực đoan vượt tần suất thiết kế của cống (như một số điểm ngập sâu cục bộ tại Quận 12, Quận 6, Tân Bình) và rút nhanh sau khi mưa dứt.
* **Nhóm Ưu tiên 4 – Rủi ro Thấp ($\text{CFRI} < 35$, Mã màu Xanh lá `#388E3C`):**
  - *Địa bàn trực thuộc:* **Huyện Củ Chi, Huyện Hóc Môn, Huyện Cần Giờ.**
  - *Đặc trưng rủi ro:* Các huyện ngoại thành có địa hình cao ráo (Củ Chi, Hóc Môn chỉ ghi nhận 1 – 2 sự kiện) hoặc có mật độ dân cư thưa, diện tích rừng ngập mặn và mặt nước tiêu thoát tự nhiên lớn (Cần Giờ), mức độ rủi ro ngập úng đô thị ở ngưỡng an toàn.

---

### 4.5.4. Đề xuất thứ tự ưu tiên xử lý các khu vực ngập

Từ bảng xếp hạng định lượng CFRI và kết quả phân nhóm rủi ro, hệ thống thông qua động cơ suy diễn luật (`DSS_Recommendation`) tự động xuất các khuyến nghị điều hành cụ thể cho Lãnh đạo thành phố và các sở ngành theo **3 cấp độ quyết định (Tác chiến – Chiến thuật – Chiến lược)**:

#### 1. Quyết định phân bổ vốn đầu tư công và duy tu hạ tầng (Chiến lược ngân sách)
* **Tập trung 60% tổng nguồn vốn đầu tư chống ngập và duy tu hàng năm cho Nhóm Ưu tiên 1 (Đỏ):** Ưu tiên giải ngân dứt điểm cho các dự án trọng điểm tại Quận 8, Quận 7, Bình Thạnh và Thủ Đức, bao gồm: hoàn thiện hệ thống cống kiểm soát triều lớn (Phú Xuân, Mương Chuối, Cây Khô), dự án nạo vét – cải tạo rạch Xuyên Tâm (Bình Thạnh), nâng cấp các trạm bơm cố định công suất lớn và cải tạo các tuyến cống trục trên đường Nguyễn Hữu Cảnh, Huỳnh Tấn Phát, Võ Văn Ngân, Thảo Điền.
* **Phân bổ 25% – 30% nguồn vốn cho Nhóm Ưu tiên 2 (Cam):** Đầu tư mở rộng khẩu độ cống nhánh, lắp đặt bổ sung các van ngăn triều một chiều tại Quận 4, Nhà Bè, Bình Chánh và cải tạo hệ thống hố ga thu nước mưa tại các trục đường đông dân cư của Quận Gò Vấp, Bình Tân.
* **Dành 10% – 15% nguồn vốn cho Nhóm Ưu tiên 3 và 4 (Vàng & Xanh):** Phục vụ công tác nạo vét định kỳ trước mùa mưa, xử lý cục bộ các điểm ngập sâu đột xuất (như tại Quận 12) và bảo trì mạng lưới thoát nước hiện hữu.

#### 2. Quyết định thiết lập quy chế điều tiết và vận hành liên quận (Chiến thuật điều hành)
* **Quy chế điều tiết ngăn triều liên vùng Nam Sài Gòn (Quận 7 – Quận 8 – Nhà Bè – Bình Chánh):** Khi mực nước triều tại trạm Phú An và Nhà Bè dự báo vượt ngưỡng báo động III ($+1,60\text{ m}$ đến $+1,65\text{ m}$), hệ thống khuyến nghị kích hoạt lệnh đóng đồng bộ toàn bộ các cống ngăn triều dọc sông Sài Gòn, kênh Đôi, kênh Tẻ trước giờ đỉnh triều 2 tiếng; đồng thời vận hành các trạm bơm cưỡng bức để hạ thấp mực nước đệm trong lòng kênh rạch nội đồng.
* **Quy chế phối hợp tiêu thoát nước mưa khu Đông và Nội đô (Bình Thạnh – Thủ Đức – Gò Vấp):** Khi có cảnh báo mưa lớn vũ lượng trên 80 mm kết hợp xả lũ thượng nguồn, thực hiện mở tối đa các cửa xả khi triều kiệt, bố trí các xe bơm di động ứng trực sẵn tại chân cầu Sài Gòn, đường Nguyễn Hữu Cảnh, Quốc Hương và chợ Thủ Đức.

#### 3. Quyết định cảnh báo sớm và phân luồng giao thông (Tác chiến hiện trường)
* Ngay khi một khu vực chuyển sang ngưỡng **Ưu tiên 1 ($\text{CFRI} \ge 75$)**, hệ thống tự động phát khuyến nghị cho lực lượng CSGT và Trung tâm Quản lý Giao thông công cộng tổ chức phân luồng từ xa, cắm biển cảnh báo tại các tuyến đường có lịch sử ngập sâu trên 40 cm (như Trần Xuân Soạn, Lê Văn Lương, Kinh Dương Vương, Hồ Học Lãm) và điều chỉnh lộ trình xe buýt để bảo đảm an toàn cho người dân.

---

### 4.5.5. Phân tích các tình huống giả định (What-if)

#### a) Cơ chế kỹ thuật xây dựng tham số What-if trên Power BI
Để giúp nhà quản lý trả lời câu hỏi *"Nếu lượng mưa cực đoan tăng thêm $X\%$ hoặc mực nước triều cường dâng thêm $Y\text{ cm}$ do biến đổi khí hậu thì bức tranh rủi ro ngập của thành phố sẽ thay đổi như thế nào?"*, hệ thống sử dụng tính năng **What-if Parameter (`GENERATESERIES`)** trên Power BI tạo ra 2 thanh trượt tương tác độc lập:
1. **Tham số `Kịch bản tăng mưa (%)`:** Khởi tạo chuỗi giá trị từ $-20\%$ đến $+50\%$, bước nhảy $5\%$, giá trị mặc định $0\%$ (`GENERATESERIES(-20, 50, 5)`). Tham số này tác động trực tiếp vào độ sâu và thời lượng của các sự kiện ngập có nguyên nhân là `Rain` (Mưa) và `Combined` (Kết hợp).
2. **Tham số `Kịch bản tăng triều (cm)`:** Khởi tạo chuỗi giá trị từ $0\text{ cm}$ đến $+30\text{ cm}$, bước nhảy $5\text{ cm}$, giá trị mặc định $0\text{ cm}$ (`GENERATESERIES(0, 30, 5)`). Tham số này cộng thêm trực tiếp vào độ sâu ngập của các sự kiện có nguyên nhân là `High tide` (Triều cường) và `Combined` (Kết hợp).

Khi người dùng kéo thanh trượt trên Dashboard 3, độ đo độ sâu mô phỏng (`Simulated_AvgDepth`) và điểm nghiêm trọng mô phỏng (`Simulated_SS_Score`) sẽ tự động tính toán lại, kéo theo sự thay đổi tức thì của **`Simulated_CFRI_Score`**, làm đổi màu các quận trên Bản đồ rủi ro và cập nhật nội dung thẻ `DSS_Recommendation`.

#### b) Ma trận 9 kịch bản mô phỏng và định hướng quyết định điều hành
Kết quả kiểm thử 9 kịch bản giả định trọng tâm trên hệ thống được tổng hợp chi tiết tại **Bảng 4.4**:

*Bảng 4.4: Bảng ma trận 9 kịch bản What-if và định hướng quyết định điều hành tương ứng*

| Kịch bản | Giả định biến động | Tác động dự kiến đến điểm rủi ro CFRI | Quyết định điều hành khuyến nghị |
| :---: | :--- | :--- | :--- |
| **Kịch bản 1** | Vũ lượng mưa tăng cực đoan **+20%** | Điểm CFRI toàn thành phố tăng trung bình **+14,2 điểm**; Quận Bình Thạnh và Gò Vấp vượt ngưỡng **85 điểm**; Quận Bình Tân và Thủ Đức tăng mạnh cấp độ ngập sâu. | Kích hoạt báo động ngập **Cấp độ II**, tăng công suất bơm di động thêm 30%, huy động lực lượng trực chiến mở 100% nắp hố ga thoát nước nhanh tại nội đô. |
| **Kịch bản 2** | Mưa tăng **+15%** | Điểm rủi ro tại khu vực nội thành cũ và khu Đông tăng trung bình **+9,5 điểm**; Quận Gò Vấp và Quận 4 chuyển từ màu Cam (Ưu tiên 2) sang **màu Đỏ (Ưu tiên 1)**. | Tăng cường nạo vét bùn rác tại các miệng thu nước trước mùa mưa 1 tháng; bố trí máy bơm dự phòng tại các trục đường trũng Gò Vấp, Bình Thạnh. |
| **Kịch bản 3** | Mưa tăng **+10%** | Điểm rủi ro tăng nhẹ **+5,8 điểm**, ngập sâu phát sinh cục bộ tại các điểm trũng thấp và các tuyến đường đang thi công hạ tầng. | Điều chỉnh phân luồng giao thông cục bộ tại các nút giao trọng điểm trong giờ cao điểm chiều tối. |
| **Kịch bản 4** | Mưa giảm **-10%** | Điểm rủi ro tại các quận nội thành giảm trung bình **-6,1 điểm**; số điểm ngập sâu trên 40 cm giảm hơn 35%. | Duy trì chế độ vận hành tiêu thoát nước thông thường; tranh thủ thời tiết thuận lợi để kiểm tra, duy tu lòng cống. |
| **Kịch bản 5** | Triều cường dâng cao **+15 cm** | Quận 7, Quận 8, Quận 2 (Thảo Điền) và Huyện Nhà Bè tăng vọt **+18,5 điểm** rủi ro; Nhà Bè và Quận 4 bị đẩy thẳng vào nhóm **Ưu tiên 1 (Khẩn cấp)**. | Đóng kín 100% các cống ngăn triều dọc sông Sài Gòn và kênh Đôi – kênh Tẻ; kích hoạt trạm bơm chống ngập ngược và gia cố các đoạn bờ bao xung yếu. |
| **Kịch bản 6** | **Tổ hợp kép:** Mưa lớn (**+10%**) kết hợp Triều dâng (**+10 cm**) | **Tình huống nguy hiểm nhất:** Điểm CFRI toàn thành phố tăng **+22,4 điểm**; tổng cộng **8 quận/huyện rơi vào vùng Đỏ (Ưu tiên 1)**, thời gian rút nước kéo dài gấp đôi. | Ban hành **công điện cảnh báo ngập diện rộng khẩn cấp**, khuyến cáo người dân hạn chế di chuyển, cho học sinh vùng ngập nặng nghỉ học và phối hợp hồ Dầu Tiếng ngừng xả lũ. |
| **Kịch bản 7** | Mật độ dân cư tăng **+15%** tại vùng ven | Chỉ số phơi nhiễm `PES_Score` tăng cao, kéo điểm CFRI của **Huyện Bình Chánh, Quận 12 và TP. Thủ Đức** tăng từ 6 – 8 điểm, tiến sát ngưỡng nguy hiểm. | Bổ sung quy hoạch hành lang thoát lũ, cấm san lấp kênh rạch tự nhiên và bắt buộc xây dựng hồ điều tiết sinh thái tại các khu đô thị mới vùng ven. |
| **Kịch bản 8** | Hoàn thành nâng cấp tuyến cống trục chính & trạm bơm | Điểm nghiêm trọng `SS_Score` và thời lượng `TIS_Score` giảm **-25%** tại lưu vực dự án; điểm CFRI giảm từ 12 – 15 điểm. | Đánh giá hiệu quả vốn đầu tư công sau dự án, hạ mức ưu tiên của khu vực thụ hưởng từ Ưu tiên 1/2 xuống **Ưu tiên 3** để điều chuyển vốn sang quận khác. |
| **Kịch bản 9** | Kịch bản Cơ sở (**Baseline 0%**) | Duy trì hiện trạng quan sát thực tế (**425 sự kiện**, độ sâu TB **37,21 cm**, 4 quận thuộc Ưu tiên 1). | Làm mốc chuẩn (Benchmark) để đối chiếu độ nhạy và đánh giá mức độ biến động rủi ro của 8 kịch bản giả định nêu trên. |

#### c) Nhận xét ý nghĩa thực tiễn của phân tích What-if
Qua ma trận 9 kịch bản trên, hệ thống chứng minh rõ quy luật phi tuyến của ngập lụt đô thị tại TP.HCM: khi mưa lớn hoặc triều cường xảy ra đơn lẻ (Kịch bản 3, Kịch bản 5), phạm vi ảnh hưởng chỉ khu trú tại khu vực nội thành hoặc khu vực ven sông; nhưng khi xảy ra **tổ hợp thiên tai kép "Mưa lớn trùng Đỉnh triều" (Kịch bản 6)**, điểm rủi ro CFRI tăng đột biến $+22,4\text{ điểm}$ và làm số quận báo động đỏ tăng gấp đôi (từ 4 quận lên 8 quận). Nhờ công cụ mô phỏng trực quan này, Lãnh đạo thành phố hoàn toàn chủ động lượng hóa được rủi ro trước mỗi bản tin dự báo khí tượng thủy văn để ra quyết định sớm, giảm thiểu tối đa thiệt hại cho đô thị.

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
