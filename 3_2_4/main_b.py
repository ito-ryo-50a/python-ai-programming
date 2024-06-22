import pandas as pd

file_path = 'data/sample_sales_data.xlsx'

df = pd.read_excel(file_path)

print(df)

df['売上'] = df['価格'] * df['販売数'] * (1 + df ['税率'])
product_sales = df.groupby('商品名')['売上'].sum().reset_index()

category_sales = df.groupby('カテゴリ')['売上'].sum().reset_index()

with pd.ExcelWriter('3_2_4/sales_report.xlsx') as writer:
  product_sales.to_excel(writer, sheet_name='商品ごとの売上', index=False)
  category_sales.to_excel(writer, sheet_name='カテゴリごとの売上', index=False)