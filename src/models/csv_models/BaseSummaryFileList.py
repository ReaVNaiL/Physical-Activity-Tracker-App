from dataclasses import dataclass, field

# Create a class to a list of BaseSummaryModel objects

@dataclass(init=True)
class BaseSummaryFileList():
    file_contents: list = field(default_factory=list)
    file_contents_dict: dict = field(default_factory=dict)

    