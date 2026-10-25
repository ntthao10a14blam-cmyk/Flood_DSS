/*
============================================================
Project : Flood Decision Support System
Script  : Create_Staging_Tables.sql
Owner   : TV1

Purpose:
    Create staging tables used by SSIS.

Design principles:
    - Preserve source data.
    - Allow NULL values.
    - Do not enforce source business IDs as primary keys.
    - Data quality rules are handled by ETL.
============================================================
*/

USE Flood_DSS;
GO


/* =========================================================
   1. STAGING - FLOOD
   ========================================================= */

IF OBJECT_ID(N'stg.Flood', N'U') IS NULL
BEGIN

    CREATE TABLE stg.Flood
    (
        fid                     BIGINT          NULL,
        OBJECTID                BIGINT          NULL,

        Obs_id                  NVARCHAR(100)   NULL,
        [Date]                  DATE            NULL,
        [Year]                  SMALLINT        NULL,

        Location_name           NVARCHAR(500)   NULL,
        Location_type           NVARCHAR(100)   NULL,
        District_mentioned      NVARCHAR(255)   NULL,
        Ward                    NVARCHAR(255)   NULL,
        Current_admin_unit      NVARCHAR(255)   NULL,

        Water_height_max_cm     DECIMAL(10,2)   NULL,
        Depth_class             NVARCHAR(100)   NULL,

        Cause                   NVARCHAR(255)   NULL,
        Impact_type             NVARCHAR(255)   NULL,

        Source_id               NVARCHAR(100)   NULL,
        Source_type             NVARCHAR(100)   NULL,

        Spatial_precision       NVARCHAR(100)   NULL,
        Geocoding_method        NVARCHAR(100)   NULL,
        Observation_notes       NVARCHAR(MAX)   NULL,

        Commune                 NVARCHAR(255)   NULL,
        Province                NVARCHAR(255)   NULL,

        Water_height_min_cm     DECIMAL(10,2)   NULL,
        Duration_hours          DECIMAL(10,2)   NULL,

        Longitude               DECIMAL(15,12)  NULL,
        Latitude                DECIMAL(15,12)  NULL,

        Missing_Date            BIT             NULL,
        Missing_Depth           BIT             NULL,
        Duplicate_Obs_id        BIT             NULL,
        Invalid_Coordinates     BIT             NULL,
        Invalid_Depth_Range     BIT             NULL,
        Year_Date_Mismatch      BIT             NULL,

        Province_Joined         NVARCHAR(255)   NULL
    );

    PRINT N'Created stg.Flood.';

END;
GO

/* =========================================================
   2. STAGING - FLOOD INTEGRATED

   Source:
   Flood_Water_Population_Roads.csv

   Contains:
   Flood + Water + Population + Road matching results
   ========================================================= */

