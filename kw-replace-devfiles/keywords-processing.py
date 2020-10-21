# keywords-processing.py
#change the txt value in Google Adwords keyword suggestion csv by a numerical value
#the lower value has been choosen as default to avoid over estimated forecast.
#Requirement: csv for excel to work due to additional lines in the csv for google adwords.
#requirement: edit: only keyword and Avg. Monthly Searches colums have been kept and the latter edited
#Result: print the value but does not actually change the file.
# This is a script intended for development. NOT A Production script

from __future__ import division
import urllib.request
import csv
import codecs
from string import punctuation


kwtable = []

with codecs.open('kwlist_test.csv', 'rU', 'utf-16') as csvfile:
    kwtable = csv.DictReader(csvfile)
    for row in kwtable:
        print(row['Keyword'], row['Avg. Monthly Searches'])
        
with codecs.open('kwlist_test.csv', 'rU', 'utf-16') as csvfile:
    kwtable = csv.DictReader(csvfile)
    for row in kwtable:
        if row['Avg. Monthly Searches']== '1K – 10K':
            row['Avg. Monthly Searches']= 1000
            print(row['Keyword'], row['Avg. Monthly Searches'])
        elif row['Avg. Monthly Searches']== '10K – 100K':
            row['Avg. Monthly Searches']= 10000
            print(row['Keyword'], row['Avg. Monthly Searches'])
        elif row['Avg. Monthly Searches']== '100 – 1K':
            row['Avg. Monthly Searches']= 100
            print(row['Keyword'], row['Avg. Monthly Searches'])
        elif row['Avg. Monthly Searches']== '10 – 100':
            row['Avg. Monthly Searches']= 10
            print(row['Keyword'], row['Avg. Monthly Searches'])
        elif row['Avg. Monthly Searches']== '0 – 10':
            row['Avg. Monthly Searches']= 1
            print(row['Keyword'], row['Avg. Monthly Searches'])
        
