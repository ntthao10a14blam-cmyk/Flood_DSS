/*
============================================================
Project  : Flood Decision Support System
Database : Flood_DSS
Phase    : Phase 4 - Data Warehouse Implementation
Script   : Create_Flood_DSS.sql
Owner    : TV1

Purpose:
    1. Create Flood_DSS database.
    2. Create 2 core schemas for the data architecture.

Schemas:
    stg  : Staging Layer (Vùng đệm trung gian nhận dữ liệu từ CSV)
    dw   : Dimensional Data Warehouse (Kho dữ liệu mô hình Star Schema)
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
   2. CREATE SCHEMA: stg (Staging Layer)
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
   3. CREATE SCHEMA: dw (Data Warehouse Layer)
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
   4. VALIDATION
   ========================================================= */

SELECT
    name AS SchemaName
FROM sys.schemas
WHERE name IN
(
    N'stg',
    N'dw'
)
ORDER BY name;
GO