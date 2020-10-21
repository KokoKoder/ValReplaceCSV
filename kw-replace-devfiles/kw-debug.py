# kw-debug.py

from __future__ import division
import urllib.request
import csv
import codecs
from string import punctuation

# Python 3.x only
import csv
with open('utf16.csv', 'r', encoding='utf16') as csvf:
    for line in csv.reader(csvf):
        print(line) # do something with the line
        

reader = csv.reader(open('kwlist.csv','r',encoding="utf-16"), delimiter=';', quotechar='|')
for row in reader:
    print (row)
out_file = open("c:/out.csv", "wb")
print(4)
writer = csv.writer(out_file)
print(5)
for row in reader:
    print(loop)
    if row['Avg. Monthly Searches (exact match only)']== '10K – 100K':
        row['Avg. Monthly Searches (exact match only)'] = 10000
        writer.writerow(row)
        print(row)
    elif row['Avg. Monthly Searches (exact match only)']== '1K – 10K':
        row['Avg. Monthly Searches (exact match only)']= 1000
        writer.writerow(row)
        print(row)
    elif row['Avg. Monthly Searches (exact match only)']== '100 – 1K':
        row['Avg. Monthly Searches (exact match only)']= 100
        writer.writerow(row)
        print(row)
    elif row['Avg. Monthly Searches (exact match only)']== '10 – 100':
        row['Avg. Monthly Searches (exact match only)']= 10
        writer.writerow(row)
        print(row)
    elif row['Avg. Monthly Searches (exact match only)']== '0 – 10':
        row['Avg. Monthly Searches (exact match only)']= 1
        writer.writerow(row)
        print(row)

   
out_file.close()   
        
