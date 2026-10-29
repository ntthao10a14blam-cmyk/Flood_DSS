/*
============================================================
Project : Flood Decision Support System (Flood_DSS)
Script  : Validate_Dimensions.sql
Owner   : TV4 (Dimension Tables & Dimension ETL)

Purpose :
    Kiểm tra toàn bộ 5 bảng Dimension sau khi hoàn tất ETL:
    1. Kiểm tra bản ghi Unknown (-1) tồn tại đủ.
    2. Kiểm tra số dòng thực tế theo kỳ vọng.
    3. Kiểm tra không có NULL ở cột khóa tự nhiên.
    4. Kiểm tra tính toàn vẹn khóa ngoại (FK) Dim_Location -> Dim_Area.
    5. Kiểm tra không có trùng lặp khóa tự nhiên.
============================================================
*/

USE Flood_DSS;
GO

PRINT N'============================================================';
PRINT N'VALIDATE DIMENSIONS - Flood_DSS';
PRINT N'Thời gian chạy: ' + CONVERT(NVARCHAR(30), GETDATE(), 120);
PRINT N'============================================================';
GO

/* =========================================================
   PHẦN 1: KIỂM TRA BẢN GHI UNKNOWN (-1)
   Kỳ vọng: Mỗi bảng phải có đúng 1 dòng với Key = -1
   ========================================================= */
PRINT N'';
PRINT N'--- PHẦN 1: Kiểm tra bản ghi Unknown (Key = -1) ---';

SELECT
    'dw.Dim_Time'    AS Dimension,
    TimeKey          AS [Key],
    CAST(FullDate AS NVARCHAR(50)) AS Identifier,
    Season           AS [Description],
    CASE WHEN TimeKey = -1 THEN N'OK' ELSE N'MISSING' END AS [Status]
FROM dw.Dim_Time WHERE TimeKey = -1

UNION ALL

SELECT
    'dw.Dim_Area',
    AreaKey,
    Area_ID,
    Area_Name,
    CASE WHEN AreaKey = -1 THEN N'OK' ELSE N'MISSING' END
FROM dw.Dim_Area WHERE AreaKey = -1

UNION ALL

SELECT
    'dw.Dim_Cause',
    CauseKey,
    Cause_Name,
    [Description],
    CASE WHEN CauseKey = -1 THEN N'OK' ELSE N'MISSING' END
FROM dw.Dim_Cause WHERE CauseKey = -1

UNION ALL

SELECT
    'dw.Dim_Source',
    SourceKey,
    Source_ID,
    Source_Name,
    CASE WHEN SourceKey = -1 THEN N'OK' ELSE N'MISSING' END
FROM dw.Dim_Source WHERE SourceKey = -1

UNION ALL

SELECT
    'dw.Dim_Location',
    LocationKey,
    Location_ID,
    Location_Name,
    CASE WHEN LocationKey = -1 THEN N'OK' ELSE N'MISSING' END
FROM dw.Dim_Location WHERE LocationKey = -1;
GO

/* =========================================================
   PHẦN 2: KIỂM TRA SỐ DÒNG THỰC TẾ
   Kỳ vọng:
     Dim_Time     >= 11,323 dòng (2000-01-01 -> 2030-12-31) + 1 Unknown
     Dim_Area     = 25 dòng (24 quận/huyện + 1 Unknown)
     Dim_Cause    = 4 dòng  (3 nguyên nhân + 1 Unknown)
     Dim_Source   = 54 dòng (53 nguồn + 1 Unknown)
     Dim_Location = 425 dòng (424 vị trí + 1 Unknown)
   ========================================================= */
PRINT N'';
PRINT N'--- PHẦN 2: Kiểm tra số dòng ---';

SELECT
    Dimension,
    TotalRows,
    Expected,
    CASE WHEN TotalRows >= Expected THEN N'OK' ELSE N'THIẾU DỮ LIỆU' END AS [Status]
FROM (
    SELECT 'dw.Dim_Time'     AS Dimension, COUNT(*) AS TotalRows, 11324 AS Expected FROM dw.Dim_Time
    UNION ALL
    SELECT 'dw.Dim_Area',     COUNT(*), 25  FROM dw.Dim_Area
    UNION ALL
    SELECT 'dw.Dim_Cause',    COUNT(*), 4   FROM dw.Dim_Cause
    UNION ALL
    SELECT 'dw.Dim_Source',   COUNT(*), 54  FROM dw.Dim_Source
    UNION ALL
    SELECT 'dw.Dim_Location', COUNT(*), 425 FROM dw.Dim_Location
) t;
GO

/* =========================================================
   PHẦN 3: KIỂM TRA NULL Ở CỘT KHÓA TỰ NHIÊN
   Kỳ vọng: 0 dòng NULL ở các cột định danh chính
   ========================================================= */
PRINT N'';
PRINT N'--- PHẦN 3: Kiểm tra NULL ở cột định danh chính ---';

SELECT
    Dimension,
    NullCount,
    CASE WHEN NullCount = 0 THEN N'OK' ELSE N'CÓ NULL - CẦN KIỂM TRA' END AS [Status]
