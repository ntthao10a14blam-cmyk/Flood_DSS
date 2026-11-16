USE Flood_DSS;
GO

/* 1. KIỂM TRA KHÓA NGOẠI BẢNG FACT_FLOODOBSERVATION (5 FK) */
SELECT N'TimeKey' AS ForeignKeyColumn, COUNT_BIG(*) AS InvalidRows
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Time d ON f.TimeKey = d.TimeKey WHERE d.TimeKey IS NULL
UNION ALL
SELECT N'AreaKey', COUNT_BIG(*)
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Area d ON f.AreaKey = d.AreaKey WHERE d.AreaKey IS NULL
UNION ALL
SELECT N'LocationKey', COUNT_BIG(*)
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Location d ON f.LocationKey = d.LocationKey WHERE d.LocationKey IS NULL
UNION ALL
SELECT N'CauseKey', COUNT_BIG(*)
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Cause d ON f.CauseKey = d.CauseKey WHERE d.CauseKey IS NULL
UNION ALL
SELECT N'SourceKey', COUNT_BIG(*)
FROM dw.Fact_FloodObservation f LEFT JOIN dw.Dim_Source d ON f.SourceKey = d.SourceKey WHERE d.SourceKey IS NULL;
GO

/* 2. KIỂM TRA KHÓA NGOẠI BẢNG FACT_POPULATION (2 FK) & DIM_LOCATION (1 FK) */
SELECT N'Fact_Population -> AreaKey' AS RelationshipName, COUNT_BIG(*) AS InvalidRows
FROM dw.Fact_Population f LEFT JOIN dw.Dim_Area d ON f.AreaKey = d.AreaKey WHERE d.AreaKey IS NULL
UNION ALL
SELECT N'Fact_Population -> SourceKey', COUNT_BIG(*)
FROM dw.Fact_Population f LEFT JOIN dw.Dim_Source d ON f.SourceKey = d.SourceKey WHERE d.SourceKey IS NULL
UNION ALL
SELECT N'Dim_Location -> AreaKey', COUNT_BIG(*)
FROM dw.Dim_Location l LEFT JOIN dw.Dim_Area a ON l.AreaKey = a.AreaKey WHERE a.AreaKey IS NULL;
GO

/* 3. KIỂM TRA TRẠNG THÁI CÁC RÀNG BUỘC TRONG SYS.FOREIGN_KEYS */
SELECT OBJECT_SCHEMA_NAME(parent_object_id) AS SchemaName,
       OBJECT_NAME(parent_object_id) AS TableName,
       name AS ConstraintName,
       is_disabled,
       is_not_trusted
FROM sys.foreign_keys
WHERE parent_object_id IN (OBJECT_ID(N'dw.Fact_FloodObservation'), OBJECT_ID(N'dw.Fact_Population'));
GO