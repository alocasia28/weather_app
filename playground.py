from datetime import datetime
from statistics import mean


def find_min(weather_data):
   
    float_list = []
    for i in weather_data:
        float_list.append(float(i))
    min_value = min(float_list)
    index = float_list.index(min_value)

    print(float(min_value),index)

find_min([10.4, 14.5, 12.9, 8.9, 10.5, 11.7])

