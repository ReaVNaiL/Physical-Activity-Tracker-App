# Create DeviceDataModel class
# {
#     "UTC_date": datetime,
#     "timezone": int,
#     "firmware_version": str,
#     "app_name": str,
#     "app_version": str,
#     "mobile_os": str,
#     "mobile_os_version": str,
#     "gtcs_algorithm_version": str,
# }

import datetime
from dataclasses import dataclass

@dataclass(init=True, order=True)
class DeviceDataModel:
    """ DeviceDataModel For DeviceData.csv Data """
    timezone: int
    UTC_date: str
    firmware_version: str
    app_name: str = "Mate"
    app_version: str = ""
    mobile_os: str = ""
    mobile_os_version: str = ""
    gtcs_algorithm_version: str = ""
                  
    def __iter__ (self):
        return iter(self.__dict__.values())
