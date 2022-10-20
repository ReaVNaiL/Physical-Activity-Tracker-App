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

import datetime
from dataclasses import dataclass

@dataclass(order=True)
class BaseSummaryModel:
    """ BaseSummaryModel For Summary.csv Data """
    timezone: int
    UTC_date: str
    unix_time_stamp: str
    acc_magnitude_avg: float
    eda_avg: float
    temp_avg: float
    movement_intensity: int = 0
    steps_count: int = 0
    rest: int = 0
    on_wrist: bool = True