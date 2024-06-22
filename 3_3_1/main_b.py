import pandas as pd

file_path = 'data/sample_sales_data2.xlsx'

df = pd.read_excel(file_path)

sales_sum = df.groupby('部門').sum()

with pd.ExcelWriter('3_3_1/sales_summery.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Original Data', index=False)
    sales_sum.to_excel(writer, sheet_name='Sales Summary')