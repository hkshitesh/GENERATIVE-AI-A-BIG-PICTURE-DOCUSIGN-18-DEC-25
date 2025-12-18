## Link of Virtaul Machine

  https://docs.google.com/spreadsheets/d/1_7eJDFbuqY_WVFAR1wqRJNfjiSehXFm9TYp_HkoAYhc/edit?usp=sharing

## Lab Exercise 1: Prommpt Engineering

https://colab.research.google.com/drive/1IPBvDtafvIFXh3L9-g-YCxBIjE-Rif5C?usp=sharing

## Project Work 1: Build Your First MCP Server: Leave Management

https://github.com/hkshitesh/MCP-SERVER-DS

## Project Work 2: Develop a DocuSign Agreement AI Agent

https://colab.research.google.com/drive/1GQWnTbslwqAct15jM5NNvA1pFFfFiuzi?usp=sharing


-- Choose an account role that can create objects
USE ROLE ACCOUNTADMIN;
-- Create a warehouse for the lab (small size for cost control)
CREATE OR REPLACE WAREHOUSE lab_wh WITH WAREHOUSE_SIZE = 'XSMALL' AUTO_SUSPEND = 60 AUTO_RESUME = TRUE;

-- Create a database and schema
CREATE OR REPLACE DATABASE lab_db;
CREATE OR REPLACE SCHEMA lab_db.public;

USE WAREHOUSE lab_wh;
USE DATABASE lab_db;
USE SCHEMA lab_db.public;
