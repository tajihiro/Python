import json
import csv
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

path = './data/sample.txt'
records = [json.loads(line) for line in open(path)]
area = [rec['cy'] for rec in records if 'cy' in rec]
#print(area[:10])

frame = DataFrame(records)
area_counts = frame['cy'].value_counts()
print(area_counts)
area_counts.plot(kind)

# path = './data/sample.csv'
# f = open(path)
# records = csv.reader(f)
# records = [csv.reader(line) for line in open(path,'rb')]

#for row in records:
#last_name = [row[1] for row in records]

