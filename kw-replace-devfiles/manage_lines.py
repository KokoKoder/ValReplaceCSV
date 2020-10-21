# kw-replace-csv.py
import csv

reader = csv.reader(open('kw-ASCII.csv'))
lines = [l for l in reader]
i = 0
for line in lines:
    row = str(lines[i])
    print('value of row: ' + row + 'at iteration: '+ str(i) )
    with open('temp.txt','w') as temp:
        temp.write(row)
    kw_vol = open("temp.txt").read()
    kw_data =kw_vol.split('\\t')
    spe = ["'","]"]
    for word in spe:
        kw_data[1]=kw_data[1].replace(word,'')  
    print (kw_data[1])
    i=i+1
