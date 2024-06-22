# pandasライブラリをインポートする
# ファイル内で略称pdで参照できるように設定、機能をpdで使用することができる
import pandas as pd

# 変数に使用するファイルの保存場所を代入する
file_path = '2_4_3/advertising_sales_data.csv'

# 変数dataにpandasライブラリのread_csvメソッドを使用しDataFrame形式で代入
# Pythonで扱いやすい形式に変換する
data = pd.read_csv(file_path)

# headメソッドでdata変数の内容を先頭から５行表示、これはデフォルトの挙動
# 引数に.head（10）とすることで表示する行数を変更可能
# データがDataFrame形式に変換されていることがメソッド使用の条件
print(data.head())