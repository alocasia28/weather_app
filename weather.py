import csv
from datetime import datetime
from statistics import mean

DEGREE_SYMBOL = "°C"

#this works with manual input, cannot test in unit test yet(will probably get used for the daily summary)
def format_temperature(temp):
    formatted_temp = str(temp) + DEGREE_SYMBOL
    print(formatted_temp)
  


#tested working
def convert_date(iso_string):
    converted_date = datetime.fromisoformat(iso_string) #convert ISO format to date
    formatted_date = converted_date.strftime('%A %d %B %Y') #return date in format of Weekday DD Month YYYY e.g. Wednesday 25 October 2023
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
    average = mean(float_list)
    return float(average)




def load_data_from_csv(csv_file):
    file = open(csv_file,"r")
    data = list(csv.reader(file,delimiter=","))
    file.close() 
    print(data)
    
    x = []
    for i in data[1:]:
        x.append([(i[0]),int(i[1]),int(i[2])])
    return x
 ##Need to handle blank lines
    
    
"""Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
"""


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
