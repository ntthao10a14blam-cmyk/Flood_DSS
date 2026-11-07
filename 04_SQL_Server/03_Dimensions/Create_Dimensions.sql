/*
============================================================
Project : Flood Decision Support System (Flood_DSS)
Script  : Create_Dimensions.sql
Owner   : TV4 (Dimension Tables & Dimension ETL)

Purpose :
    Create 5 Dimension tables in schema 'dw':
    1. dw.Dim_Time      - Chiều thời gian (Grain: Ngày)
    2. dw.Dim_Area      - Chiều khu vực hành chính (Grain: Khu vực x Phiên bản địa giới)
    3. dw.Dim_Cause     - Chiều nguyên nhân ngập (SCD Type 1)
    4. dw.Dim_Source    - Chiều nguồn dữ liệu (SCD Type 1)
    5. dw.Dim_Location  - Chiều vị trí ngập (FK tham chiếu dw.Dim_Area)

Rules:
    - PK sử dụng Surrogate Key (SK) tự tăng IDENTITY, riêng Dim_Time dùng YYYYMMDD.
    - Duy trì Business Key / Natural Key với ràng buộc UNIQUE.
    - Ràng buộc CHECK cho phép NULL để phục vụ nạp bản ghi Unknown (-1).
============================================================
*/

USE Flood_DSS;
GO

-- Đảm bảo schema 'dw' đã tồn tại
IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = N'dw')
BEGIN
    EXEC('CREATE SCHEMA dw');
    PRINT N'Created schema dw.';
END;
GO

/* =========================================================
   1. DIMENSION - TIME (Chiều thời gian)
   ========================================================= */
IF OBJECT_ID(N'dw.Dim_Time', N'U') IS NULL
BEGIN
    CREATE TABLE dw.Dim_Time
    (
        TimeKey         INT             NOT NULL,
        FullDate        DATE            NOT NULL,
        [Day]           TINYINT         NULL,
        [Month]         TINYINT         NULL,
        [Quarter]       TINYINT         NULL,
        [Year]          SMALLINT        NULL,
        Season          NVARCHAR(30)    NULL,
        DayOfWeek       TINYINT         NULL,

        CONSTRAINT PK_Dim_Time 
            PRIMARY KEY (TimeKey),

        CONSTRAINT UQ_Dim_Time_FullDate 
            UNIQUE (FullDate),

        CONSTRAINT CK_Dim_Time_Day 
            CHECK ([Day] IS NULL OR [Day] BETWEEN 1 AND 31),

        CONSTRAINT CK_Dim_Time_Month 
            CHECK ([Month] IS NULL OR [Month] BETWEEN 1 AND 12),

        CONSTRAINT CK_Dim_Time_Quarter 
            CHECK ([Quarter] IS NULL OR [Quarter] BETWEEN 1 AND 4),

        CONSTRAINT CK_Dim_Time_DayOfWeek 
            CHECK (DayOfWeek IS NULL OR DayOfWeek BETWEEN 1 AND 7)
    );
    PRINT N'Created dw.Dim_Time.';
END;
GO

/* =========================================================
   2. DIMENSION - AREA (Chiều khu vực hành chính)
   Nguồn: stg.Area (Area_Boundaries_Clean.csv)
   ========================================================= */
IF OBJECT_ID(N'dw.Dim_Area', N'U') IS NULL
BEGIN
    CREATE TABLE dw.Dim_Area
    (
        AreaKey             INT IDENTITY(1,1)   NOT NULL,
        Area_ID             NVARCHAR(50)        NOT NULL,
        Area_Name           NVARCHAR(150)       NOT NULL,
        Area_Level          NVARCHAR(30)        NOT NULL,
        ParentArea_ID       NVARCHAR(50)        NULL,
        ParentArea_Name     NVARCHAR(150)       NULL,
        BoundaryVersion     NVARCHAR(30)        NOT NULL,
        Area_km2            DECIMAL(18,4)       NULL,
        EffectiveFrom       DATE                NULL,
        EffectiveTo         DATE                NULL,
        IsCurrent           BIT DEFAULT 1       NOT NULL,

        CONSTRAINT PK_Dim_Area 
            PRIMARY KEY (AreaKey),

        -- Khóa duy nhất ghép theo tài liệu thiết kế: (Area_ID, BoundaryVersion)
        CONSTRAINT UQ_Dim_Area_NaturalKey 
            UNIQUE (Area_ID, BoundaryVersion),

        CONSTRAINT CK_Dim_Area_km2 
            CHECK (Area_km2 IS NULL OR Area_km2 > 0),

        CONSTRAINT CK_Dim_Area_Dates 
            CHECK (EffectiveFrom IS NULL OR EffectiveTo IS NULL OR EffectiveFrom <= EffectiveTo),

        CONSTRAINT CK_Dim_Area_IsCurrent 
            CHECK (IsCurrent IN (0, 1))
    );
    PRINT N'Created dw.Dim_Area.';
