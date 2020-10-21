# kw-replace-csv.py
import csv

reader = csv.reader(open('keyword_xls.csv', encoding='utf-16'))
lines = [l for l in reader]
i = 0
for line in lines:
    line = str(lines[i])
    with open('temp.txt','w') as temp:
        temp.write(line)
    kw_vol = open("temp.txt").read()
    kw_data =kw_vol.split('\\t')
    spe = ["[","'","]"]
    for word in spe:
        kw_data[3]=kw_data[3].replace(word,'')
        kw_data[1]=kw_data[1].replace(word,'')
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
    print(str(kw_data[1]) + str(kw_data[3]))
    i=i+1

