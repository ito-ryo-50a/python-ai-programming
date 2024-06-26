import pandas as pd

file_path = 'data/sample_sales_data2.xlsx'

df = pd.read_excel(file_path)

# 合計カラムを計算
# ilocは「integer location」 DataFrameで位置ベースのインデックス指定をするためのメソッド(二次元配列の添字指定と同じ)
# axisは「軸」 axis=0 == 行方向(y軸), axis=1 == 列方向(x軸)
df['合計'] = df.iloc[:, 2:].sum(axis=1)

# 地区部門カラムを作成
df['地区部門'] = df['地区'] + "-" + df['部門']

# 合計カラムで降順に並べ替え
# ascendingはTrueで昇順、Falseで降順
# inplaceはTrueで元のDataFrameを変更、Falseで元のDataFrameは変更せず新しいDataFrameを返す
df.sort_values(by='合計', ascending=False, inplace=True)

# 必要なカラムのみを含むDataFrameを作成
output_df = df[['地区部門', '合計']]

# Excelファイルに出力
output_df.to_excel('3_3_1_2/部門別売上.xlsx', index=False, sheet_name='部門別売上')
