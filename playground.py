from datetime import datetime

weather_data = [49, 57, 56, 55, 53]
def calculate_mean(weather_data):
    float_list = []
    for i in weather_data:
        float_list.append(float(i))
    average = sum(float_list)/len(float_list)
    output = float(average) 
    return output

calculate_mean(weather_data)




