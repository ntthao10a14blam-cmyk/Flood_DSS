
USE Flood_DSS;
GO

SET XACT_ABORT ON;
GO

BEGIN TRY
    BEGIN TRANSACTION;

    -- 1. Dim_Area
    IF NOT EXISTS (
        SELECT 1 FROM dw.Dim_Area
        WHERE AreaKey = -1
    )
    BEGIN
        SET IDENTITY_INSERT dw.Dim_Area ON;

        INSERT INTO dw.Dim_Area (
            AreaKey, Area_ID, Area_Name,
            Area_Level, BoundaryVersion, IsCurrent
        )
        VALUES (
            -1, N'UNKNOWN', N'Unknown',
            N'Unknown', N'Unknown', 0
        );

        SET IDENTITY_INSERT dw.Dim_Area OFF;
    END;

    -- 2. Dim_Cause
    IF NOT EXISTS (
        SELECT 1 FROM dw.Dim_Cause
        WHERE CauseKey = -1
    )
    BEGIN
        SET IDENTITY_INSERT dw.Dim_Cause ON;

        INSERT INTO dw.Dim_Cause (
            CauseKey, Cause_Name
        )
        VALUES (-1, N'Unknown');

        SET IDENTITY_INSERT dw.Dim_Cause OFF;
    END;

    -- 3. Dim_Source
    IF NOT EXISTS (
        SELECT 1 FROM dw.Dim_Source
        WHERE SourceKey = -1
    )
    BEGIN
        SET IDENTITY_INSERT dw.Dim_Source ON;

        INSERT INTO dw.Dim_Source (
            SourceKey, Source_ID, Source_Name
        )
        VALUES (
            -1, N'UNKNOWN', N'Unknown'
        );

        SET IDENTITY_INSERT dw.Dim_Source OFF;
    END;

    -- 4. Dim_Location
    IF NOT EXISTS (
        SELECT 1 FROM dw.Dim_Location
        WHERE LocationKey = -1
    )
    BEGIN
        SET IDENTITY_INSERT dw.Dim_Location ON;

        INSERT INTO dw.Dim_Location (
            LocationKey, Location_ID,
            Location_Name, AreaKey
        )
        VALUES (
            -1, N'UNKNOWN',
            N'Unknown', -1
        );

        SET IDENTITY_INSERT dw.Dim_Location OFF;
    END;

    COMMIT TRANSACTION;

    PRINT N'Tao cac ban ghi Unknown thanh cong.';
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;

    -- Tắt IDENTITY_INSERT nếu lỗi xảy ra giữa chừng
    BEGIN TRY
        SET IDENTITY_INSERT dw.Dim_Area OFF;
        SET IDENTITY_INSERT dw.Dim_Cause OFF;
        SET IDENTITY_INSERT dw.Dim_Source OFF;
        SET IDENTITY_INSERT dw.Dim_Location OFF;
    END TRY
    BEGIN CATCH
        PRINT ERROR_MESSAGE();
    END CATCH;

    THROW;
END CATCH;
GO

-- 5. KIỂM TRA KẾT QUẢ
SELECT 'Dim_Area' AS DimensionName,
       AreaKey AS UnknownKey,
       Area_Name AS UnknownName
FROM dw.Dim_Area
WHERE AreaKey = -1

UNION ALL

SELECT 'Dim_Cause', CauseKey, Cause_Name
FROM dw.Dim_Cause
WHERE CauseKey = -1

UNION ALL

SELECT 'Dim_Source', SourceKey, Source_Name
FROM dw.Dim_Source
WHERE SourceKey = -1

UNION ALL

SELECT 'Dim_Location', LocationKey, Location_Name
FROM dw.Dim_Location
WHERE LocationKey = -1;
