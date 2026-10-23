# Quy Tắc Khuyến Nghị Hỗ Trợ Ra Quyết Định (Rule-Based DSS)

Tập luật minh bạch (Transparency Rules) được cấu hình trong bảng `dss.DSS_Rule` để tự động đưa ra khuyến nghị hành động cho cơ quan quản lý và thông tin cảnh báo cho người dân.

---

## 1. Nhóm khuyến nghị dành cho Cơ quan Quản lý (Decision Makers)

| Mã luật (RuleCode) | Điều kiện kích hoạt (Condition) | Mức ưu tiên | Nội dung khuyến nghị (Recommendation) |
|---|---|:---:|---|
| `RULE_MGT_01` | `PriorityScore >= 70 AND ExposureScore >= 70` | 🔴 CAO | **Ưu tiên bảo vệ dân sinh cấp bách:** Khu vực có mật độ dân cư rất cao và tần suất ngập nặng. Đề xuất bố trí ngay máy bơm di động, thiết lập rào chắn cảnh báo giao thông tại các nút giao trũng thấp, và huy động đội phản ứng nhanh ứng trực. |
| `RULE_MGT_02` | `PriorityScore >= 70 AND WaterProximityScore >= 75` | 🔴 CAO | **Kiểm tra bờ bao và van ngăn triều:** Điểm ngập nằm sát hành lang kênh rạch kết hợp triều cường/nước dâng. Đề xuất khảo sát hiện trạng sạt lở bờ bao, kiểm tra vận hành các cống ngăn triều lân cận. |
| `RULE_MGT_03` | `40 <= PriorityScore < 70` | 🟡 TRUNG BÌNH | **Duy tu & giám sát định kỳ:** Đưa khu vực vào danh mục nạo vét hệ thống thoát nước trước mùa mưa; định kỳ kiểm tra các hố ga và điểm nghẽn dòng chảy. |
| `RULE_MGT_04` | `PriorityScore < 40` | 🟢 THẤP | **Duy trì quan trắc:** Nguy cơ thấp trong điều kiện thông thường, tiếp tục thu thập dữ liệu quan trắc định kỳ. |
| `RULE_MGT_WARN` | `AssessmentStatus = 'InsufficientData'` | ⚠️ CẢNH BÁO | **Rà soát dữ liệu hành chính/không gian:** Khu vực thiếu số liệu thống kê dân số hoặc tọa độ chưa khớp ranh giới chuẩn. Cần cập nhật chuẩn hóa trước khi ra quyết định đầu tư công. |

---

## 2. Nhóm khuyến nghị hỗ trợ Người dân (Citizen Guidance)

| Mã luật (RuleCode) | Điều kiện kích hoạt | Mức nguy cơ | Nội dung hỗ trợ người dân |
|---|---|:---:|---|
| `RULE_CIT_01` | Lịch sử ngập tái diễn (`FloodCount >= 5` và `AvgDepth_cm >= 30`) | 🔴 NGUY CƠ CAO | Đoạn đường/khu vực có tiền sử ngập sâu trên 30cm khi có triều cường hoặc mưa lớn. Cân nhắc chọn lộ trình thay thế, hạn chế xe máy và phương tiện gầm thấp lưu thông vào khung giờ triều đạt đỉnh. |
| `RULE_CIT_02` | `FloodCount >= 1` và `AvgDepth_cm < 30` | 🟡 NGUY CƠ VỪA | Tuyến đường có xuất hiện ngập cục bộ, độ sâu trung bình dưới 30cm. Lưu ý giảm tốc độ và chú ý nắp hố ga. |
| `RULE_CIT_03` | Không có ghi nhận ngập lịch sử | 🟢 AN TOÀN | Không ghi nhận ngập trong cơ sở dữ liệu quan trắc lịch sử. |
