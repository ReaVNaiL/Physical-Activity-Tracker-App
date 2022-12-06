from datetime import datetime as date
import os


def get_dates(summary_list):
    print("Before: ", summary_list[0].UTC_date)
    print("After: ", format_utc_to_standard(summary_list[0].UTC_date))
    print("\n")


def format_standard_to_utc(datetimeStandard: str):
    """
    Converts From: 01/17/2020 11:48:00 PM
    To: 2020-01-17T23:48:00Z
    """
    utc_time = date.strptime(datetimeStandard, "%M/%D/%Y %I:%M %p").strftime("%Y-%m-%dT%H:%M:%SZ")
    return utc_time


def format_utc_to_standard(datetimeUTC: str):
    """
    Converts From: 2020-01-17T23:48:00Z
    To: 01/17/2020 11:48 PM
    """
    standard_time = date.strptime(datetimeUTC, "%Y-%m-%dT%H:%M:%SZ").strftime("%m/%d/%Y %I:%M %p")
    return standard_time


def convert_timestamp_standard(timestamp: int):
    """
    Converts From: `1579298080`
    To: `01/17/2020 11:48 PM`
    """
    return date.utcfromtimestamp(int(timestamp / 1000)).strftime("%m/%d/%Y %I:%M %p")


def get_path_date_range(start_date: str, end_date: str) -> list[str]:
    """
    This assumes the start and end dates are in the format of 01/17/2020 11:48:00 PM
    """
    # Ignore the time for now
    start_date = start_date.split(" ")[0]
    end_date = end_date.split(" ")[0]

    # If the date is missing a leading 0, add it to the month less than 10 (i.e: 1/17/2020)
    if len(start_date.split("/")[0]) == 1:
        start_date = "0" + start_date
    if len(end_date.split("/")[0]) == 1:
        end_date = "0" + end_date

    # Get the path of the data folder (helpers\src\../data == ../../data)
    data_path = os.path.join(os.path.dirname(__file__), "../../data")

    # Get the list of dates in the data folder (YYYYMMDD)
    data_folders = os.listdir(data_path)

    # Convert each date from string YYYYMMDD to string MM/DD/YYYY
    date_range = []

    for folder in data_folders:
        # Convert the date from YYYYMMDD to Standard MM/DD/YYYY
        new_date = date.strptime(folder, "%Y%m%d").strftime("%m/%d/%Y")

        # Compare the date to the start and end date
        if new_date >= start_date and new_date <= end_date:
            date_range.append(folder)

    return date_range


if __name__ == "__main__":
    os.system("cls")
    csv_sample_path = os.path.join(os.path.dirname(__file__), "../data/20200118/310/summary.csv")

    # csv_object = load_csv(csv_sample_path)
    # new_list = parse_csv(csv_object, "summary")

    # get_dates(new_list)

    # Get the date range
    start_date = "2020-01-18T23:48:00Z"
    start_date = format_utc_to_standard(start_date)
    print(start_date)

    end_date = "2020-01-19T23:48:00Z"
    end_date = format_utc_to_standard(end_date)
    print(end_date)

    # Convert Back to UTC
    start_date = format_standard_to_utc(start_date)
    print(start_date)

    end_date = format_standard_to_utc(end_date)
    print(end_date)

    # Convert Back to Standard And Get Date Range
    start_date = format_utc_to_standard(start_date)
    end_date = format_utc_to_standard(end_date)
    date_range = get_path_date_range(start_date, end_date)
    print(date_range)


# # 10 July 2021, 10:54:27AM
# datetime.strftime("%-d %B %Y, %I:%M:%S%p")
