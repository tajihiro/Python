import pandas as pd

# File1読込
df1 = pd.read_csv("data\\file1.csv")
# 欠損値の0埋め
df1 = df1.fillna(0)
# 重複行削除
df1 = df1.drop_duplicates('id')

# 抽出
df1 = df1[df1['name'] != '松本']
# 列追加
df1.loc[: ,'amount'] = df1['sales'] + df1['tax']
# 集約
df1 = df1[['name','sales', 'amount']].groupby(df1['name']).sum()

print("--- df1 ---")
print(df1)

# File2読込
df2 = pd.read_csv("data\\file2.csv")

print("--- df2 ---")
print(df2)

# File1とFile2の比較
df3 = pd.merge(df1, df2, left_on=['name'], right_on=['name'])

df3 = df3[df3['amount'] != df3['total']]
print("--- df3 ---")
print(df3)

