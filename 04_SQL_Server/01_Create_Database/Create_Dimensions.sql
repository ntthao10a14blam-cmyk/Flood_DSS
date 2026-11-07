
USE Flood_DSS;
GO

/* ============================================
   1. DIM_AREA
   ============================================ */
IF OBJECT_ID('dw.Dim_Area', 'U') IS NULL
BEGIN
    CREATE TABLE dw.Dim_Area (
        AreaKey INT IDENTITY(1,1) NOT NULL,
        Area_ID NVARCHAR(50) NOT NULL,
        Area_Name NVARCHAR(150) NOT NULL,
        Area_Level NVARCHAR(30) NOT NULL,
        ParentArea_ID NVARCHAR(50) NULL,
        ParentArea_Name NVARCHAR(150) NULL,
        BoundaryVersion NVARCHAR(30) NOT NULL,
        Area_km2 DECIMAL(18,4) NULL,
        EffectiveFrom DATE NULL,
        EffectiveTo DATE NULL,
        IsCurrent BIT NOT NULL
            CONSTRAINT DF_Dim_Area_IsCurrent DEFAULT (1),

        CONSTRAINT PK_Dim_Area
            PRIMARY KEY (AreaKey),

        CONSTRAINT UQ_Dim_Area_Version
            UNIQUE (Area_ID, BoundaryVersion),

        CONSTRAINT CK_Dim_Area_Size
            CHECK (Area_km2 > 0),

        CONSTRAINT CK_Dim_Area_Dates
            CHECK (
                EffectiveFrom IS NULL
                OR EffectiveTo IS NULL
                OR EffectiveFrom <= EffectiveTo
            ),

        CONSTRAINT CK_Dim_Area_Name
            CHECK (LEN(TRIM(Area_Name)) > 0),

        CONSTRAINT CK_Dim_Area_Level
            CHECK (LEN(TRIM(Area_Level)) > 0)
    );

    -- Mỗi Area_ID chỉ có tối đa một phiên bản hiện hành
    CREATE UNIQUE INDEX UX_Dim_Area_Current
    ON dw.Dim_Area (Area_ID)
    WHERE IsCurrent = 1
      AND AreaKey <> -1;
END;
GO

/* ============================================
   2. DIM_CAUSE
   ============================================ */
IF OBJECT_ID('dw.Dim_Cause', 'U') IS NULL
BEGIN
    CREATE TABLE dw.Dim_Cause (
        CauseKey INT IDENTITY(1,1) NOT NULL,
        Cause_Name NVARCHAR(150) NOT NULL,
        Description NVARCHAR(500) NULL,

        CONSTRAINT PK_Dim_Cause
            PRIMARY KEY (CauseKey),

        CONSTRAINT UQ_Dim_Cause_Name
            UNIQUE (Cause_Name),

        CONSTRAINT CK_Dim_Cause_Name
            CHECK (LEN(TRIM(Cause_Name)) > 0)
    );
END;
GO

/* ============================================
   3. DIM_SOURCE
   ============================================ */
IF OBJECT_ID('dw.Dim_Source', 'U') IS NULL
BEGIN
    CREATE TABLE dw.Dim_Source (
        SourceKey INT IDENTITY(1,1) NOT NULL,
        Source_ID NVARCHAR(100) NOT NULL,
        Source_Name NVARCHAR(255) NOT NULL,
        Source_Type NVARCHAR(100) NULL,
        SourceURL NVARCHAR(1000) NULL,
        DatasetVersion NVARCHAR(100) NULL,
        RetrievedDate DATE NULL,

        CONSTRAINT PK_Dim_Source
            PRIMARY KEY (SourceKey),

        CONSTRAINT UQ_Dim_Source_ID
            UNIQUE (Source_ID),

        CONSTRAINT CK_Dim_Source_Name
            CHECK (LEN(TRIM(Source_Name)) > 0)
    );
END;
GO

/* ============================================
   4. DIM_LOCATION
   ============================================ */
IF OBJECT_ID('dw.Dim_Location', 'U') IS NULL
BEGIN
    CREATE TABLE dw.Dim_Location (
        LocationKey INT IDENTITY(1,1) NOT NULL,
        Location_ID NVARCHAR(50) NOT NULL,
        Location_Name NVARCHAR(255) NULL,
        Location_Type NVARCHAR(100) NULL,
        AreaKey INT NOT NULL,
        Latitude DECIMAL(10,7) NULL,
        Longitude DECIMAL(10,7) NULL,
        SpatialPrecision NVARCHAR(100) NULL,
        GeocodingMethod NVARCHAR(100) NULL,
        DistanceToWater_m DECIMAL(14,3) NULL,
        NearestWater_ID NVARCHAR(50) NULL,
        NearestRoad_Name NVARCHAR(150) NULL,
        DistanceToRoad_m DECIMAL(14,3) NULL,

        CONSTRAINT PK_Dim_Location
            PRIMARY KEY (LocationKey),

        CONSTRAINT UQ_Dim_Location_ID
            UNIQUE (Location_ID),

        CONSTRAINT FK_Dim_Location_Area
            FOREIGN KEY (AreaKey)
            REFERENCES dw.Dim_Area(AreaKey),

        CONSTRAINT CK_Dim_Location_Lat
            CHECK (Latitude BETWEEN -90 AND 90),

        CONSTRAINT CK_Dim_Location_Long
            CHECK (Longitude BETWEEN -180 AND 180),

        CONSTRAINT CK_Dim_Location_Water
            CHECK (DistanceToWater_m >= 0),

        CONSTRAINT CK_Dim_Location_Road
            CHECK (DistanceToRoad_m >= 0)
    );
END;
GO

/* ============================================
   5. KIỂM TRA KẾT QUẢ
   ============================================ */
SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'dw'
  AND TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_NAME;
GO
