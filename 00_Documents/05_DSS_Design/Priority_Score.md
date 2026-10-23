# Thiết kế Công thức Tính Điểm Ưu Tiên Ứng Phó Ngập (Priority Score)

Hệ thống hỗ trợ ra quyết định (DSS) phân loại mức độ ưu tiên ứng phó ngập lụt tại các khu vực thuộc TP.HCM dựa trên 4 thành phần cốt lõi.

---

## 1. Công thức tổng quát

$$PriorityScore = 0.35 \times FloodFrequencyScore + 0.30 \times SeverityScore + 0.25 \times ExposureScore + 0.10 \times WaterProximityScore$$

| Thành phần | Tỷ trọng | Thang điểm | Nguồn dữ liệu | Ý nghĩa nghiệp vụ |
|---|---:|:---:|---|---|
| **FloodFrequencyScore** | **35%** | 0 – 100 | `dw.Fact_FloodObservation` | Tần suất xuất hiện các đợt ngập trong kỳ phân tích tại khu vực. |
| **SeverityScore** | **30%** | 0 – 100 | `dw.Fact_FloodObservation` | Mức độ nghiêm trọng dựa trên độ sâu ngập trung bình / tối đa ghi nhận. |
| **ExposureScore** | **25%** | 0 – 100 | `dw.Fact_Population` | Mức độ phơi nhiễm dân cư (Mật độ dân số người/km² theo địa giới). |
| **WaterProximityScore** | **10%** | 0 – 100 | `dw.Dim_Location` | Khoảng cách đại diện đến sông/kênh/rạch (chỉ báo không gian thoát nước/triều). |
| **Tổng** | **100%** | **0 – 100** | | Điểm số tổng hợp đại diện mức độ ưu tiên ứng phó. |

> [!NOTE]
> **Phạm vi Giai đoạn 4:** Đã chính thức loại bỏ chỉ số Lượng mưa (`RainfallScore`) và Cao độ địa hình (`ElevationScore`) do dữ liệu NASA thô và chưa có nguồn DEM chuẩn hóa toàn thành phố.

---

## 2. Phương pháp chuẩn hóa (Min-Max Normalization về thang 0–100)

1. **Điểm Tần suất ($FloodFrequencyScore$):**
   $$Score_{Freq} = \min\left(100, \frac{FloodCount}{MaxThreshold_{Freq}} \times 100\right)$$
   *(Ví dụ: Ngưỡng tối đa 20 đợt ngập = 100 điểm)*

2. **Điểm Mức độ nghiêm trọng ($SeverityScore$):**
   $$Score_{Sev} = 0.6 \times \left(\frac{AvgDepth\_cm}{MaxDepthThreshold} \times 100\right) + 0.4 \times \left(\frac{MaxDepth\_cm}{ExtremeDepthThreshold} \times 100\right)$$

3. **Điểm Phơi nhiễm dân cư ($ExposureScore$):**
   $$Score_{Exp} = \frac{PopulationDensity - MinDensity}{MaxDensity - MinDensity} \times 100$$

4. **Điểm Khoảng cách sông/kênh ($WaterProximityScore$):**
   Càng gần sông/kênh thì điểm rủi ro càng cao (nghịch đảo khoảng cách):
   $$Score_{Prox} = \max\left(0, \left(1 - \frac{DistanceToWater\_m}{MaxInfluenceDist}\right) \times 100\right)$$
   *(Với $MaxInfluenceDist = 1000m$; nếu khoảng cách > 1000m thì điểm = 0)*

---

## 3. Phân loại mức độ ưu tiên (Priority Levels)

- 🔴 **Ưu tiên CAO (High Priority):** $PriorityScore \ge 70$  
  *(Cần khảo sát cấp bách, bố trí máy bơm lưu động, kiểm tra cống nghẹt).*
- 🟡 **Ưu tiên TRUNG BÌNH (Medium Priority):** $40 \le PriorityScore < 70$  
  *(Theo dõi diễn biến triều cường, duy tu định kỳ nạo vét).*
- 🟢 **Ưu tiên THẤP (Low Priority):** $PriorityScore < 40$  
  *(Duy trì trạng thái quan trắc thông thường).*

---

## 4. Xử lý thiếu dữ liệu (Data Quality & Policy)

- Nếu khu vực không có dữ liệu dân số (`PopulationDensity IS NULL`) hoặc vị trí chưa xác minh:  
  `AssessmentStatus = 'InsufficientData'`
- Tuyệt đối không thay thế `NULL` bằng `0` để tránh làm méo mó điểm trung bình.
