# Flood Decision Support System (Flood_DSS)

Hệ thống hỗ trợ ra quyết định quản lý và ứng phó ngập lụt tại Thành phố Hồ Chí Minh (Decision Support System for Flood Management in HCMC).

---

## 📁 Cấu trúc thư mục (Repository Structure)

```text
Flood_DSS/
├── 00_Documents/         # Tài liệu thiết kế hệ thống, yêu cầu nghiệp vụ & mô hình Kimball
│   ├── 01_Business_Requirements/
│   ├── 02_Kimball_Design/
│   ├── 05_DSS_Design/
│   └── 06_System_Design/
├── 01_Raw/               # Dữ liệu thô ban đầu (Flood, GIS, Population, Rainfall)
├── 02_Staging_CSV/       # Dữ liệu CSV sau khi trích xuất & làm sạch
├── 03_Python/            # Kịch bản Python xử lý, chuẩn hóa và tích hợp không gian
├── 04_SQL_Server/        # Kịch bản tạo bảng chiều, bảng sự kiện và dữ liệu kịch bản
├── 05_SSIS/              # Gói SSIS phục vụ quy trình ETL
├── 06_QGIS/              # Bản đồ không gian, lớp layer và dự án QGIS (Flood_DSS.qgz)
├── 07_Logs/              # Báo cáo kiểm định chất lượng dữ liệu và nhật ký tích hợp
├── 08_SSAS/              # Mô hình phân tích SSAS Tabular/Multidimensional
├── 09_DSS/               # Công cụ mô phỏng kịch bản, quy tắc DSS và tính toán trọng số
├── 10_PowerBI/           # Báo cáo trực quan hóa Power BI (.pbix)
└── 11_Web_App/           # Ứng dụng web hiển thị bản đồ và phân tích kịch bản ngập lụt
```

---

## 🛠️ Công nghệ sử dụng (Tech Stack)

- **Ngôn ngữ**: Python, SQL
- **GIS & Không gian**: QGIS, GeoPandas, Shapely, PyProj
- **Cơ sở dữ liệu**: Microsoft SQL Server / Azure SQL
- **Phân tích & BI**: Microsoft SSAS, Microsoft Power BI
- **Quản lý phiên bản**: Git & GitHub
