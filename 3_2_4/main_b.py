import pandas as pd

file_path = 'data/sample_sales_data.xlsx'

df = pd.read_excel(file_path)

# 変数dfに代入されているデータを使用して新しく売上カラムを追加
# 売上カラムの値は価格と販売数の積に税率をかけた値を使用する
df['売上'] = df['価格'] * df['販売数'] * (1 + df ['税率'])

# 変数product_salesにgroupbyメソッドを使用して商品名カラムの項目ごとに売上を合計したものを格納する
product_sales = df.groupby('商品名')['売上'].sum().reset_index()

# 変数category_salesにgroupbyメソッドを使用してカテゴリカラムの項目ごとに売上を合計したものを格納する
category_sales = df.groupby('カテゴリ')['売上'].sum().reset_index()

# 引数で指定したファイルのデータからpandasライブラリのDataFrameクラスのExcelWriterオブジェクトを生成
# 略称writerで操作できるように設定
with pd.ExcelWriter('3_2_4/sales_report.xlsx') as writer:

  # product_salesにto_excelメソッドを実行しwriterオブジェクト内に商品ごとの売上というシート名でインデックス非表示で格納する
  product_sales.to_excel(writer, sheet_name='商品ごとの売上', index=False)

  # category_salesにto_excelメソッドを実行しwriterオブジェクト内にカテゴリごとの売上というシート名でインデックス非表示で格納する
  category_sales.to_excel(writer, sheet_name='カテゴリごとの売上', index=False)