USE Flood_DSS;
GO


/* =========================================================
   TEST 1 - SCHEMAS
   ========================================================= */

SELECT
    name AS SchemaName
FROM sys.schemas
WHERE name IN ('stg', 'dw', 'mart', 'dss')
ORDER BY name;
GO


/* =========================================================
   TEST 2 - TV1 TABLES
   ========================================================= */

SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE
       (TABLE_SCHEMA = 'stg'
        AND TABLE_NAME IN
        (
            'Flood',
            'FloodIntegrated',
            'Population',
            'Roads',
            'Area',
            'ETL_Log',
            'ETL_Error'
        ))
    OR
       (TABLE_SCHEMA = 'dw'
        AND TABLE_NAME = 'Dim_Time')
ORDER BY
    TABLE_SCHEMA,
    TABLE_NAME;
GO


/* =========================================================
   TEST 3 - STAGING COLUMN DEFINITIONS
   ========================================================= */

SELECT
    TABLE_NAME,
    ORDINAL_POSITION,
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    NUMERIC_PRECISION,
    NUMERIC_SCALE,
    IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'stg'
ORDER BY
    TABLE_NAME,
    ORDINAL_POSITION;
GO


/* =========================================================
   TEST 4 - DIM_TIME
   ========================================================= */

SELECT
    COUNT(*) AS TotalTimeRows,
    MIN(FullDate) AS MinDate,
    MAX(FullDate) AS MaxDate
FROM dw.Dim_Time;
GO


/* =========================================================
   TEST 5 - UNKNOWN TIME MEMBER
   ========================================================= */

SELECT *
FROM dw.Dim_Time
WHERE TimeKey = -1;
GO

