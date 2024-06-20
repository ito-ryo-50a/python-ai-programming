import pandas as pd

file_path = '2_4_3/advertising_sales_data.csv'
data = pd.read_csv(file_path)
print(data.head())

##### ここまではmain_a.pyと同じ記述 #####


# matplotlibライブラリをインポートし略称pltで使用可能に設定
# Pythonの主要なグラフ描画ライブラリでグラフやチャートの実装に用いられる
import matplotlib.pyplot as plt

# 表示するキャンバス(ウィンドウ)サイズをwidth:10インチ、height:6インチに設定
plt.figure(figsize=(10, 6))
# scatterメソッドで散布図を作成する
# x軸の値、y軸の値、ドットのカラーをブルーに、ドットの透明度を0.5に指定
plt.scatter(data['広告費'],data['売上'], color='blue', alpha=0.5)
# グラフのタイトルを設定
plt.title('Advertising Cost vs. Sales')
# グラフのx軸のラベルを設定
plt.xlabel('Advertising Cost')
# グラフのy軸のラベルを設定
plt.ylabel('Sales')
# グラフにグリッドを表示する
plt.grid(True)
# 作成したグラフをウィンドウを開いて表示する、表示中は常時スクリプトが実行中となる
plt.show()