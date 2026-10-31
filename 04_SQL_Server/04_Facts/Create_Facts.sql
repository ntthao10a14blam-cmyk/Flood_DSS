
/*
============================================================
Project : Flood Decision Support System
Script  : Create_Facts.sql
Owner   : TV5

Purpose:
    Create Fact_FloodObservation and Fact_Population.

Grain:
    Fact_FloodObservation: One row per source observation.
    Fact_Population: One row per area, year and source.

============================================================
*/

USE Flood_DSS;
GO

/* Ensure DW schema exists */
IF SCHEMA_ID(N'dw') IS NULL
    EXEC(N'CREATE SCHEMA dw');
GO

/* =========================================================
   1. FACT FLOOD OBSERVATION
   ========================================================= */

IF OBJECT_ID(N'dw.Fact_FloodObservation', N'U') IS NULL
BEGIN
    CREATE TABLE dw.Fact_FloodObservation
    (
        FloodObservationKey BIGINT IDENTITY(1,1) NOT NULL,
        Obs_ID              NVARCHAR(200) NOT NULL,

        TimeKey             INT NOT NULL,
        AreaKey             INT NOT NULL,
        LocationKey         INT NOT NULL,
        CauseKey            INT NOT NULL,
        SourceKey           INT NOT NULL,

        MinDepth_cm         DECIMAL(10,2) NULL,
        MaxDepth_cm         DECIMAL(10,2) NULL,
        AvgDepth_cm         DECIMAL(10,2) NULL,
        Duration_hours      DECIMAL(10,2) NULL,

        DepthClass          NVARCHAR(100) NULL,
        ImpactType          NVARCHAR(510) NULL,

        ObservationCount    TINYINT NOT NULL
            CONSTRAINT DF_Fact_Flood_ObservationCount DEFAULT (1),

        DataQualityStatus   NVARCHAR(100) NOT NULL,

        CONSTRAINT PK_Fact_FloodObservation
            PRIMARY KEY (FloodObservationKey),

        CONSTRAINT UQ_Fact_FloodObservation_Source_Obs
            UNIQUE (SourceKey, Obs_ID),

        CONSTRAINT FK_Fact_FloodObservation_Time
            FOREIGN KEY (TimeKey)
            REFERENCES dw.Dim_Time(TimeKey),

        CONSTRAINT FK_Fact_FloodObservation_Area
            FOREIGN KEY (AreaKey)
            REFERENCES dw.Dim_Area(AreaKey),

        CONSTRAINT FK_Fact_FloodObservation_Location
            FOREIGN KEY (LocationKey)
            REFERENCES dw.Dim_Location(LocationKey),

        CONSTRAINT FK_Fact_FloodObservation_Cause
            FOREIGN KEY (CauseKey)
            REFERENCES dw.Dim_Cause(CauseKey),

        CONSTRAINT FK_Fact_FloodObservation_Source
            FOREIGN KEY (SourceKey)
            REFERENCES dw.Dim_Source(SourceKey),

        CONSTRAINT CK_Fact_FloodObservation_MinDepth
            CHECK (MinDepth_cm IS NULL OR MinDepth_cm >= 0),

        CONSTRAINT CK_Fact_FloodObservation_MaxDepth
            CHECK (MaxDepth_cm IS NULL OR MaxDepth_cm >= 0),

        CONSTRAINT CK_Fact_FloodObservation_Duration
            CHECK (Duration_hours IS NULL OR Duration_hours >= 0),

        CONSTRAINT CK_Fact_FloodObservation_DepthRange
            CHECK (
                MinDepth_cm IS NULL
                OR MaxDepth_cm IS NULL
                OR MinDepth_cm <= MaxDepth_cm
            ),

        CONSTRAINT CK_Fact_FloodObservation_AvgDepth
            CHECK (
                AvgDepth_cm IS NULL
                OR MinDepth_cm IS NULL
                OR MaxDepth_cm IS NULL
                OR (
                    AvgDepth_cm >= MinDepth_cm
                    AND AvgDepth_cm <= MaxDepth_cm
                )
            ),

        CONSTRAINT CK_Fact_FloodObservation_Count
            CHECK (ObservationCount = 1),

        CONSTRAINT CK_Fact_FloodObservation_ObsID_NotEmpty
            CHECK (LEN(LTRIM(RTRIM(Obs_ID))) > 0)
    );

    PRINT N'Created dw.Fact_FloodObservation';
END
ELSE
    PRINT N'dw.Fact_FloodObservation already exists - skipped';
GO

/* =========================================================
   2. FACT POPULATION
   ========================================================= */

IF OBJECT_ID(N'dw.Fact_Population', N'U') IS NULL
BEGIN
    CREATE TABLE dw.Fact_Population
    (
        PopulationKey       BIGINT IDENTITY(1,1) NOT NULL,

        AreaKey             INT NOT NULL,
        Year                SMALLINT NOT NULL,
        SourceKey           INT NOT NULL,

        Population          BIGINT NULL,
        Area_km2            DECIMAL(18,4) NULL,
        PopulationDensity   DECIMAL(18,3) NULL,

        DataQualityStatus   NVARCHAR(100) NOT NULL,

        CONSTRAINT PK_Fact_Population
            PRIMARY KEY (PopulationKey),

        CONSTRAINT UQ_Fact_Population_Area_Year_Source
            UNIQUE (AreaKey, Year, SourceKey),

        CONSTRAINT FK_Fact_Population_Area
            FOREIGN KEY (AreaKey)
            REFERENCES dw.Dim_Area(AreaKey),

        CONSTRAINT FK_Fact_Population_Source
            FOREIGN KEY (SourceKey)
            REFERENCES dw.Dim_Source(SourceKey),

        CONSTRAINT CK_Fact_Population_Population
            CHECK (Population IS NULL OR Population >= 0),

        CONSTRAINT CK_Fact_Population_Area
            CHECK (Area_km2 IS NULL OR Area_km2 > 0),

        CONSTRAINT CK_Fact_Population_Density
            CHECK (PopulationDensity IS NULL OR PopulationDensity >= 0)
    );

    PRINT N'Created dw.Fact_Population';
END
ELSE
    PRINT N'dw.Fact_Population already exists - skipped';
GO

/* =========================================================
   3. BASIC VALIDATION
   ========================================================= */

SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = N'dw'
  AND TABLE_NAME IN
  (
      N'Fact_FloodObservation',
      N'Fact_Population'
  )
ORDER BY TABLE_NAME;
GO
