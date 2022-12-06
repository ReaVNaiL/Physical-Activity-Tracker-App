import helpers.format_date as ft
from DataHandler import DataHandler


class PlottingHandler:
    def __init__(self):
        self._data_handler = DataHandler()
        self._data_handler.TEST_DATA_HANDLER()

    def TEST_PLOTTING_HANDLER(self):
        print("TEST_PLOTTING_HANDLER")
        
        # for each attribute of data_handler print the value
        self._data_handler.__repr__()
        
        self.data = self._data_handler.process_data_filtering(filter_enabled=False)

        x_axis = self.data["Unix Timestamp (UTC)"]
        y_axis = self.data["Eda avg"]
        
        new_time = ft.convert_timestamp_standard(x_axis.to_list()[2])
        print(new_time)
        
if __name__ == "__main__":
    plotting_handler = PlottingHandler()
    plotting_handler.TEST_PLOTTING_HANDLER()