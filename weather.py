import csv
from datetime import datetime

DEGREE_SYMBOL = "°C"

def load_data_from_csv(csv_file):
    file = open(csv_file,"r")
    next(file)
    data = list(csv.reader(file,delimiter=","))
    file.close() 
    
    new_list = []
    for i in data:
        if i: #handles blank lines 
            new_list.append([(i[0]),int(i[1]),int(i[2])])
    return new_list



#this works with manual input, cannot test in unit test yet(will probably get used for the daily summary)
def format_temperature(temp):
    formatted_temp = str(temp) + DEGREE_SYMBOL
    print(formatted_temp)
  


#tested working
def convert_date(iso_string):
    converted_date = datetime.fromisoformat(iso_string) #convert ISO format to date
    formatted_date = str(converted_date.strftime('%A %d %B %Y')) #return date in format of Weekday DD Month YYYY e.g. Wednesday 25 October 2023
    return formatted_date




#Accepts an argument, converts to float, and returns the temp as celsius rounded to 1dp
def convert_f_to_c(temp_in_farenheit):
    c_temp = ((float(temp_in_farenheit))-32)*5/9
    y = "{:.1f}".format(c_temp)
    return float(y)
    '''Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """'''

#accepts a list of numbers and provides the mean of the numbers in the list. 
def calculate_mean(weather_data):
    float_list = []
    for i in weather_data:
        float_list.append(float(i))
    average = sum(float_list)/len(float_list)
    output =(float(average))
    return output





    


def find_min(weather_data):
   
    float_list = []
    for i in weather_data:
        try:
            float_list.append(float(i))
        
            min_value = min(float_list,default = 0) 
            index = len(float_list) - list(reversed(float_list)).index(min_value)-1
        except ValueError:
            print ("fuhged about it")
    
    try: 
        return (float(min_value),index)
    except UnboundLocalError:
        return ()



def find_max(weather_data):
    float_list = []
    for i in weather_data:
        try:
            float_list.append(float(i))
        
            max_value = max(float_list,default = 0) 
            index = len(float_list) - list(reversed(float_list)).index(max_value)-1
        except ValueError:
            return ()
    
    try: 
        return (float(max_value),index)
    except UnboundLocalError:
        return ()



def generate_summary(weather_data):
    date_list = []
    min_list = []
    max_list = []
    for i in weather_data:
        date = convert_date(i[0]) #converts each iteration of date from f to c which is in index location 0
        min_temp = convert_f_to_c(i[1]) #converts each iteration of min temp from f to cwhich is in index location 1
        max_temp = convert_f_to_c(i[2]) #converts each iteration of max temp from f to c which is in index location 2

        date_list.append(date) #creates a list of dates
        min_list.append(float(min_temp)) #creates a list of min temps
        max_list.append(max_temp) #creates a list of max temps

    avg_min = calculate_mean(min_list)
    avg_max = calculate_mean(max_list)

    min_date = min_list.index(min(min_list))
    max_date = max_list.index(max(max_list))

      
    output = (f'{len(date_list)} Day Overview\n  The lowest temperature will be {min(min_list)}{DEGREE_SYMBOL}, \
and will occur on {date_list[min_date]}.\n  The highest temperature will be {max(max_list)}{DEGREE_SYMBOL}, and will occur on {date_list[max_date]}.\n  The average low this week is {avg_min}{DEGREE_SYMBOL}.\n  The average high this week is {avg_max}{DEGREE_SYMBOL}.\n')
    return output
    
    
"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #5 Day Overview
        #calculate the number of rows in the input
    #The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021. 
        #return the min and its associated day(dictionary?), using the temp as a key?
    #The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
        #as above
    #The average low this week is 12.2°C.
        #avg of mins
    #The average high this week is 17.8°C.
        #avg of maxes



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    output = ""
    for i in weather_data:
        if i != False:
            date = convert_date(i[0])
            min = convert_f_to_c(i[1])
            max = convert_f_to_c(i[2])

            x = f"---- {date} ----\n  Minimum Temperature: {min}{DEGREE_SYMBOL}\n  Maximum Temperature: {max}{DEGREE_SYMBOL}\n\n"
            output = output + x
    return output
    
    


    
    #date in format: ---- Saturday 03 July 2021 ----
    #temp in format:Minimum Temperature: 13.9°C
    #Maximum Temperature: 20.0°C
