import numpy as np
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('example')
# print(df)

# df.to_csv('my_output', index=False)

# print(pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1'))

# df.to_excel('Excel_Sample2.xlsx', sheet_name='Sheet1')


data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# print(df[0].head())


engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table', con=engine)

sqldf = pd.read_sql('my_table', con=engine)
print(sqldf)
