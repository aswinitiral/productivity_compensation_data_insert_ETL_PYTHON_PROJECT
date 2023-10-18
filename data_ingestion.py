import pandas as pd
import psycopg2
from psycopg2 import extras
df = pd.read_csv('productivity_n_hourly_compensation.csv')
# Convert DataFrame to a list of tuples
data_tuples = [tuple(row) for row in df.itertuples(index=False, name=None)]
#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='good', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
# Create a cursor and execute the SQL query
cursor = conn.cursor()
table_name = 'prod1'
columns = ', '.join(df.columns)
# Use execute_values to insert multiple rows efficiently
extras.execute_values(cursor, f"INSERT INTO {table_name} ({columns}) VALUES %s", data_tuples)
# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()