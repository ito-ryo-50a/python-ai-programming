import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data/sample_sales_data2.xlsx'

df = pd.read_excel(file_path)

# 部門ごとの売上推移を折れ線グラフで表示
plt.figure(figsize=(12, 8))
for i in range(len(df)):
    plt.plot(df.columns[2:], df.iloc[i, 2:], label=f"{df.iloc[i, 0]}-{df.iloc[i, 1]}")

# グラフの装飾
plt.title('各部門のFY2023Q1からFY2024Q4までの売上推移')
plt.xlabel('四半期')
plt.ylabel('売上')
plt.legend()
plt.grid(True)
plt.show()