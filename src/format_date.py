from datetime import datetime as date
import os 
from load_csv import *

def get_dates(summary_list):
    print("Before: ", summary_list[0].UTC_date)
    print("After: ", format_utc_to_standard(summary_list[0].UTC_date))
    print("\n")
   
def format_standard_to_utc(datetimeStandard: str):
    # 01/17/2020 11:48:00 PM to 2020-01-17T23:48:00Z
    utc_time = date.strptime(datetimeStandard, '%m/%d/%Y %I:%M:%S %p').strftime('%Y-%m-%dT%H:%M:%SZ')
    return utc_time
    
def format_utc_to_standard(datetimeUTC: str):
    # 2020-01-17T23:48:00Z to 01/17/2020 11:48:00 PM
    standard_time = date.strptime(datetimeUTC, '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y %I:%M:%S %p')
    return standard_time
    
if __name__ == "__main__":
    os.system("cls")
    csv_sample_path = os.path.join(os.path.dirname(__file__), "../data/20200118/310/summary.csv")

    csv_object = load_csv(csv_sample_path)
    new_list = parse_csv(csv_object, "summary")

    get_dates(new_list) 
    
    
    
    
# # 10 July 2021, 10:54:27AM
# datetime.strftime("%-d %B %Y, %I:%M:%S%p")