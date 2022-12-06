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
        super().file_index = input_model.file_index
        super().subject_id = input_model.subject_id
        super().device_OS = input_model.device_OS
        super().is_standard_time = input_model.is_standard_time
        super().start_date = input_model.start_date
        super().end_date = input_model.end_date


    def process_data_filtering(self):
        """
        Given the input model, return a dataframe of the filtered data.
        1- Get the path date range
        2- Get the path list of the files using the file_index (summary or metadata) and subject_id (if applicable)
        3- Load the csv files into a dataframe
        4- Filter the dataframe based on the input model
        5- Return the filtered dataframe
        """
        #
        print("Start Date: ", self.start_date)
        print("End Date: ", self.end_date)
        print("File Index: ", self.file_index)
        print("Subject ID: ", self.subject_id)
        print("Device OS: ", self.device_OS)
        print("Is Standard Time: ", self.is_standard_time)
        print("Graph Filter: ", self.graph_filter, "\n")

        date_range = fd.get_path_date_range(self.start_date, self.end_date)
        
        # If the date range is empty return None
        if len(date_range) == 0:
            return pd.DataFrame()
        
        path_list = self.get_path_list(date_range, self.file_index, self.subject_id)
        
        if len(path_list) == 0:
            return pd.DataFrame()
        
        # Load the csv files into a dataframe
        record_df = self.import_csv_data_frames(path_list)

        # Add the date columns copied from df["Datetime (UTC)"] with the correct standard time
        # after the Datetime (UTC) column
        self.generate_standard_time_column(record_df)

         # Remove the data that is not in the date range
        record_df = self.filter_dates(record_df, self.start_date, self.end_date)

        # Now filtering the dataframe based on the graph_filter
        for column in record_df.columns:
            # If the column is datetime, skip it
            if column == "Datetime (UTC)" or column == "Datetime (Standard)": 
                continue
            
            if column not in self.graph_filter:
                record_df = record_df.drop(column, axis=1)
        
        record_df = self.extract_datetime_format(record_df)

        # Return the filtered dataframe
        return record_df

    def extract_datetime_format(self, record_df: pd.DataFrame):
        """
        If the `is_standard_time` is `True`, then extract the `Datetime (Standard)` column
        else extract the `Datetime (UTC)` column
        """
        if self.is_standard_time:
            record_df = record_df.drop('Datetime (UTC)', axis=1)
        else: 
            record_df = record_df.drop('Datetime (Standard)', axis=1)
        return record_df

    def generate_standard_time_column(self, csv_data: pd.DataFrame):
        """
        Given a `dataframe`, add a `column` with the standard time named `Datetime (Standard)`
        """
        csv_data.insert(1, "Datetime (Standard)", csv_data["Datetime (UTC)"].apply(fd.format_utc_to_standard))

    def import_csv_data_frames(self, path_list):
        """
        Given a `relative` list of paths, return a `dataframe` with all the data
        
        RETURN:
            The `path_list` is a list of paths relative to the current directory\n
            The `dataframe` will be a `concatenation` of all the csv files in the `path_list`
        """
        return pd.concat([pd.read_csv(path) for path in path_list], ignore_index=True)

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

    def filter_dates(self, csv_data: pd.DataFrame, start_date: str, end_date: str):
        """
        Removes the `datarows` that is not in the date range: `start_date` and `end_date`
        
        Args:
            `csv_data` (pd.DataFrame) : The dataframe to filter

            `start_date` (str) : The start date of the range in the format of MM/DD/YYYY HH:MM AM/PM
            
            `end_date` (str) : The end date of the range in the format of MM/DD/YYYY HH:MM AM/PM
        """
        # Remove the data that is not in the date range
        csv_data = csv_data[(csv_data["Datetime (Standard)"] >= start_date) & (csv_data["Datetime (Standard)"] <= end_date)]

        return csv_data

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
    # os.system("cls")

    """
    Testing Get Headers Method
    """
    print("\n\n#################################### Get Headers ##########################################")
    data_handler = DataHandler()
    print(data_handler.get_headers("summary.csv"))


    """
    Testing the process_filtering function
    """
    print("\n\n#################################### Process Filtering ####################################")
    start_date = "01/20/2020 12:00 AM"
    end_date = "01/21/2020 12:00 AM"
    filtering = ['Movement intensity', 'Rest']
    
    # Add the variables to the DataHandler object
    data_handler.start_date = start_date
    data_handler.end_date = end_date
    data_handler.graph_filter = filtering
    data_handler.file_index = "summary.csv"
    data_handler.device_OS = "All Devices"
    data_handler.subject_id = "310"
    data_handler.is_standard_time = True

    # Process the data
    print(data_handler.process_data_filtering())
    

    
    # # DONE: Given a date range, parse all CSV files into a list of BaseSummaryModel objects
    # file type:
    file_index = "summary.csv"

    """
    Get the list of paths to the csv files with parsed data
    """
    print ("\n\n#################################### Get Path List #####################################")

    # start_date = "2020-01-20T23:48:00Z"
    # start_date = fd.format_utc_to_standard(start_date)

    # end_date = "2020-01-20T23:48:00Z"
    # end_date = fd.format_utc_to_standard(end_date)

    date_range = fd.get_path_date_range(start_date, end_date)

    # Create the DataHandler object
    data_handler = DataHandler()

    # Assign the variables to the DataHandler object
    data_handler.file_index = file_index
    data_handler.start_date = start_date
    data_handler.end_date = end_date

    # Get the list of paths
    path_list = data_handler.get_path_list(date_range, file_index, "310")

    for path in path_list:
        print(path)
    
    print("\n")