from dataclasses import dataclass, field

@dataclass(init=True)
class InputModel():
    '''
    This class is used to store the input data from the user.
    
    Attributes:
        date_range: A list of strings that contains the start and end date of the data to be loaded.
        file_index: A string that contains the file index of the data to be loaded. (e.g. "summary", "metadata")
        device: A string that contains the device of the data to be loaded.
        data_type: A string that contains the data type of the data to be loaded.
    '''
    file_index: str = field(default="summary")
    subject_id: str = field(default="310")
    device_OS: str = field(default="Android")
    is_standard_time: bool = field(default=False)
    date_range: list[str] = field(default_factory=list)
