import pandas as pd

file_path = 'data/sample_sales_data2.xlsx'

df = pd.read_excel(file_path)

df['合計'] = df.iloc[:, 2:].sum(axis=1)

df['地区部門'] = df['地区'] + "-" + df['部門']

output_df = df[['地区部門', '合計']]
output_df.to_excel('3_3_1/部門別売上.xlsx', index=False, sheet_name='部門別売上')