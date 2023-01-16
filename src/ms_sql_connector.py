from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime,Integer,create_engine
from datetime import datetime
import pandas as pd
import pyodbc 

cnxn_str = ("Driver={ODBC Driver 11 for SQL Server};"
            "Server=EVS08APD1494JW0;"
            "Database=NEW_DB;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()
cursor.execute('SELECT Top 2 DEPARTMENT_ID from [NEW_DB].[dbo].[department]')
# data = pd.read_sql("SELECT Top 2 DEPARTMENT_ID from [NEW_DB].[dbo].[department]", cnxn)
for row in cursor.fetchall():
    print('row = %r' % (row,))