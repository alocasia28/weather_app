import csv
from datetime import datetime
from statistics import mean

"""Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """



 
list = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]

def calculate_mean(weather_data):
    int_list = []
    for i in weather_data:
        int_list.append(float(i))
    average = mean(int_list)
    print(float(average))
    

    #print(x)

calculate_mean(list)


    



'''def load_data_from_csv():
    file = open("/Users/alisha/Coding/weather_app/tests/data/example_one.csv","r")
    data = list(csv.reader(file,delimiter=","))
    file.close() 
    
    x = []s
    for i in data[1:]:
        x.append([i[0],i[1],i[2]])
    print(x)
load_data_from_csv()'''

'''FILE = "/Users/alisha/Coding/weather_app/tests/data/example_one.csv"

file = open(FILE,"r")
data = list(csv.reader(file,delimiter=","))
file.close() 

    
x = []

for i in data[1:]: 
    x.append([(i[0]),int(i[1]),int(i[2])])
    print(x)

    

     open(FILE, 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        if len(row) >0:
            print(row)
        else:
            print("Nope")'''
    

