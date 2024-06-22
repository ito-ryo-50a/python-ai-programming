import pandas as pd

file_path = 'data/sample_sales_data.xlsx'

df = pd.read_excel(file_path)

file_path = '3_2_3/sample.xlsx'

# to_excel()はpandasライブラリのDataFrameクラスに定義されているメソッド
# DataFrameクラスのインスタンスになっているデータを拡張子が.xlsxもしくは.xlsのファイルとして書き出す
# 引数でDataFrameのheader(列のアクセサ)とindex(行のアクセサ)を非表示にすることができる
df.to_excel(file_path, index=False)

print(f"{file_path}にデータを出力しました。")
