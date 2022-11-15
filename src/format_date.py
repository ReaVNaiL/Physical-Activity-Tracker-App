from datetime import datetime as date
import os 
from load_csv import *

def get_dates(summary_list):
    print("Before: ", summary_list[0].UTC_date)
    print("After: ", format_utc_to_standard(summary_list[0].UTC_date))
    print("\n")
   
def format_standard_to_utc(datetimeStandard: str):
    ''' 
    Converts From: 01/17/2020 11:48:00 PM
    To: 2020-01-17T23:48:00Z 
    '''
    utc_time = date.strptime(datetimeStandard, '%m/%d/%Y %I:%M:%S %p').strftime('%Y-%m-%dT%H:%M:%SZ')
    return utc_time
    
def format_utc_to_standard(datetimeUTC: str):
    ''' 
    Converts From: 2020-01-17T23:48:00Z 
    To: 01/17/2020 11:48:00 PM
    '''
    standard_time = date.strptime(datetimeUTC, '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y %I:%M:%S %p')
    return standard_time

def get_date_range(start_date: str, end_date: str):
    '''
    This assumes the start and end dates are in the format of 01/17/2020 11:48:00 PM
    '''
    # Ignore the time for now
    start_date = start_date.split(" ")[0]
    end_date = end_date.split(" ")[0]
    
    # Get the path of the data folder
    data_path = os.path.join(os.path.dirname(__file__), "../data")
    
    # Get the list of dates in the data folder (YYYYMMDD)
    data_folders = os.listdir(data_path)
    
    # Convert each date from string YYYYMMDD to string MM/DD/YYYY
    data_range = []
    
    for folder in data_folders:
        # Convert the date from YYYYMMDD to Standard MM/DD/YYYY
        new_date = date.strptime(folder, '%Y%m%d').strftime('%m/%d/%Y')
        
        # Compare the date to the start and end date
        if new_date >= start_date and new_date <= end_date:
            data_range.append(folder)
            
    return data_range
    
if __name__ == "__main__":
    os.system("cls")
    csv_sample_path = os.path.join(os.path.dirname(__file__), "../data/20200118/310/summary.csv")

    csv_object = load_csv(csv_sample_path)
    new_list = parse_csv(csv_object, "summary")

    get_dates(new_list) 

    # Get the date range
    start_date = "2020-01-18T23:48:00Z"
    start_date = format_utc_to_standard(start_date)
    
    end_date = "2020-01-19T23:48:00Z"
    end_date = format_utc_to_standard(end_date)
    
    date_range = get_date_range(start_date, end_date)
    print(date_range)
    
    
    
# # 10 July 2021, 10:54:27AM
# datetime.strftime("%-d %B %Y, %I:%M:%S%p")