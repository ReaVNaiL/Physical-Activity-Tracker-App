# type: ignore
# CSV Data Loader
import os
from models.csv_models.BaseSummaryModel import BaseSummaryModel
from models.csv_models.DeviceDataModel import DeviceDataModel
from models.csv_models.BaseSummaryFileList import BaseSummaryFileList
import format_date as fd
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
    elif name == "metadata": # TBD
        return parse_metadata_into_list(csv)


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

        # From UTC to Standard Time
        summary.UTC_date = fd.format_utc_to_standard(summary.UTC_date)

        # Add the summary object to the list
        summary_list.append(summary)

    return summary_list


def get_path_list(date_range: list[str], file_index: str):
    '''
    Given a list of dates, return a list of paths to the file_index.csv files
    i.e: file_index = "summary" or "metadata"
    The path structure is as follows:
    /data/{date}/{device}/{file_index}.csv
    '''
    path_list = []

    # for each folder in the date range
    for date in date_range:
        # Get the path of the data folder
        data_path = os.path.join(os.path.dirname(__file__), "..\data")

        # Get the list of devices in the data folder
        device_folders = os.listdir(os.path.join(data_path, date))

        # For each device folder, get the path to the file_index.csv file
        for device in device_folders:
            path_list.append(os.path.join(
                data_path, date, device, f"{file_index}.csv"))

    return path_list


def get_date_from_path(path):
    '''
    Given a path, return the date of the file
    '''
    return path.split("\\")[-3]


def get_device_from_path(path):
    '''
    Given a path, return the device of the file
    '''
    return path.split("\\")[-2]


# Testing only
if __name__ == "__main__":
    os.system("cls")
    # csv_sample_path = os.path.join(os.path.dirname(__file__), "../data/20200118/310/summary.csv")

    # csv_object = load_csv(csv_sample_path)
    # summary_file = parse_csv(csv_object, "summary")

    # # Print summary
    # print("Summary List: ")

    # avg = 0
    # sum_total = 0

    # for elem in summary_file:
    #     sum_total += elem.steps_count
    #     elem.eda_avg = round(elem.eda_avg, 2)

    # avg = sum_total / len(summary_file)
    # print("Average for the steps count is:", avg)

    # DONE: Given a date range, parse all CSV files into a list of BaseSummaryModel objects

    # file type:
    index_file = "summary"

    '''
    Testing the get_path_list function
    '''
    start_date = "2020-01-18T23:48:00Z"
    start_date = fd.format_utc_to_standard(start_date)

    end_date = "2020-01-20T23:48:00Z"
    end_date = fd.format_utc_to_standard(end_date)

    date_range = fd.get_date_range(start_date, end_date)
    path_list = get_path_list(date_range, index_file)

    new_summary_list = BaseSummaryFileList()

    '''
    Testing the parse_summary_into_list function to BaseSummaryFileList
    '''
    for path in path_list:
        '''
        Consists of three steps.
        1- Load the csv file
        2- Parse the csv file into a list of BaseSummaryModel objects
        3- Append the list of BaseSummaryModel objects to the BaseSummaryFileList
        4- Optional: Assign the BaseSummaryFileList to a dictionary with the key being the date + device
        '''
        csv_object = load_csv(path)
        summary_file = parse_csv(csv_object, index_file)
        new_summary_list.file_contents.append(summary_file)

        '''
        Building the dictionary:
        '''
        date = get_date_from_path(path) 
        device = get_device_from_path(path)
        new_summary_list.file_contents_dict[f"{date}+{device}"] = summary_file

    print("\nPath List: ")
    for path in path_list:
        print("-", path)

    # print("\nNew Summary List: ")
    # for summary in new_summary_list.file_contents:
    #     print(summary)
    #     print("\n")
