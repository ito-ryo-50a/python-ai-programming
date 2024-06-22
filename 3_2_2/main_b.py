import pandas as pd

file_path = 'data/sample_sales_data.xlsx'

df = pd.read_excel(file_path)

print(df)