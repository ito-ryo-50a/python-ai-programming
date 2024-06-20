import pandas as pd

file_path = 'data/sample_sales_data.xlsx'
df = pd.read_excel(file_path)

##### ここまでは3_2_2の記述と同じ #####


file_path = '3_2_3/sample.xlsx'
df.to_excel(file_path, index=False)

print(f"{file_path}にデータを出力しました。")
