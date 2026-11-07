USE Flood_DSS;
GO

SET NOCOUNT ON;
GO

/* 1. THONG KE SO DONG HAI BANG FACT */
SELECT
    N'dw.Fact_FloodObservation' AS TableName,
    COUNT_BIG(*) AS TotalRows
FROM dw.Fact_FloodObservation

UNION ALL

SELECT
    N'dw.Fact_Population',
    COUNT_BIG(*)
FROM dw.Fact_Population;
GO

/* 2. KIEM TRA KHOA NGOAI FACT_FLOODOBSERVATION */
SELECT
    N'TimeKey' AS ForeignKeyColumn,
    COUNT_BIG(*) AS InvalidRows
FROM dw.Fact_FloodObservation f
LEFT JOIN dw.Dim_Time d ON f.TimeKey = d.TimeKey
WHERE d.TimeKey IS NULL

UNION ALL

SELECT
    N'AreaKey',
    COUNT_BIG(*)
FROM dw.Fact_FloodObservation f
LEFT JOIN dw.Dim_Area d ON f.AreaKey = d.AreaKey
WHERE d.AreaKey IS NULL

UNION ALL

SELECT
    N'LocationKey',
    COUNT_BIG(*)
FROM dw.Fact_FloodObservation f
LEFT JOIN dw.Dim_Location d ON f.LocationKey = d.LocationKey
WHERE d.LocationKey IS NULL

UNION ALL

SELECT
    N'CauseKey',
    COUNT_BIG(*)
FROM dw.Fact_FloodObservation f
LEFT JOIN dw.Dim_Cause d ON f.CauseKey = d.CauseKey
WHERE d.CauseKey IS NULL

UNION ALL

SELECT
    N'SourceKey',
    COUNT_BIG(*)
FROM dw.Fact_FloodObservation f
LEFT JOIN dw.Dim_Source d ON f.SourceKey = d.SourceKey
WHERE d.SourceKey IS NULL;
GO

/* 3. KIEM TRA KHOA NGOAI FACT_POPULATION */
SELECT
    N'AreaKey' AS ForeignKeyColumn,
    COUNT_BIG(*) AS InvalidRows
FROM dw.Fact_Population f
LEFT JOIN dw.Dim_Area d ON f.AreaKey = d.AreaKey
WHERE d.AreaKey IS NULL

UNION ALL

SELECT
    N'SourceKey',
    COUNT_BIG(*)
FROM dw.Fact_Population f
LEFT JOIN dw.Dim_Source d ON f.SourceKey = d.SourceKey
WHERE d.SourceKey IS NULL;
GO

/* 4. KIEM TRA KHOA NGOAI CUA DIM_LOCATION */
SELECT
    COUNT_BIG(*) AS InvalidLocationAreaKeys
FROM dw.Dim_Location l
LEFT JOIN dw.Dim_Area a ON l.AreaKey = a.AreaKey
WHERE a.AreaKey IS NULL;
GO

/* 5. KIEM TRA TRANG THAI CAC RANG BUOC */
SELECT
    OBJECT_SCHEMA_NAME(parent_object_id) AS SchemaName,
    OBJECT_NAME(parent_object_id) AS TableName,
    name AS ConstraintName,
    type_desc AS ConstraintType,
    is_disabled,
    is_not_trusted
FROM sys.foreign_keys
WHERE parent_object_id IN (
    OBJECT_ID(N'dw.Fact_FloodObservation'),
    OBJECT_ID(N'dw.Fact_Population')
);
GO