import csv
from datetime import datetime



'''def load_data_from_csv():
    file = open("/Users/alisha/Coding/weather_app/tests/data/example_one.csv","r")
    data = list(csv.reader(file,delimiter=","))
    file.close() 
    
    x = []s
    for i in data[1:]:
        x.append([i[0],i[1],i[2]])
    print(x)
load_data_from_csv()'''

FILE = "/Users/alisha/Coding/weather_app/tests/data/example_one.csv"

file = open(FILE,"r")
data = list(csv.reader(file,delimiter=","))
file.close() 

    
x = []

for i in data[1:]: 
    x.append([(i[0]),int(i[1]),int(i[2])])
    print(x)

    
'''with open(FILE, 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        if len(row) >0:
            print(row)
        else:
            print("Nope"'''
    

