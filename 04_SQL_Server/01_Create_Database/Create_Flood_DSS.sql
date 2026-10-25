/*
============================================================
Project  : Flood Decision Support System
Database : Flood_DSS
Phase    : Phase 4 - Data Warehouse Implementation
Script   : Create_Flood_DSS.sql
Owner    : TV1

Purpose:
    1. Create Flood_DSS database.
    2. Create schemas for each data layer.

Schemas:
    stg  : Staging
    dw   : Dimensional Data Warehouse
    mart : Data Mart
    dss  : Decision Support System
============================================================
*/

USE master;
GO


/* =========================================================
   1. CREATE DATABASE
   ========================================================= */

IF DB_ID(N'Flood_DSS') IS NULL
BEGIN
    CREATE DATABASE Flood_DSS;
    PRINT N'Created database Flood_DSS.';
END
ELSE
BEGIN
    PRINT N'Database Flood_DSS already exists.';
END;
GO


USE Flood_DSS;
GO


/* =========================================================
   2. CREATE SCHEMA: stg
   ========================================================= */

IF NOT EXISTS
(
    SELECT 1
    FROM sys.schemas
    WHERE name = N'stg'
)
BEGIN
    EXEC(N'CREATE SCHEMA stg');
    PRINT N'Created schema stg.';
END;
GO


/* =========================================================
   3. CREATE SCHEMA: dw
   ========================================================= */

IF NOT EXISTS
(
    SELECT 1
    FROM sys.schemas
    WHERE name = N'dw'
)
BEGIN
    EXEC(N'CREATE SCHEMA dw');
    PRINT N'Created schema dw.';
END;
GO


/* =========================================================
   4. CREATE SCHEMA: mart
   ========================================================= */

IF NOT EXISTS
(
    SELECT 1
    FROM sys.schemas
    WHERE name = N'mart'
)
BEGIN
    EXEC(N'CREATE SCHEMA mart');
    PRINT N'Created schema mart.';
END;
GO


/* =========================================================
   5. CREATE SCHEMA: dss
   ========================================================= */

IF NOT EXISTS
(
    SELECT 1
    FROM sys.schemas
    WHERE name = N'dss'
)
BEGIN
    EXEC(N'CREATE SCHEMA dss');
    PRINT N'Created schema dss.';
END;
GO


/* =========================================================
   6. VALIDATION
   ========================================================= */

SELECT
    name AS SchemaName
FROM sys.schemas
WHERE name IN
(
    N'stg',
    N'dw',
    N'mart',
    N'dss'
)
ORDER BY name;
GO