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

@dataclass(order=True)
class DeviceDataModel:
    """ DeviceDataModel For DeviceData.csv Data """
    timezone: int = 0
    UTC_date: datetime = None
    firmware_version: str = None
    app_name: str = "Mate"
    app_version: str = None
    mobile_os: str = None
    mobile_os_version: str = None
    gtcs_algorithm_version: str = None
        
        
