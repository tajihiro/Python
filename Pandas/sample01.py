import os
import pandas as pd

# 表示設定
pd.set_option('display.width', 1200)
pd.set_option('display.max_columns', 100)

base_url = 'http://raw.githubusercontent.com/practical-jupyter/sample-data/master/anime/'
anime_csv = os.path.join(base_url, 'anime.csv')

df = pd.read_csv('http://raw.githubusercontent.com/practical-jupyter/sample-data/master/anime/anime.csv')
# df = pd.read_csv(anime_csv)


# df.loc[:, 'column01'] = df['episodes']

print(df)
