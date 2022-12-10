from dataclasses import dataclass, field

@dataclass(init=True)
class InputModel():
    '''
    This class is used to store the input data from the user.
    
    Attributes:
        `file_index`: A string that contains the file index of the data to be loaded. (e.g. "summary", "metadata")
        `subject_id`: A string that contains the subject id of the data to be loaded.
        `device_OS`: A string that contains the device OS of the data to be loaded.
        `start_date`: A string that contains the start date of the data to be loaded.
        `end_date`: A string that contains the end date of the data to be loaded.
    '''
    file_index: str = field(default="summary.csv")
    subject_id: str = field(default="310")
    device_OS: str = field(default="Android")
    is_standard_time: bool = field(default=False)
    start_date: str = field(default="01/18/2020 12:00 AM")
    end_date: str = field(default="01/21/2020 12:00 AM")
