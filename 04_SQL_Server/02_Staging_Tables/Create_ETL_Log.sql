/*
============================================================
Project : Flood Decision Support System
Script  : Create_ETL_Log.sql
Owner   : TV1

Purpose:
    Create ETL execution logging and data-error tables.
============================================================
*/

USE Flood_DSS;
GO


/* =========================================================
   1. ETL EXECUTION LOG
   ========================================================= */

IF OBJECT_ID(N'stg.ETL_Log', N'U') IS NULL
BEGIN

    CREATE TABLE stg.ETL_Log
    (
        LogID             BIGINT IDENTITY(1,1) NOT NULL,
        BatchID           UNIQUEIDENTIFIER NOT NULL,

        PackageName       NVARCHAR(255) NOT NULL,
        SourceFile        NVARCHAR(500) NULL,

        StartTime         DATETIME2(0) NOT NULL,
        EndTime           DATETIME2(0) NULL,

        RowsRead          INT NULL,
        RowsInserted      INT NULL,
        RowsRejected      INT NULL,

        ExecutionStatus   NVARCHAR(30) NOT NULL,
        ErrorMessage      NVARCHAR(MAX) NULL,

        CONSTRAINT PK_ETL_Log
            PRIMARY KEY (LogID),

        CONSTRAINT CK_ETL_Log_Status
            CHECK
            (
                ExecutionStatus IN
                (
                    N'Running',
                    N'Success',
                    N'Failed'
                )
            ),

        CONSTRAINT CK_ETL_Log_Time
            CHECK
            (
                EndTime IS NULL
                OR EndTime >= StartTime
            ),

        CONSTRAINT CK_ETL_Log_RowsRead
            CHECK (RowsRead IS NULL OR RowsRead >= 0),

        CONSTRAINT CK_ETL_Log_RowsInserted
            CHECK (RowsInserted IS NULL OR RowsInserted >= 0),

        CONSTRAINT CK_ETL_Log_RowsRejected
            CHECK (RowsRejected IS NULL OR RowsRejected >= 0)
    );

    PRINT N'Created stg.ETL_Log.';

END;
GO


/* =========================================================
   2. ETL DATA ERROR
   ========================================================= */

IF OBJECT_ID(N'stg.ETL_Error', N'U') IS NULL
BEGIN

    CREATE TABLE stg.ETL_Error
    (
        ErrorID            BIGINT IDENTITY(1,1) NOT NULL,
        BatchID            UNIQUEIDENTIFIER NOT NULL,

        SourceTable        NVARCHAR(150) NOT NULL,
        SourceRecordID     NVARCHAR(100) NULL,

        ErrorColumn        NVARCHAR(150) NULL,
        ErrorDescription   NVARCHAR(2000) NOT NULL,

        RawValue           NVARCHAR(MAX) NULL,

        CreatedAt          DATETIME2(0) NOT NULL,

        CONSTRAINT PK_ETL_Error
            PRIMARY KEY (ErrorID)
    );

    PRINT N'Created stg.ETL_Error.';

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
      'ETL_Log',
      'ETL_Error'
  )
ORDER BY TABLE_NAME;
GO

