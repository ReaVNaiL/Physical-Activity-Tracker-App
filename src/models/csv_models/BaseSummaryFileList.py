from BaseSummaryModel import BaseSummaryModel
from dataclasses import dataclass

# Create a class to a list of BaseSummaryModel objects

@dataclass(init=True)
class BaseSummaryFileList():
    file_contents: list = [BaseSummaryModel]
    