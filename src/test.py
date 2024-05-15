import pyodbc
import sqlite3
import sys
from os import popen, path
from settings import Settings
from access.access import Access

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Jaso5\kraken\data\PopulatedAccessDatabase.accdb;')

cursor = conn.cursor()

for row in cursor.execute(
"""
SELECT * FROM AssertableAssets
"""
):
    print(row)

# tables = cursor.tables()
# for row in tables:
#     print(f"Name: {row.table_name}")
    # for column in cursor.columns(table=row.table_name):
    #     print(f"{column.column_name}: <{column.type_name}, {column.data_type}>")