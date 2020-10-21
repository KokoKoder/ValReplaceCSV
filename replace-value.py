# kw-replace-csv.py
# Google Ad keyword suggestion tool gives the Average Search volume as an interval.
# This script replace it by a numberical value.
# Place the value you exported from google Ad in a csv with the following columns: Keyword,Avg. Monthly Searches
# keeps all data in the csv file and replace the text in
# the "Average Search Volume" column by a numerical value (lower end)

import csv

reader = csv.reader(open('keyword_xls.csv', encoding='utf-16'))
spe = ["[","'","]",'"']
lines = [l for l in reader]
with open('keyword_output.csv','w', newline='') as csvoutput:
    writer=csv.writer(csvoutput)
    i = 0
    for line in lines:
        line = lines[i]
        with open('temp.txt','w') as temp:
            temp.write(str(line))
        kw_vol = open("temp.txt").read()
        kw_data =line.split('\\t')#This trick is not necessary if the csv spearator are coma instead of tab. For tab it is really convenient.
        for word in spe:
            kw_data[0]=kw_data[0].replace(word,'')
            kw_data[11]=kw_data[11].replace(word,'')
        if kw_data[3]== '1K – 10K':
            kw_data[3]= 1000
        elif kw_data[3]== '10K – 100K':
            kw_data[3]= 10000
        elif kw_data[3]== '100 – 1K':
            kw_data[3]= 100
        elif kw_data[3]== '10 – 100':
            kw_data[3]= 10
        elif kw_data[3]== '0 – 10':
            kw_data[3]= 1
        lines[i]=kw_data
        i=i+1
    writer.writerows(lines)
