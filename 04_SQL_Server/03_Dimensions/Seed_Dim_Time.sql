/*
============================================================
Project : Flood Decision Support System (Flood_DSS)
Script  : Seed_Dim_Time.sql
Owner   : TV4 (Dimension Tables & Dimension ETL)

Purpose :
    Automatically generate and populate calendar dates into dw.Dim_Time.
    
Scope:
    - Period: 2000-01-01 -> 2030-12-31 (Covers all historical floods & 2026 data).
    - Preserves Unknown member (TimeKey = -1).
    - Idempotent: Does not insert duplicates if dates already exist.
============================================================
*/

USE Flood_DSS;
GO

PRINT N'Starting generation of Dim_Time calendar...';

/* =========================================================
   1. CẤU HÌNH KHOẢNG THỜI GIAN CẦN SINH LỊCH
   ========================================================= */
DECLARE @StartDate DATE = '2000-01-01';
DECLARE @EndDate   DATE = '2030-12-31';

/* =========================================================
   2. TẠO LỊCH BẰNG BẢNG TẠM VÀ NẠP TẬP HỢP (TỐI ƯU CỰC NHANH)
   Sử dụng CTE đệ quy / Tally table để nạp hàng chục năm chỉ mất < 1 giây
   ========================================================= */
;WITH DateSequence AS
(
    SELECT @StartDate AS CalendarDate
    UNION ALL
    SELECT DATEADD(DAY, 1, CalendarDate)
    FROM DateSequence
    WHERE CalendarDate < @EndDate
)
INSERT INTO dw.Dim_Time
(
    TimeKey,
    FullDate,
    [Day],
    [Month],
    [Quarter],
    [Year],
    Season,
    DayOfWeek
)
SELECT
    -- TimeKey: Định dạng YYYYMMDD
    YEAR(CalendarDate) * 10000 + MONTH(CalendarDate) * 100 + DAY(CalendarDate) AS TimeKey,
    CalendarDate AS FullDate,
    DAY(CalendarDate) AS [Day],
    MONTH(CalendarDate) AS [Month],
    DATEPART(QUARTER, CalendarDate) AS [Quarter],
    YEAR(CalendarDate) AS [Year],
    
    -- Phân loại mùa tại TP.HCM: Tháng 5-11 là mùa mưa, còn lại là mùa khô
    CASE 
        WHEN MONTH(CalendarDate) BETWEEN 5 AND 11 THEN N'Rainy'
        ELSE N'Dry'
    END AS Season,

    -- Thứ trong tuần (1: Chủ Nhật -> 7: Thứ Bảy theo chuẩn không phụ thuộc DATEFIRST)
    ((DATEDIFF(DAY, '19000101', CalendarDate) % 7) + 1) AS DayOfWeek
FROM DateSequence d
WHERE NOT EXISTS
(
    -- Tránh nạp trùng nếu ngày đó đã có trong Dim_Time (kể cả bản ghi Unknown)
    SELECT 1 
    FROM dw.Dim_Time t 
    WHERE t.FullDate = d.CalendarDate
)
OPTION (MAXRECURSION 0); -- Cho phép đệ quy > 10000 ngày mà không bị giới hạn
GO

PRINT N'Dim_Time calendar generation completed successfully!';
GO


/* =========================================================
   3. KIỂM TRA TÍNH TOÀN VẸN CỦA DIM_TIME (HEALTH CHECK)
   ========================================================= */

-- 1. Tổng số dòng, ngày bắt đầu, ngày kết thúc
SELECT 
    COUNT(*) AS TotalDays,
    MIN(FullDate) AS MinCalendarDate,
    MAX(FullDate) AS MaxCalendarDate
FROM dw.Dim_Time
WHERE TimeKey <> -1;

-- 2. Thống kê số ngày theo Mùa (Rainy / Dry)
SELECT 
    Season, 
    COUNT(*) AS NumberOfDays 
FROM dw.Dim_Time 
WHERE TimeKey <> -1
GROUP BY Season;

-- 3. Kiểm tra xem ngày sự kiện ngập năm 2026 (Obs_266) đã có trong lịch chưa
SELECT TOP 5 * 
FROM dw.Dim_Time 
WHERE Year = 2026 AND Month = 5 AND Day = 2;
GO