IF OBJECT_ID(N'stg.FloodIntegrated', N'U') IS NULL
BEGIN

    CREATE TABLE stg.FloodIntegrated
    (
        fid                         BIGINT          NULL,
        OBJECTID                    BIGINT          NULL,

        Obs_id                      NVARCHAR(100)   NULL,
        [Date]                      DATE            NULL,
        [Year]                      SMALLINT        NULL,

        Location_name               NVARCHAR(500)   NULL,
        Location_type               NVARCHAR(100)   NULL,
        District_mentioned          NVARCHAR(255)   NULL,
        Ward                        NVARCHAR(255)   NULL,
        Current_admin_unit          NVARCHAR(255)   NULL,

        Water_height_max_cm         DECIMAL(10,2)   NULL,
        Depth_class                 NVARCHAR(100)   NULL,

        Cause                       NVARCHAR(255)   NULL,
        Impact_type                 NVARCHAR(255)   NULL,

        Source_id                   NVARCHAR(100)   NULL,
        Source_type                 NVARCHAR(100)   NULL,

        Spatial_precision           NVARCHAR(100)   NULL,
        Geocoding_method            NVARCHAR(100)   NULL,
        Observation_notes           NVARCHAR(MAX)   NULL,

        Commune                     NVARCHAR(255)   NULL,
        Province                    NVARCHAR(255)   NULL,

        Water_height_min_cm         DECIMAL(10,2)   NULL,
        Duration_hours              DECIMAL(10,2)   NULL,

        Longitude                   DECIMAL(15,12)  NULL,
        Latitude                    DECIMAL(15,12)  NULL,

        Missing_Date                BIT             NULL,
        Missing_Depth               BIT             NULL,
        Duplicate_Obs_id            BIT             NULL,
        Invalid_Coordinates         BIT             NULL,
        Invalid_Depth_Range         BIT             NULL,
        Year_Date_Mismatch          BIT             NULL,

        Province_Joined             NVARCHAR(255)   NULL,

        /* Water integration */
        Water_ID                    NVARCHAR(100)   NULL,
        DistanceToWater_m           DECIMAL(18,6)   NULL,

        /* Population integration */
        Population_Area_ID          NVARCHAR(50)    NULL,
        Population_Area_Name        NVARCHAR(150)   NULL,
        Population_ReferenceYear    SMALLINT        NULL,
        Population_BoundaryVersion  NVARCHAR(30)    NULL,
        Population_2019             BIGINT          NULL,
        Population_Area_km2         DECIMAL(18,4)   NULL,
        PopulationDensity_2019      DECIMAL(18,6)   NULL,
        Population_Join_Status      NVARCHAR(100)   NULL,

        /* Area matching */
        Nearest_Area_ID             NVARCHAR(50)    NULL,
        DistanceToNearestDistrict_m DECIMAL(18,6)   NULL,
        Population_Review_Note      NVARCHAR(MAX)   NULL,

        /* Road integration */
        Nearest_Road_ID             NVARCHAR(100)   NULL,
        Nearest_Road_Name           NVARCHAR(255)   NULL,
        Nearest_Road_Mentioned_Years INT            NULL,
        DistanceToNearestRoad_m     DECIMAL(18,6)   NULL,
        Road_Distance_Band          NVARCHAR(50)    NULL,
        Road_Match_Status           NVARCHAR(100)   NULL
    );

    PRINT N'Created stg.FloodIntegrated.';

END;
GO

/* =========================================================
   3. STAGING - POPULATION
   ========================================================= */

IF OBJECT_ID(N'stg.Population', N'U') IS NULL
BEGIN

    CREATE TABLE stg.Population
    (
        OBJECTID           BIGINT          NULL,
        Area_ID            NVARCHAR(50)    NULL,
        Area_Name          NVARCHAR(150)   NULL,
        [Year]             SMALLINT        NULL,
        BoundaryVersion    NVARCHAR(30)    NULL,

        Population         BIGINT          NULL,
        Area_km2           DECIMAL(18,4)   NULL,
        PopulationDensity  DECIMAL(18,6)   NULL,

        Source_ID          NVARCHAR(100)   NULL
    );

    PRINT N'Created stg.Population.';

END;
GO

/* =========================================================
   4. STAGING - ROADS

   Source columns:
   Road_ID
   Road_Name
   Mentioned_Years
   Source_ID
   ========================================================= */

IF OBJECT_ID(N'stg.Roads', N'U') IS NULL
BEGIN

    CREATE TABLE stg.Roads
    (
        Road_ID          NVARCHAR(100)   NULL,
        Road_Name        NVARCHAR(255)   NULL,
        Mentioned_Years  INT             NULL,
        Source_ID        NVARCHAR(100)   NULL
    );

    PRINT N'Created stg.Roads.';

END;
GO

/* =========================================================
   5. STAGING - AREA
   ========================================================= */

IF OBJECT_ID(N'stg.Area', N'U') IS NULL
BEGIN

    CREATE TABLE stg.Area
    (
        Area_ID          NVARCHAR(50)   NULL,
        Area_Name        NVARCHAR(150)  NULL,
        Area_Level       NVARCHAR(30)   NULL,

        ParentArea_ID    NVARCHAR(50)   NULL,
        ParentArea_Name  NVARCHAR(150)  NULL,

        BoundaryVersion  NVARCHAR(30)   NULL,
        Area_km2         DECIMAL(18,4)  NULL,

        EffectiveFrom    DATE           NULL,
        EffectiveTo      DATE           NULL
    );

    PRINT N'Created stg.Area.';

END;
GO

/* =========================================================
   VALIDATION
   ========================================================= */

SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'stg'
  AND TABLE_NAME IN
  (
      'Flood',
      'FloodIntegrated',
      'Population',
      'Roads',
      'Area'
  )
ORDER BY TABLE_NAME;
GO

