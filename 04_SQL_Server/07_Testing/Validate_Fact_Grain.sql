USE Flood_DSS;
GO

SET NOCOUNT ON;
GO

/* 1. KIEM TRA GRAIN FACT_POPULATION */
/* Grain: AreaKey + Year + SourceKey */

SELECT
    AreaKey,
    [Year],
    SourceKey,
    COUNT_BIG(*) AS DuplicateCount
FROM dw.Fact_Population
GROUP BY AreaKey, [Year], SourceKey
HAVING COUNT_BIG(*) > 1;
GO

SELECT
    COUNT_BIG(*) AS TotalRows,
    (
        SELECT COUNT_BIG(*)
        FROM (
            SELECT AreaKey, [Year], SourceKey
            FROM dw.Fact_Population
            GROUP BY AreaKey, [Year], SourceKey
        ) AS G
    ) AS UniqueGrainCombinations
FROM dw.Fact_Population;
GO

/* 2. KIEM TRA GRAIN FACT_FLOODOBSERVATION */
/* Grain: SourceKey + Obs_ID */

SELECT
    SourceKey,
    Obs_ID,
    COUNT_BIG(*) AS DuplicateCount
FROM dw.Fact_FloodObservation
GROUP BY SourceKey, Obs_ID
HAVING COUNT_BIG(*) > 1;
GO

SELECT
    COUNT_BIG(*) AS TotalRows,
    (
        SELECT COUNT_BIG(*)
        FROM (
            SELECT SourceKey, Obs_ID
            FROM dw.Fact_FloodObservation
            GROUP BY SourceKey, Obs_ID
        ) AS G
    ) AS UniqueGrainCombinations
FROM dw.Fact_FloodObservation;
GO

/* 3. KIEM TRA KHOA GRAIN NULL */

SELECT
    N'Fact_Population' AS FactTable,
    COUNT_BIG(*) AS InvalidRows
FROM dw.Fact_Population
WHERE AreaKey IS NULL
   OR [Year] IS NULL
   OR SourceKey IS NULL

UNION ALL

SELECT
    N'Fact_FloodObservation',
    COUNT_BIG(*)
FROM dw.Fact_FloodObservation
WHERE SourceKey IS NULL
   OR Obs_ID IS NULL
   OR LTRIM(RTRIM(Obs_ID)) = N'';
GO

/* 4. KIEM TRA MEASURE FACT_POPULATION */

SELECT
    COUNT_BIG(*) AS TotalRows,
    SUM(CASE WHEN Population < 0 THEN 1 ELSE 0 END)
        AS NegativePopulation,
    SUM(CASE WHEN Area_km2 IS NOT NULL AND Area_km2 <= 0
             THEN 1 ELSE 0 END)
        AS InvalidArea,
    SUM(CASE WHEN PopulationDensity < 0 THEN 1 ELSE 0 END)
        AS NegativePopulationDensity
FROM dw.Fact_Population;
GO

/* 5. KIEM TRA MEASURE FACT_FLOODOBSERVATION */

SELECT
    COUNT_BIG(*) AS TotalRows,

    SUM(CASE
        WHEN MinDepth_cm < 0 OR MaxDepth_cm < 0
          OR (MinDepth_cm IS NOT NULL
              AND MaxDepth_cm IS NOT NULL
              AND MinDepth_cm > MaxDepth_cm)
        THEN 1 ELSE 0
    END) AS InvalidDepth,

    SUM(CASE
        WHEN MinDepth_cm IS NOT NULL
         AND MaxDepth_cm IS NOT NULL
         AND AvgDepth_cm IS NOT NULL
         AND (AvgDepth_cm < MinDepth_cm
              OR AvgDepth_cm > MaxDepth_cm)
        THEN 1 ELSE 0
    END) AS InvalidAverageDepth,

    SUM(CASE
        WHEN Duration_hours < 0
        THEN 1 ELSE 0
    END) AS NegativeDuration,

    SUM(CASE
        WHEN ObservationCount <> 1
        THEN 1 ELSE 0
    END) AS InvalidObservationCount

FROM dw.Fact_FloodObservation;
GO