from datetime import datetime
from statistics import mean


def find_min(weather_data):
   
    float_list = []
    for i in weather_data:
        float_list.append(float(i))
    min_value = min(float_list)
    index = len(float_list) - list(reversed(float_list)).index(min_value)-1
    
    print(float(min_value),index)

find_min([49, 57, 56, 55, 53, 49])