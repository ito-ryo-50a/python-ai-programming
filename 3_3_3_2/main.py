import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

# 出力先フォルダのパス
output_folder = '3_3_3_2'

# 出力先フォルダが存在しない場合は作成
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

file_path = 'data/sample_sales_data2.xlsx'

df = pd.read_excel(file_path)

# データを長い形式のデータフレームに変換
df_melted = df.melt(id_vars=['地区', '部門'], var_name='四半期', value_name='売上')

# 折れ線グラフの作成
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melted, x='四半期', y='売上', hue='地区', style='部門')
plt.title('部門別売上推移')
plt.xticks(rotation=45)
plt.savefig(f'{output_folder}/部門別売上推移.png')
plt.close()

# 棒グラフの作成
plt.figure(figsize=(10, 6))
sns.barplot(data=df_melted, x='四半期', y='売上', hue='地区')
plt.xticks(rotation=45)
plt.title('地区別四半期売上')
plt.savefig(f'{output_folder}/地区別四半期売上.png')
plt.close()

# ヒートマップの作成
plt.figure(figsize=(10, 6))
heatmap_data = df.drop(['地区', '部門'], axis=1).set_index(df['地区'] + ' ' + df['部門'])
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='coolwarm')
plt.title('部門別四半期別売上ヒートマップ')
plt.savefig(f'{output_folder}/部門別四半期売上ヒートマップ.png')
plt.close()

# 箱ひげ図の作成
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_melted, x='部門', y='売上', hue='地区')
plt.title('各部門の売上分布')
plt.savefig(f'{output_folder}/地区部門別売上分布.png')
plt.close()
