# Data Ingestion Guide: `main.py` for Snowflake

## Introduction

This document provides a comprehensive guide to using the `main.py` script within the GLOBAL ELECTRONIC RETAILS ANALYSIS SNOWFLAKE project. The primary purpose of `main.py` is to facilitate the ingestion of local CSV (Comma Separated Values) data files into Snowflake, leveraging the `snowflake-connector-python` library and Pandas DataFrames for efficient data transfer. This guide will walk you through the setup, configuration, execution, and common troubleshooting steps for successful data loading.

## Table of Contents

1.  [Introduction](#introduction)
2.  [Table of Contents](#table-of-contents)
3.  [Prerequisites](#prerequisites)
4.  [Configuration](#configuration)
    *   [Snowflake Connection Parameters](#snowflake-connection-parameters)
    *   [CSV File Path](#csv-file-path)
    *   [Target Table Name](#target-table-name)
5.  [Script Overview](#script-overview)
6.  [How to Run](#how-to-run)
7.  [Troubleshooting](#troubleshooting)
8.  [Glossary of Terms](#glossary-of-terms)
9.  [References](#references)

## Prerequisites

Before running the `main.py` script, ensure you have the following software and libraries installed on your system:

*   **Python:** Version 3.8 or higher is recommended. You can download Python from the official website: [python.org](https://www.python.org/downloads/)
*   **pip:** Python's package installer, usually comes bundled with Python installations.

Once Python and `pip` are available, install the necessary Python libraries using the following command in your terminal or command prompt:

```bash
pip install pandas snowflake-connector-python
```

*   `pandas`: A powerful data manipulation and analysis library.
*   `snowflake-connector-python`: The official Snowflake connector for Python, enabling interaction with Snowflake databases.

## Configuration

The `main.py` script requires specific parameters to connect to your Snowflake instance and identify the data source and destination. These parameters are defined directly within the script and need to be updated with your specific values.

### Snowflake Connection Parameters

The following variables in `main.py` must be configured with your Snowflake account details:

```python
# Connect to snowflake
SNOWFLAKE_USER = 
SNOWFLAKE_PASSWORD = 
SNOWFLAKE_ACCOUNT = 
SNOWFLAKE_WAREHOUSE = 
SNOWFLAKE_DATABASE = 
SNOWFLAKE_SCHEMA = 
SNOWFLAKE_ROLE = 
```

*   `SNOWFLAKE_USER`: Your Snowflake username.
*   `SNOWFLAKE_PASSWORD`: Your Snowflake password.
*   `SNOWFLAKE_ACCOUNT`: Your Snowflake account identifier (e.g., `your_account_name.your_region`).
*   `SNOWFLAKE_WAREHOUSE`: The name of the Snowflake virtual warehouse to use for query execution (e.g., `COMPUTE_WH`).
*   `SNOWFLAKE_DATABASE`: The name of the Snowflake database where the data will be loaded (e.g., `GLB_ELEC_RETS`).
*   `SNOWFLAKE_SCHEMA`: The name of the schema within the specified database (e.g., `GER2`).
*   `SNOWFLAKE_ROLE`: The Snowflake role to assume for the connection (e.g., `ACCOUNTADMIN`, `SYSADMIN`).

**Important:** For security best practices, avoid hardcoding sensitive credentials directly in the script for production environments. Consider using environment variables or a secure configuration management system.

### CSV File Path

The script reads data from a local CSV file. The placeholder `PATH` needs to be replaced with the absolute or relative path to your CSV file:

```python
# Read CSV
df = pd.read_csv(r"PATH")
```

Replace `r"PATH"` with the actual path, for example: `r"C:\Users\YourUser\Documents\data.csv"` or `"./data/sales.csv"`. The `r` prefix indicates a raw string, which is useful for Windows paths to avoid issues with backslashes.

### Target Table Name

The `table_name` variable specifies the name of the table in Snowflake where the data will be ingested.

```python
table_name = 'NEW_FILE_NAME'  # Change this to your desired table name
```

Replace `'NEW_FILE_NAME'` with the desired name for your Snowflake table. The script is configured with `auto_create_table=True`, meaning if the table does not exist, it will be automatically created based on the DataFrame's schema.

## Script Overview

The `main.py` script automates the process of loading CSV data into Snowflake. Here's a step-by-step breakdown of its functionality:

1.  **Import Libraries:** The script begins by importing necessary libraries: `sys` (for interpreter info), `pandas` (for data handling), and `snowflake.connector` along with `write_pandas` (for Snowflake interaction).
    ```python
    import sys
    print("Interpreter:", sys.executable)
    import pandas as pd
    print("pandas version:", pd._version_)

    import snowflake.connector
    from snowflake.connector.pandas_tools import write_pandas
    print("All imports succeeded!")
    ```
2.  **Read CSV File:** It reads the specified CSV file into a Pandas DataFrame. This DataFrame holds the data in memory, ready for transfer.
    ```python
    # Read CSV
    df = pd.read_csv(r"PATH")
    ```
3.  **Establish Snowflake Connection:** Using the configured credentials, the script establishes a secure connection to your Snowflake account.
    ```python
    # Establish the connection
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
        role=SNOWFLAKE_ROLE
    )
    ```
4.  **Write DataFrame to Snowflake:** The `write_pandas` function from `snowflake.connector.pandas_tools` is used to efficiently upload the Pandas DataFrame to the specified Snowflake table. The `auto_create_table=True` argument ensures that if the target table does not exist, it will be created automatically, inferring column names and data types from the DataFrame.
    ```python
    # Replace 'YOUR_TABLE' with actual table name and use auto_create_table
    table_name = 'NEW_FILE_NAME'  # Change this to your desired table name
    success, nchunks, nrows, _ = write_pandas(
        conn,
        df,
        table_name,
        auto_create_table=True  # This will create the table if it doesn't exist
    )
    print(f"Inserted {nrows} rows in {nchunks} batch(es).")
    ```
5.  **Close Connection:** Finally, the script closes the Snowflake connection to release resources.
    ```python
    # Close Connection
    conn.close()
    ```

## How to Run

Follow these steps to execute the `main.py` script:

1.  **Ensure Prerequisites:** Verify that Python, `pandas`, and `snowflake-connector-python` are installed as described in the [Prerequisites](#prerequisites) section.
2.  **Configure `main.py`:** Open the `main.py` file (located at `C:\Users\6135532\OneDrive - Thomson Reuters Incorporated\Desktop\ClarityForge & COAL\Clarity Forge\(Interactively Created Documentations)\GLB_ELEC_RET\main.py`) in a text editor.
    *   Update the `PATH` variable to point to your CSV file.
    *   Fill in all Snowflake connection parameters (`SNOWFLAKE_USER`, `SNOWFLAKE_PASSWORD`, etc.) with your specific account details.
    *   Set the `table_name` variable to your desired Snowflake table name.
3.  **Navigate to Script Directory:** Open your terminal or command prompt and navigate to the directory where `main.py` is located.
    ```bash
    cd "C:\Users\6135532\OneDrive - Thomson Reuters Incorporated\Desktop\ClarityForge & COAL\Clarity Forge\(Interactively Created Documentations)\GLB_ELEC_RET"
    ```
4.  **Execute the Script:** Run the script using the Python interpreter:
    ```bash
    python main.py
    ```
5.  **Verify Output:** The script will print messages indicating the Python interpreter and pandas version, successful import, and finally, a confirmation of the number of rows inserted into Snowflake.
    ```
    Interpreter: C:\path\to\your\python.exe
    pandas version: 2.1.4
    All imports succeeded!
    Inserted XXX rows in Y batch(es).
    ```
    If successful, you can then query the specified `table_name` in your Snowflake environment to verify the data.

## Troubleshooting

This section addresses common issues you might encounter when using the `main.py` script for data ingestion.

*   **`FileNotFoundError: [Errno 2] No such file or directory: 'PATH'`**
    *   **Cause:** The `PATH` specified for your CSV file is incorrect or the file does not exist at that location.
    *   **Solution:** Double-check the file path in `df = pd.read_csv(r"PATH")`. Ensure it's an absolute path or a correct relative path from where you are running the script. Verify the file exists and you have read permissions.

*   **`ModuleNotFoundError: No module named 'pandas'` or `No module named 'snowflake.connector'`**
    *   **Cause:** The required Python libraries are not installed in your environment.
    *   **Solution:** Run `pip install pandas snowflake-connector-python` to install the dependencies. Ensure you are using the `pip` associated with the Python interpreter that you are using to run `main.py`.

*   **Snowflake Connection Errors (e.g., `snowflake.connector.errors.DatabaseError: 250001: Failed to connect to DB. ...` )**
    *   **Cause:** Incorrect Snowflake connection parameters, network issues, or firewall restrictions.
    *   **Solution:**
        *   Verify `SNOWFLAKE_USER`, `SNOWFLAKE_PASSWORD`, `SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_WAREHOUSE`, `SNOWFLAKE_DATABASE`, `SNOWFLAKE_SCHEMA`, and `SNOWFLAKE_ROLE` are all correctly entered and match your Snowflake credentials.
        *   Ensure your network allows outbound connections to Snowflake endpoints.
        *   Check if your Snowflake user has the necessary permissions (e.g., `USAGE` on database/schema, `OPERATE` on warehouse, `CREATE TABLE` on schema if `auto_create_table` is used for a new table, and `INSERT` on the table).

*   **Data Type Mismatch or Ingestion Errors**
    *   **Cause:** While `write_pandas` is robust, complex data types or inconsistencies in your CSV might lead to issues during table creation or data insertion.
    *   **Solution:**
        *   Inspect your CSV file for unexpected characters, inconsistent formatting, or headers that might not align with desired Snowflake column names.
        *   If `auto_create_table` creates a table with incorrect data types, consider pre-creating the table in Snowflake with explicit data types before running the script, then set `auto_create_table=False`.
        *   Check Snowflake's query history for more detailed error messages related to the ingestion.

*   **`write_pandas` performance issues with very large files**
    *   **Cause:** For extremely large CSV files, loading the entire file into a Pandas DataFrame might consume significant memory or time.
    *   **Solution:** For production-grade large file ingestion, consider alternative Snowflake loading methods like Snowpipe or `PUT`/`COPY INTO` commands, which are optimized for bulk loading and can handle larger volumes more efficiently. The `main.py` script is best suited for moderately sized datasets.

## Glossary of Terms

*   **CSV (Comma Separated Values):** A plain text file format for storing tabular data, where each line is a data record and fields are separated by commas.
*   **DataFrame:** A 2-dimensional labeled data structure with columns of potentially different types, primarily used in the Pandas library for data manipulation.
*   **Pandas:** An open-source Python library providing high-performance, easy-to-use data structures and data analysis tools.
*   **Schema:** In Snowflake, a logical grouping of database objects, such as tables, views, and functions.
*   **Snowflake:** A cloud-based data warehousing platform that enables data storage, processing, and analytic solutions.
*   **`snowflake-connector-python`:** The official Python library provided by Snowflake for connecting to and interacting with a Snowflake data warehouse.
*   **Warehouse (Virtual Warehouse):** In Snowflake, a cluster of compute resources that perform data processing. You can create multiple warehouses to manage different workloads.
*   **`write_pandas`:** A function provided by `snowflake-connector-python` that efficiently writes a Pandas DataFrame to a Snowflake table.

## References

*   `main.py`: The Python script responsible for data ingestion.
*   `README.md`: Project overview and initial setup instructions.
*   `main.sql`: Contains SQL commands for database and schema creation, and table definitions within the Snowflake environment.