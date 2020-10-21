# kw-replace-csv.py
import csv

reader = csv.reader(open('kw-ASCII.csv'))
lines = [l for l in reader]
line = str(lines[1])
with open('temp.txt','w') as temp:
    temp.write(line)
ctrl =  open('temp.txt','r')
print('Ctrl2: '+ ctrl.read())
kw_vol = open("temp.txt").read()
print(kw_vol)
kw_data =kw_vol.split('\\t')
spe = ["'","]"]
for word in spe:
    kw_data[1]=kw_data[1].replace(word,'')  
print (kw_data[1])