END;
GO

/* =========================================================
   3. DIMENSION - CAUSE (Chiều nguyên nhân ngập)
   Nguồn: stg.Flood (Cột Cause)
   ========================================================= */
IF OBJECT_ID(N'dw.Dim_Cause', N'U') IS NULL
BEGIN
    CREATE TABLE dw.Dim_Cause
    (
        CauseKey        INT IDENTITY(1,1)   NOT NULL,
        Cause_Name      NVARCHAR(150)       NOT NULL,
        [Description]   NVARCHAR(500)       NULL,

        CONSTRAINT PK_Dim_Cause 
            PRIMARY KEY (CauseKey),

        CONSTRAINT UQ_Dim_Cause_Name 
            UNIQUE (Cause_Name)
    );
    PRINT N'Created dw.Dim_Cause.';
END;
GO

/* =========================================================
   4. DIMENSION - SOURCE (Chiều nguồn dữ liệu)
   Nguồn: stg.Flood, stg.Population, stg.Roads (Source_ID, Source_Type)
   ========================================================= */
IF OBJECT_ID(N'dw.Dim_Source', N'U') IS NULL
BEGIN
    CREATE TABLE dw.Dim_Source
    (
        SourceKey           INT IDENTITY(1,1)   NOT NULL,
        Source_ID           NVARCHAR(100)       NOT NULL,
        Source_Name         NVARCHAR(255)       NOT NULL,
        Source_Type         NVARCHAR(100)       NULL,
        SourceURL           NVARCHAR(1000)      NULL,
        DatasetVersion      NVARCHAR(100)       NULL,
        RetrievedDate       DATE                NULL,

        CONSTRAINT PK_Dim_Source 
            PRIMARY KEY (SourceKey),

        CONSTRAINT UQ_Dim_Source_ID 
            UNIQUE (Source_ID)
    );
    PRINT N'Created dw.Dim_Source.';
END;
GO

/* =========================================================
   5. DIMENSION - LOCATION (Chiều vị trí ngập)
   Nguồn: stg.Flood & stg.FloodIntegrated
   Phụ thuộc: Cần khóa ngoại AreaKey sang dw.Dim_Area
   ========================================================= */
IF OBJECT_ID(N'dw.Dim_Location', N'U') IS NULL
BEGIN
    CREATE TABLE dw.Dim_Location
    (
        LocationKey             INT IDENTITY(1,1)   NOT NULL,
        Location_ID             NVARCHAR(50)        NOT NULL,
        Location_Name           NVARCHAR(500)       NULL,
        Location_Type           NVARCHAR(100)       NULL,
        AreaKey                 INT                 NOT NULL,
        
        -- Khớp với kiểu DECIMAL(15,12) trong stg.Flood để không mất độ chính xác GIS
        Longitude               DECIMAL(15,12)      NULL,
        Latitude                DECIMAL(15,12)      NULL,
        
        SpatialPrecision        NVARCHAR(100)       NULL,
        GeocodingMethod         NVARCHAR(100)       NULL,
        
        -- Khớp với kiểu khoảng cách trong stg.FloodIntegrated
        DistanceToWater_m       DECIMAL(18,6)       NULL,
        NearestWater_ID         NVARCHAR(100)       NULL,
        NearestRoad_Name        NVARCHAR(255)       NULL,
        DistanceToRoad_m        DECIMAL(18,6)       NULL,

        CONSTRAINT PK_Dim_Location 
            PRIMARY KEY (LocationKey),

        CONSTRAINT UQ_Dim_Location_ID 
            UNIQUE (Location_ID),

        CONSTRAINT FK_Dim_Location_Area 
            FOREIGN KEY (AreaKey) REFERENCES dw.Dim_Area(AreaKey),

        CONSTRAINT CK_Dim_Location_Latitude 
            CHECK (Latitude IS NULL OR (Latitude BETWEEN -90 AND 90)),

        CONSTRAINT CK_Dim_Location_Longitude 
            CHECK (Longitude IS NULL OR (Longitude BETWEEN -180 AND 180)),

        CONSTRAINT CK_Dim_Location_DistanceWater 
            CHECK (DistanceToWater_m IS NULL OR DistanceToWater_m >= 0),

        CONSTRAINT CK_Dim_Location_DistanceRoad 
            CHECK (DistanceToRoad_m IS NULL OR DistanceToRoad_m >= 0)
    );
    PRINT N'Created dw.Dim_Location.';
END;
GO

/* =========================================================
   KIỂM TRA CẤU TRÚC 5 BẢNG ĐÃ TẠO
   ========================================================= */
SELECT 
    TABLE_SCHEMA, 
    TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_SCHEMA = 'dw' 
  AND TABLE_NAME IN ('Dim_Time', 'Dim_Area', 'Dim_Cause', 'Dim_Source', 'Dim_Location')
ORDER BY TABLE_NAME;
GO