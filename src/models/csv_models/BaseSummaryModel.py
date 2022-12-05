# Create BaseSummaryModel class
# {
#     "UTC_date": datetime,
#     "timezone": int,
#     "unix_time_stamp": str,
#     "acc_magnitude_avg": float,
#     "eda_avg": float,
#     "temp_avg": float,
#     "movement_intensity": int,
#     "steps_count": int,
#     "rest": int,
#     "on_wrist": bool
# }
from dataclasses import dataclass

@dataclass(init=True)
class BaseSummaryModel(object):
    """ BaseSummaryModel For Summary.csv Data """
    UTC_date: str = ""
    timezone: int = 0
    unix_time_stamp: float = 0.0
    acc_magnitude_avg: float = 0.0
    eda_avg: float = 0.0
    temp_avg: float = 0.0
    movement_intensity: int = 0
    steps_count: int = 0
    rest: int = 0
    on_wrist: bool = True

    def __iter__ (self):
        return iter(self.__dict__.values())
    
    def get_attr_names(self):
        attrs = []
        for key in self.__dict__.keys():
            attrs.append(key)  
        return attrs