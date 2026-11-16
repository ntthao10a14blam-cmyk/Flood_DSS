USE Flood_DSS;
GO

/* 1. KIỂM TRA ĐỘ MỊN (GRAIN) CỦA FACT_POPULATION (AreaKey + Year + SourceKey) */
SELECT COUNT_BIG(*) AS TotalRows,
       (SELECT COUNT_BIG(*) FROM (
           SELECT AreaKey, [Year], SourceKey FROM dw.Fact_Population GROUP BY AreaKey, [Year], SourceKey
       ) AS G) AS UniqueGrainCombinations
FROM dw.Fact_Population;

/* 2. KIỂM TRA ĐỘ MỊN (GRAIN) CỦA FACT_FLOODOBSERVATION (SourceKey + Obs_ID) */
SELECT COUNT_BIG(*) AS TotalRows,
       (SELECT COUNT_BIG(*) FROM (
           SELECT SourceKey, Obs_ID FROM dw.Fact_FloodObservation GROUP BY SourceKey, Obs_ID
       ) AS G) AS UniqueGrainCombinations
FROM dw.Fact_FloodObservation;

/* 3. KIỂM TRA KHÓA GRAIN BỊ NULL HOẶC RỖNG */
SELECT N'Fact_Population' AS FactTable, COUNT_BIG(*) AS InvalidNullRows
FROM dw.Fact_Population WHERE AreaKey IS NULL OR [Year] IS NULL OR SourceKey IS NULL
UNION ALL
SELECT N'Fact_FloodObservation', COUNT_BIG(*)
FROM dw.Fact_FloodObservation WHERE SourceKey IS NULL OR Obs_ID IS NULL OR LTRIM(RTRIM(Obs_ID)) = N'';

/* 4. KIỂM TRA MIỀN GIÁ TRỊ MEASURE BẢNG FACT_POPULATION */
SELECT COUNT_BIG(*) AS TotalRows,
       SUM(CASE WHEN Population < 0 THEN 1 ELSE 0 END) AS NegativePopulation,
       SUM(CASE WHEN Area_km2 IS NOT NULL AND Area_km2 <= 0 THEN 1 ELSE 0 END) AS InvalidArea,
       SUM(CASE WHEN PopulationDensity < 0 THEN 1 ELSE 0 END) AS NegativePopulationDensity
FROM dw.Fact_Population;

/* 5. KIỂM TRA MIỀN GIÁ TRỊ MEASURE BẢNG FACT_FLOODOBSERVATION */
SELECT COUNT_BIG(*) AS TotalRows,
       SUM(CASE WHEN MinDepth_cm < 0 OR MaxDepth_cm < 0
                  OR (MinDepth_cm IS NOT NULL AND MaxDepth_cm IS NOT NULL AND MinDepth_cm > MaxDepth_cm)
                THEN 1 ELSE 0 END) AS InvalidDepth,
       SUM(CASE WHEN MinDepth_cm IS NOT NULL AND MaxDepth_cm IS NOT NULL AND AvgDepth_cm IS NOT NULL
                  AND (AvgDepth_cm < MinDepth_cm OR AvgDepth_cm > MaxDepth_cm)
                THEN 1 ELSE 0 END) AS InvalidAverageDepth,
       SUM(CASE WHEN Duration_hours < 0 THEN 1 ELSE 0 END) AS NegativeDuration,
       SUM(CASE WHEN ObservationCount <> 1 THEN 1 ELSE 0 END) AS InvalidObservationCount
FROM dw.Fact_FloodObservation;
GO
