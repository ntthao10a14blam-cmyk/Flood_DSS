
/*
============================================================
Project : Flood Decision Support System
Script  : Create_Facts.sql
Owner   : TV5

Purpose:
    Create Fact_FloodObservation and Fact_Population.

Note:
    Dimension keys must be checked against TV4's final schema.
============================================================
*/

USE Flood_DSS;
GO

/* Ensure the data warehouse schema exists */
IF SCHEMA_ID(N'dw') IS NULL
    EXEC(N'CREATE SCHEMA dw');
GO

/* =========================================================
   1. FACT FLOOD OBSERVATION
   Grain: One row per flood observation.
   ========================================================= */

IF OBJECT_ID(N'dw.Fact_FloodObservation', N'U') IS NULL
BEGIN
    CREATE TABLE dw.Fact_FloodObservation
    (
        FloodObservationKey BIGINT IDENTITY(1,1) NOT NULL,

        -- Dimension keys; confirm with TV4
        TimeKey             INT NULL,
        AreaKey             INT NULL,
        LocationKey         INT NULL,
        CauseKey            INT NULL,
        SourceKey           INT NULL,

        -- Original source identifiers
        Obs_id              NVARCHAR(100) NULL,
        fid                 BIGINT NULL,
        OBJECTID            BIGINT NULL,

        -- Flood measurements
        WaterHeightMax_cm   DECIMAL(10,2) NULL,
        WaterHeightMin_cm   DECIMAL(10,2) NULL,
        Duration_hours      DECIMAL(10,2) NULL,

        -- Spatial context
        DistanceToWater_m   DECIMAL(18,6) NULL,
        DistanceToRoad_m    DECIMAL(18,6) NULL,

        CONSTRAINT PK_Fact_FloodObservation
            PRIMARY KEY (FloodObservationKey),

        CONSTRAINT CK_Fact_Flood_MaxHeight
            CHECK (WaterHeightMax_cm IS NULL
                   OR WaterHeightMax_cm >= 0),

        CONSTRAINT CK_Fact_Flood_MinHeight
            CHECK (WaterHeightMin_cm IS NULL
                   OR WaterHeightMin_cm >= 0),

        CONSTRAINT CK_Fact_Flood_Duration
            CHECK (Duration_hours IS NULL
                   OR Duration_hours >= 0)
    );

    PRINT N'Created dw.Fact_FloodObservation';
END;
GO

/* =========================================================
   2. FACT POPULATION
   Grain: One row per area, year and boundary version.
   ========================================================= */

IF OBJECT_ID(N'dw.Fact_Population', N'U') IS NULL
BEGIN
    CREATE TABLE dw.Fact_Population
    (
        PopulationFactKey BIGINT IDENTITY(1,1) NOT NULL,

        -- Dimension keys; confirm with TV4
        TimeKey           INT NULL,
        AreaKey           INT NULL,
        SourceKey         INT NULL,

        -- Original source identifiers
        Area_ID           NVARCHAR(50) NULL,
        BoundaryVersion   NVARCHAR(30) NULL,

        -- Population measurements
        Population        BIGINT NULL,
        Area_km2          DECIMAL(18,4) NULL,
        PopulationDensity DECIMAL(18,6) NULL,

        CONSTRAINT PK_Fact_Population
            PRIMARY KEY (PopulationFactKey),

        CONSTRAINT CK_Fact_Population_Count
            CHECK (Population IS NULL OR Population >= 0),

        CONSTRAINT CK_Fact_Population_Area
            CHECK (Area_km2 IS NULL OR Area_km2 >= 0),

        CONSTRAINT CK_Fact_Population_Density
            CHECK (PopulationDensity IS NULL
                   OR PopulationDensity >= 0)
    );

    PRINT N'Created dw.Fact_Population';
END;
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
