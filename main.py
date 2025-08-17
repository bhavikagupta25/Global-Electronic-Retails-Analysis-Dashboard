import sys
print("Interpreter:", sys.executable)
import pandas as pd
print("pandas version:", pd._version_)

import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
print("All imports succeeded!")

# Read CSV
df = pd.read_csv(r"PATH")

# Connect to snowflake
SNOWFLAKE_USER = 
SNOWFLAKE_PASSWORD = 
SNOWFLAKE_ACCOUNT = 
SNOWFLAKE_WAREHOUSE = 
SNOWFLAKE_DATABASE = 
SNOWFLAKE_SCHEMA = 
SNOWFLAKE_ROLE = 

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

# Replace 'YOUR_TABLE' with actual table name and use auto_create_table
table_name = 'NEW_FILE_NAME'  # Change this to your desired table name
success, nchunks, nrows, _ = write_pandas(
    conn, 
    df, 
    table_name,
    auto_create_table=True  # This will create the table if it doesn't exist
)
print(f"Inserted {nrows} rows in {nchunks} batch(es).")

# Close Connection
conn.close()