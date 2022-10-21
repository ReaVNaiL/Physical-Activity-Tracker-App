# type: ignore 
# CSV Data Loader
import os
from models.csv_models.BaseSummaryModel import BaseSummaryModel
from models.csv_models.DeviceDataModel import DeviceDataModel 
import pandas as pd
 

# @dataclass(order=True)
# class BaseSummaryModel:
#     """ BaseSummaryModel For Summary.csv Data """
    # UTC_date: str
    # timezone: int
    # unix_time_stamp: str
    # acc_magnitude_avg: float
    # eda_avg: float
    # temp_avg: float
    # movement_intensity: int
    # steps_count: int
    # rest: int
    # on_wrist: bool

def load_csv(path):
    df = pd.read_csv(path)
    return df

def parse_csv(csv, name):
    if name == "summary":
        return parse_summary_into_list(csv)
    
def parse_summary_into_list(csv_data: pd.DataFrame):
    # Create a list of BaseSummaryModel objects
    summary_list = [BaseSummaryModel]
    summary_list.pop()
    
    csv_columns = [str(columns) for columns in csv_data.columns]
    
    # For each row add a BaseSummaryModel object to the list
    for index, row in csv_data.iterrows():
        # For each column in the row, create a BaseSummaryModel object
        summary = BaseSummaryModel()

        # Fill the class
        class_iter = 0
        for property in summary.__dict__:
            summary.__dict__[property] = row[csv_columns[class_iter]]
            class_iter += 1
        
        # # Print each item in summary
        # for item in summary:
        #     print(item)
            
        # print(f"Class Properties: {dir(summary)}")
        # print("\n\n")
        
        # Add the summary object to the list
        summary_list.append(summary)
        
        
    return summary_list


# Testing only
if __name__ == "__main__":
    os.system("cls")
    csv_sample_path = os.path.join(os.path.dirname(__file__), "../data/20200118/310/summary.csv")

    csv_object = load_csv(csv_sample_path)
    new_list = parse_csv(csv_object, "summary") 

    # Print summary
    print("Summary List: ")

    avg = 0
    sum_total = 0

    for elem in new_list:
        sum_total += elem.steps_count
        elem.eda_avg = round(elem.eda_avg, 2)

    avg = sum_total / len(new_list)
    print("Average for the steps count is:", avg)