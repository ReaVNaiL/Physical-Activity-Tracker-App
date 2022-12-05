# type: ignore
# CSV Data Loader
import os
import helpers.format_date as fd
import pandas as pd

# Classes
from models.csv_models.BaseSummaryModel import BaseSummaryModel
from models.csv_models.MetadataModel import MetadataModel
from models.csv_models.BaseSummaryFileList import BaseSummaryFileList
from gui.models.InputModel import InputModel


class DataHandler(InputModel):
    def __init__(self, input_model: InputModel = None):
        if input_model is None:
            return

    def load_csv(self, path):
        df = pd.read_csv(path)
        return df

    def parse_csv(self, csv, name):
        if name == "summary":
            return self.parse_data_summary(csv)
        # elif name == "metadata": # TBD
        # return self.parse_metadata_into_list(csv)

    def parse_data_summary(self, csv_data: pd.DataFrame):
        # Create a list of BaseSummaryModel objects
        data_summary = [BaseSummaryModel]
        data_summary.pop()

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
            data_summary.append(summary)

        return data_summary

    def get_path_list(self, date_range: list[str], file_index: str):
        """
        Given a list of dates, return a list of paths to the file_index.csv files
        i.e: file_index = "summary" or "metadata"
        The path structure is as follows:
        /data/{date}/{device}/{file_index}.csv
        """
        path_list = []

        # for each folder in the date range
        for date in date_range:
            # Get the path of the data folder
            data_path = os.path.join(os.path.dirname(__file__), "..\data")

            # Get the list of devices in the data folder
            device_folders = os.listdir(os.path.join(data_path, date))

            # For each device folder, get the path to the file_index.csv file
            for device in device_folders:
                path_list.append(
                    os.path.join(data_path, date, device, f"{file_index}.csv")
                )

        return path_list

    def get_date_from_path(self, path):
        """
        Given a path, return the date of the file
        """
        return path.split("\\")[-3]

    def get_device_from_path(self, path):
        """
        Given a path, return the device of the file
        """
        return path.split("\\")[-2]

    def get_headers(self, index) -> list[str]:
        """
        Given a file index, return the headers of the csv file
        """
        output = []
        if index == "Summary.csv":
            output = BaseSummaryModel().get_attr_names()
            print(output)
        elif index == "Metadata.csv":
            output = MetadataModel().get_attr_names()
        return output


# Testing only
if __name__ == "__main__":
    os.system("cls")
    
    # Testing Get Headers Method
    data_handler = DataHandler()

    data_handler.get_headers("Summary.csv")
    
    # # DONE: Given a date range, parse all CSV files into a list of BaseSummaryModel objects

    # # file type:
    # file_index = "summary"

    # """
    # Testing the get_path_list function
    # """
    # start_date = "2020-01-18T23:48:00Z"
    # start_date = fd.format_utc_to_standard(start_date)

    # end_date = "2020-01-20T23:48:00Z"
    # end_date = fd.format_utc_to_standard(end_date)

    # date_range = fd.get_date_range(start_date, end_date)

    # # Create the DataHandler object
    # data_handler = DataHandler()

    # # Assign the variables to the DataHandler object
    # data_handler.file_index = file_index
    # data_handler.start_date = start_date
    # data_handler.end_date = end_date

    # # Get the list of paths
    # path_list = data_handler.get_path_list(date_range, file_index)

    # new_summary_list = BaseSummaryFileList()

    # """
    # Testing the parse_summary_into_list function to BaseSummaryFileList
    # """
    # for path in path_list:
    #     """
    #     Consists of three steps.
    #     1- Load the csv file
    #     2- Parse the csv file into a list of BaseSummaryModel objects
    #     3- Append the list of BaseSummaryModel objects to the BaseSummaryFileList
    #     4- Optional: Assign the BaseSummaryFileList to a dictionary with the key being the date + device
    #     """
    #     csv_object = data_handler.load_csv(path)
    #     # summary_file = data_handler.parse_csv(csv_object, index_file)
    #     # new_summary_list.file_contents.append(summary_file)

    #     # '''
    #     # Building the dictionary:
    #     # '''
    #     # date = data_handler.get_date_from_path(path)
    #     # device = data_handler.get_device_from_path(path)
    #     # new_summary_list.file_contents_dict[f"{date}+{device}"] = summary_file

    # print("\nPath List: ")
    # for path in path_list:
    #     print("-", path)

    # # print("\nNew Summary List: ")
    # # for summary in new_summary_list.file_contents:
    # #     print(summary)
    # #     print("\n")