FROM (
    SELECT 'dw.Dim_Time    -> FullDate'       AS Dimension, COUNT(*) AS NullCount FROM dw.Dim_Time     WHERE FullDate IS NULL AND TimeKey <> -1
    UNION ALL
    SELECT 'dw.Dim_Area    -> Area_ID',        COUNT(*) FROM dw.Dim_Area     WHERE Area_ID IS NULL AND AreaKey <> -1
    UNION ALL
    SELECT 'dw.Dim_Cause   -> Cause_Name',     COUNT(*) FROM dw.Dim_Cause    WHERE Cause_Name IS NULL AND CauseKey <> -1
    UNION ALL
    SELECT 'dw.Dim_Source  -> Source_ID',      COUNT(*) FROM dw.Dim_Source   WHERE Source_ID IS NULL AND SourceKey <> -1
    UNION ALL
    SELECT 'dw.Dim_Location-> Location_ID',    COUNT(*) FROM dw.Dim_Location WHERE Location_ID IS NULL AND LocationKey <> -1
) t;
GO

/* =========================================================
   PHẦN 4: KIỂM TRA TÍNH TOÀN VẸN KHÓA NGOẠI
   Kỳ vọng: Tất cả AreaKey trong Dim_Location phải tồn tại
             trong Dim_Area (kể cả -1)
   ========================================================= */
PRINT N'';
PRINT N'--- PHẦN 4: Kiểm tra FK Dim_Location -> Dim_Area ---';

SELECT
    CASE
        WHEN COUNT(*) = 0 THEN N'OK - Tất cả AreaKey hợp lệ'
        ELSE N'LỖI FK - ' + CAST(COUNT(*) AS NVARCHAR(10)) + N' dòng có AreaKey không hợp lệ'
    END AS [FK_Status],
    COUNT(*) AS InvalidCount
FROM dw.Dim_Location loc
WHERE NOT EXISTS (
    SELECT 1 FROM dw.Dim_Area a WHERE a.AreaKey = loc.AreaKey
);
GO

/* =========================================================
   PHẦN 5: KIỂM TRA KHÔNG CÓ TRÙNG LẶP KHÓA TỰ NHIÊN
   Kỳ vọng: 0 bộ trùng lặp trong mỗi bảng
   ========================================================= */
PRINT N'';
PRINT N'--- PHẦN 5: Kiểm tra trùng lặp khóa tự nhiên ---';

SELECT Dimension, DuplicateGroups,
    CASE WHEN DuplicateGroups = 0 THEN N'OK' ELSE N'CÓ TRÙNG LẶP' END AS [Status]
FROM (
    -- Dim_Area: Natural Key = Area_ID + BoundaryVersion
    SELECT 'dw.Dim_Area (Area_ID, BoundaryVersion)' AS Dimension,
        COUNT(*) AS DuplicateGroups
    FROM (
        SELECT Area_ID, BoundaryVersion, COUNT(*) AS cnt
        FROM dw.Dim_Area WHERE AreaKey <> -1
        GROUP BY Area_ID, BoundaryVersion HAVING COUNT(*) > 1
    ) x

    UNION ALL

    -- Dim_Cause: Natural Key = Cause_Name
    SELECT 'dw.Dim_Cause (Cause_Name)',
        COUNT(*)
    FROM (
        SELECT Cause_Name, COUNT(*) AS cnt
        FROM dw.Dim_Cause WHERE CauseKey <> -1
        GROUP BY Cause_Name HAVING COUNT(*) > 1
    ) x

    UNION ALL

    -- Dim_Source: Natural Key = Source_ID
    SELECT 'dw.Dim_Source (Source_ID)',
        COUNT(*)
    FROM (
        SELECT Source_ID, COUNT(*) AS cnt
        FROM dw.Dim_Source WHERE SourceKey <> -1
        GROUP BY Source_ID HAVING COUNT(*) > 1
    ) x

    UNION ALL

    -- Dim_Location: Natural Key = Location_ID
    SELECT 'dw.Dim_Location (Location_ID)',
        COUNT(*)
    FROM (
        SELECT Location_ID, COUNT(*) AS cnt
        FROM dw.Dim_Location WHERE LocationKey <> -1
        GROUP BY Location_ID HAVING COUNT(*) > 1
    ) x
) t;
GO

/* =========================================================
   PHẦN 6: THỐNG KÊ NHANH DIM_LOCATION
   Phân tích AreaKey = -1 (chưa khớp quận/huyện)
   ========================================================= */
PRINT N'';
PRINT N'--- PHẦN 6: Thống kê Dim_Location theo AreaKey ---';

SELECT
    CASE WHEN loc.AreaKey = -1 THEN N'Unknown (chưa khớp)' ELSE a.Area_Name END AS Area_Name,
    COUNT(*) AS SoViTri
FROM dw.Dim_Location loc
LEFT JOIN dw.Dim_Area a ON loc.AreaKey = a.AreaKey
WHERE loc.LocationKey <> -1
GROUP BY loc.AreaKey, a.Area_Name
ORDER BY SoViTri DESC;
GO

PRINT N'';
PRINT N'============================================================';
PRINT N'VALIDATE DIMENSIONS HOÀN TẤT';
PRINT N'============================================================';
GO
