/*
============================================================
Project : Flood Decision Support System (Flood_DSS)
Script  : Seed_Unknown_Members.sql
Owner   : TV4 (Dimension Tables & Dimension ETL)

Purpose :
    Insert default 'Unknown' members (Key = -1) into 5 Dimensions.
    These members represent missing, unmapped, or invalid dimension references
    without leaving foreign keys NULL in Fact tables.

Rules:
    - Bắt buộc dùng SET IDENTITY_INSERT ON / OFF cho các bảng có cột IDENTITY.
    - Dim_Time dùng TimeKey = -1, FullDate = '1900-01-01'.
    - Không vi phạm các ràng buộc UNIQUE, CHECK đã định nghĩa.
============================================================
*/

USE Flood_DSS;
GO

/* =========================================================
   1. UNKNOWN MEMBER - dw.Dim_Time
   (Khóa = -1, Ngày quy ước = 1900-01-01)
   ========================================================= */
IF NOT EXISTS (SELECT 1 FROM dw.Dim_Time WHERE TimeKey = -1)
BEGIN
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
    VALUES
    (
        -1,
        '1900-01-01',
        NULL,
        NULL,
        NULL,
        NULL,
        N'Unknown',
        NULL
    );
    PRINT N'Seeded Unknown into dw.Dim_Time.';
END
ELSE
BEGIN
    PRINT N'Unknown already exists in dw.Dim_Time.';
END;
GO


/* =========================================================
   2. UNKNOWN MEMBER - dw.Dim_Area
   (Khóa = -1, Area_ID = 'UNKNOWN', BoundaryVersion = 'Unknown')
   ========================================================= */
IF NOT EXISTS (SELECT 1 FROM dw.Dim_Area WHERE AreaKey = -1)
BEGIN
    SET IDENTITY_INSERT dw.Dim_Area ON;

    INSERT INTO dw.Dim_Area
    (
        AreaKey,
        Area_ID,
        Area_Name,
        Area_Level,
        ParentArea_ID,
        ParentArea_Name,
        BoundaryVersion,
        Area_km2,
        EffectiveFrom,
        EffectiveTo,
        IsCurrent
    )
    VALUES
    (
        -1,
        N'UNKNOWN',
        N'Chưa xác định',
        N'Chưa xác định',
        NULL,
        NULL,
        N'Unknown',
        NULL,
        NULL,
        NULL,
        1
    );

    SET IDENTITY_INSERT dw.Dim_Area OFF;
    PRINT N'Seeded Unknown into dw.Dim_Area.';
END
ELSE
BEGIN
    PRINT N'Unknown already exists in dw.Dim_Area.';
END;
GO


/* =========================================================
   3. UNKNOWN MEMBER - dw.Dim_Cause
   (Khóa = -1, Cause_Name = 'Unknown')
   ========================================================= */
IF NOT EXISTS (SELECT 1 FROM dw.Dim_Cause WHERE CauseKey = -1)
BEGIN
    SET IDENTITY_INSERT dw.Dim_Cause ON;

    INSERT INTO dw.Dim_Cause
    (
        CauseKey,
        Cause_Name,
        [Description]
    )
    VALUES
    (
        -1,
        N'Unknown',
        N'Nguyên nhân chưa xác định hoặc dữ liệu nguồn bị khuyết'
    );

    SET IDENTITY_INSERT dw.Dim_Cause OFF;
    PRINT N'Seeded Unknown into dw.Dim_Cause.';
END
ELSE
BEGIN
    PRINT N'Unknown already exists in dw.Dim_Cause.';
END;
GO


/* =========================================================
   4. UNKNOWN MEMBER - dw.Dim_Source
   (Khóa = -1, Source_ID = 'UNKNOWN')
   ========================================================= */
IF NOT EXISTS (SELECT 1 FROM dw.Dim_Source WHERE SourceKey = -1)
BEGIN
    SET IDENTITY_INSERT dw.Dim_Source ON;

    INSERT INTO dw.Dim_Source
    (
        SourceKey,
        Source_ID,
        Source_Name,
        Source_Type,
        SourceURL,
        DatasetVersion,
        RetrievedDate
    )
    VALUES
    (
        -1,
        N'UNKNOWN',
        N'Nguồn dữ liệu không xác định',
        N'Unknown',
        NULL,
        NULL,
        NULL
    );

    SET IDENTITY_INSERT dw.Dim_Source OFF;
    PRINT N'Seeded Unknown into dw.Dim_Source.';
END
ELSE
BEGIN
    PRINT N'Unknown already exists in dw.Dim_Source.';
END;
GO


/* =========================================================
   5. UNKNOWN MEMBER - dw.Dim_Location
   (Khóa = -1, Location_ID = 'UNKNOWN', AreaKey = -1)
   ========================================================= */
IF NOT EXISTS (SELECT 1 FROM dw.Dim_Location WHERE LocationKey = -1)
BEGIN
    SET IDENTITY_INSERT dw.Dim_Location ON;

    INSERT INTO dw.Dim_Location
    (
        LocationKey,
        Location_ID,
        Location_Name,
        Location_Type,
        AreaKey,
        Longitude,
        Latitude,
        SpatialPrecision,
        GeocodingMethod,
        DistanceToWater_m,
        NearestWater_ID,
        NearestRoad_Name,
        DistanceToRoad_m
    )
    VALUES
    (
        -1,
        N'UNKNOWN',
        N'Vị trí chưa xác định',
        N'Unknown',
        -1,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL
    );

    SET IDENTITY_INSERT dw.Dim_Location OFF;
    PRINT N'Seeded Unknown into dw.Dim_Location.';
END
ELSE
BEGIN
    PRINT N'Unknown already exists in dw.Dim_Location.';
END;
GO


/* =========================================================
   KIỂM TRA CÁC BẢN GHI UNKNOWN (-1) VỪA TẠO
   ========================================================= */
SELECT 
    'dw.Dim_Time' AS Dimension, 
    TimeKey AS [Key], 
    CAST(FullDate AS NVARCHAR(50)) AS [Identifier], 
    Season AS [Description] 
FROM dw.Dim_Time WHERE TimeKey = -1

UNION ALL

SELECT 
    'dw.Dim_Area', 
    AreaKey, 
    Area_ID, 
    Area_Name 
FROM dw.Dim_Area WHERE AreaKey = -1

UNION ALL

SELECT 
    'dw.Dim_Cause', 
    CauseKey, 
    Cause_Name, 
    [Description] 
FROM dw.Dim_Cause WHERE CauseKey = -1

UNION ALL

SELECT 
    'dw.Dim_Source', 
    SourceKey, 
    Source_ID, 
    Source_Name 
FROM dw.Dim_Source WHERE SourceKey = -1

UNION ALL

SELECT 
    'dw.Dim_Location', 
    LocationKey, 
    Location_ID, 
    Location_Name 
FROM dw.Dim_Location WHERE LocationKey = -1;
GO