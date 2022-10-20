from dataclasses import dataclass

@dataclass(frozen=True, order=True, repr=True, eq=True)
class AveragesModel:
    ACC: float = None
    EDA: float = None
    Temp: float = None