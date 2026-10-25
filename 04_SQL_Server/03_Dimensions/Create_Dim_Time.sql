/*
============================================================
Project : Flood Decision Support System
Script  : Create_Dim_Time.sql
Owner   : TV1

Grain:
    One row = one calendar day.

TimeKey:
    YYYYMMDD

Unknown member:
    TimeKey  = -1
    FullDate = 1900-01-01
============================================================
*/

USE Flood_DSS;
GO


/* =========================================================
   1. CREATE DIM_TIME
   ========================================================= */

IF OBJECT_ID(N'dw.Dim_Time', N'U') IS NULL
BEGIN

    CREATE TABLE dw.Dim_Time
    (
        TimeKey     INT          NOT NULL,
        FullDate    DATE         NOT NULL,

        [Day]       TINYINT      NULL,
        [Month]     TINYINT      NULL,
        [Quarter]   TINYINT      NULL,
        [Year]      SMALLINT     NULL,

        Season      NVARCHAR(30) NULL,
        DayOfWeek   TINYINT      NULL,

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

END;
GO


/* =========================================================
   2. UNKNOWN MEMBER
   ========================================================= */

IF NOT EXISTS
(
    SELECT 1
    FROM dw.Dim_Time
    WHERE TimeKey = -1
)
BEGIN

    INSERT INTO dw.Dim_Time
    (
        TimeKey,
        FullDate,
        [Day],
        [Month],
        [Quarter],
        [Year],
        Season,
        DayOfWeek
    )
    VALUES
    (
        -1,
        '19000101',
        NULL,
        NULL,
        NULL,
        NULL,
        N'Unknown',
        NULL
    );

END;
GO


/* =========================================================
   3. GENERATE CALENDAR

   Current project analysis period:
   2002-01-01 -> 2025-12-31

   Change @EndDate later if project scope expands.
   ========================================================= */

DECLARE @CurrentDate DATE = '20020101';
DECLARE @EndDate     DATE = '20251231';


WHILE @CurrentDate <= @EndDate
BEGIN

    DECLARE @TimeKey INT;

    SET @TimeKey =
          YEAR(@CurrentDate) * 10000
        + MONTH(@CurrentDate) * 100
        + DAY(@CurrentDate);


    IF NOT EXISTS
    (
        SELECT 1
        FROM dw.Dim_Time
        WHERE TimeKey = @TimeKey
    )
    BEGIN

        INSERT INTO dw.Dim_Time
        (
            TimeKey,
            FullDate,
            [Day],
            [Month],
            [Quarter],
            [Year],
            Season,
            DayOfWeek
        )
        VALUES
        (
            @TimeKey,
            @CurrentDate,
            DAY(@CurrentDate),
            MONTH(@CurrentDate),
            DATEPART(QUARTER, @CurrentDate),
            YEAR(@CurrentDate),

            /* Season definition:
               Temporary simple month grouping.
               Confirm with team before DSS interpretation.
            */
            CASE
                WHEN MONTH(@CurrentDate) BETWEEN 5 AND 11
                    THEN N'Rainy'
                ELSE N'Dry'
            END,

            ((DATEDIFF(DAY, '19000101', @CurrentDate) % 7) + 1)
        );

    END;

    SET @CurrentDate = DATEADD(DAY, 1, @CurrentDate);

END;
GO


/* =========================================================
   4. VALIDATION
   ========================================================= */

SELECT
    COUNT(*) AS TotalRows,
    MIN(FullDate) AS MinDate,
    MAX(FullDate) AS MaxDate
FROM dw.Dim_Time;
GO


SELECT TOP 10 *
FROM dw.Dim_Time
ORDER BY TimeKey;
GO

