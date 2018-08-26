'''
import csv
rows = []
row = []
with open(r'E:\\vidyadhar\\vidya.csv','r') as csv_file:
    csvreader = csv.reader(csv_file)
    for i in csvreader:
        rows.append(i)

with open(r'E:\\vidyadhar\\kiran.csv','r') as csv_file1:
    csvread = csv.reader(csv_file1)
    for j in csvread:
        row.append(j)

total=str(zip(rows,row))
print (total)
obj=open(r'E:\\vidyadhar\\kongara.csv','w')
for i in total:
    k=obj.write(i)
'''
import pandas as pd

a = pd.read_csv("E:\\vidyadhar\\vidya.csv")
b = pd.read_csv("E:\\vidyadhar\\kiran.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='title')
merged.to_csv("output.csv", index=False)







