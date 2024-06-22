import pandas as pd

file_path = 'data/sample_sales_data.xlsx'

df = pd.read_excel(file_path)

file_path = '3_2_3_2/sample.dataframe.xlsx'

df.to_excel(file_path, index=False)

print(f"DataFrameを{file_path}に出力しました。")
