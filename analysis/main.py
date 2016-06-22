from pandas import DataFrame, Series
import pandas as pd
import numpy as np

path = "./data/sample.dat"
file = open(path, encoding='utf-8')

cnt = 0
for line in file:
    cnt = cnt + 1

print(cnt)

file.close()
