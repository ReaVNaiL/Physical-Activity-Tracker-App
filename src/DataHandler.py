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
    graph_filter: list[str]

    def __init__(self, input_model: InputModel = None):
        if input_model is None:
            return

    def process_data_filtering(self):
        """
        Given the input model, return a dataframe of the filtered data.
        1- Get the path date range
        2- Get the path list of the files using the file_index (summary or metadata) and subject_id (if applicable)
        3- Load the csv files into a dataframe
        """
        #
        print(self.start_date)
        print(self.end_date)
        print(self.graph_filter)

        date_range = fd.get_path_date_range(self.start_date, self.end_date)
        
        # If the date range is empty return None
        if len(date_range) == 0:
            return None
        
        path_list = data_handler.get_path_list(date_range, self.file_index, self.subject_id)
        
        for path in path_list:
            print(path)
            
        # Load the csv files into a dataframe
        df = pd.concat([pd.read_csv(path) for path in path_list], ignore_index=True)
        
        # Add the date columns copied from df["Datetime (UTC)"] after the Datetime (UTC) column
        df.insert(1, "Datetime (Standard)", df["Datetime (UTC)"].str.split(" ", expand=True)[0])
        
        # Now filtering the dataframe based on the graph_filter
        for column in df.columns:
            # If the column is datetime, skip it
            if column == "Datetime (UTC)" or column == "Datetime (Standard)": 
                continue
            
            if column not in self.graph_filter:
                df = df.drop(column, axis=1)
        
        return df

        
    def load_csv(self, path):
        df = pd.read_csv(path)
        return df

    def parse_csv(self, csv, name):
        if name == "summary":
            return self.parse_data_summary(csv)
        # elif name == "metadata": # TBD
        #     return self.parse_metadata_into_list(csv)

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

    def get_path_list(self, date_range: list[str], file_index: str, subject_id: str):
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
                # If the device is not in the filter, skip it
                if subject_id == "All Subjects":
                    pass
                elif device != subject_id:
                    continue
                path_list.append(os.path.join(data_path, date, device, f"{file_index}"))

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

    def get_headers(self, index):
        """
        Given a file index, return the headers of the csv file
        """
        name_path = os.path.join(os.path.dirname(__file__), "..\\data\\20200118\\310\\")
        columns = pd.read_csv(f"{name_path}{index}", nrows=0).columns
        # Dont include the first column
        return [str(column) for column in columns][1:]
    

# Testing only
if __name__ == "__main__":
    os.system("cls")

    """
    Testing Get Headers Method
    """
    data_handler = DataHandler()
    data_handler.get_headers("Summary.csv")


    """
    Testing the process_filtering function
    """
    start_date = "01/18/2020 12:00 AM"
    end_date = "01/21/2020 12:00 AM"
    filtering = ['Movement intensity', 'Rest']
    
    # Add the variables to the DataHandler object
    data_handler.start_date = start_date
    data_handler.end_date = end_date
    data_handler.graph_filter = filtering
    data_handler.file_index = "summary.csv"
    data_handler.device_OS = "All Devices"
    data_handler.subject_id = "310"

    # Process the data
    data_handler.process_data_filtering()
    
    
    # # DONE: Given a date range, parse all CSV files into a list of BaseSummaryModel objects
    # # file type:
    # file_index = "summary"

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
