from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, order=True)
class UserDataDetailsModel:
    name: str
    user_id: str
    location: str
    date: datetime
    