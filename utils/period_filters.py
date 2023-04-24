import csv
import calendar
from typing import Tuple, List
from datetime import datetime, timedelta

def load_csv(filename: str) -> List[List[str]]:
    """
    Loads data from a CSV file and returns a list of lists.
    
    Args:
    filename (str): The name of the CSV file to load.
    
    Returns:
    List[List[str]]: A list of lists where each sub-list represents a row in the CSV file.
    
    Raises:
    ValueError: If the file does not exist.
    """
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        raise ValueError(f"The file {filename} does not exist")

def check_csv_has_created_at_column(input_data: List[List[str]]) -> bool:
    """
    Checks if a list of lists containing data from a CSV file has a 'created_at' column.
    
    Args:
    input_data (List[List[str]]): A list of lists where each sub-list represents a row in the CSV file.
    
    Returns:
    bool: True if the 'created_at' column is present, False otherwise.
    """
    header = input_data[0]
    if "created_at" in header:
        return True
    else:
        return False

def get_period_filter(period_type: str) -> Tuple[datetime, datetime]:
    """
    Returns a tuple of start and end datetime objects based on the given period type.
    
    Args:
    - period_type (str): type of period for filtering the data.
        Valid values are: "today", "month", "trimester", "year", "custom".
        
    Returns:
    - tuple: A tuple of start and end datetime objects based on the given period type.
    
    Raises:
    - ValueError: if invalid period type is provided.
    - ValueError: if invalid date format is provided for custom period type.
    """

    try:
        now = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        if period_type == "today":
            date_start = now
            date_end = now + timedelta(days=1) - timedelta(microseconds=1)
        elif period_type == "month":
            date_start = now.replace(day=1)
            next_month = now.replace(day=28) + timedelta(days=4)
            date_end = next_month - timedelta(days=next_month.day)
        elif period_type == "trimester":
            quarter = (now.month - 1) // 3 + 1
            year_start = now.year
            if quarter == 1:
                year_start -= 1
            date_start = datetime(year_start, 3 * quarter - 2, 1)
            last_day = calendar.monthrange(now.year, 3 * quarter)[1]
            date_end = datetime(now.year, 3 * quarter, last_day) + timedelta(days=1) - timedelta(microseconds=1)
        elif period_type == "year":
            date_start = now.replace(month=1, day=1)
            date_end = now.replace(month=12, day=31)
        elif period_type == "custom":
            date_start_string = input("Enter start date in yyyy-mm-dd format: ")
            date_start = datetime.strptime(date_start_string, '%Y-%m-%d')
            date_end_string = input("Enter end date in yyyy-mm-dd format: ")
            date_end = datetime.strptime(date_end_string, '%Y-%m-%d')
        else:
            raise ValueError("Invalid period type provided. Valid values are: today, month, trimester, year, custom")

        date_start = date_start.replace(hour=0, minute=0, second=0, microsecond=0)
        date_end = date_end.replace(hour=23, minute=59, second=59, microsecond=999999)
        # return (date_start, date_end)
        return (date_start.strftime('%Y-%m-%d %H:%M:%S.%f') + "+00", date_end.strftime('%Y-%m-%d %H:%M:%S.%f') + "+00")

    except ValueError:
        if period_type == "custom":
            raise ValueError("Invalid date format provided. Please provide date in yyyy-mm-dd format.")
        else:
            raise ValueError("Invalid period type provided. Valid values are: today, month, trimester, year, custom")

def filter_csv_with_period(input_data: List[List[str]], date_range: Tuple[datetime, datetime]) -> List[List[str]]:
    """
    Filters the input CSV data to only include rows with a "created_at" value within the given date range.

    Args:
        input_data (List[List[str]]): A list of lists representing the CSV data.
        date_range (Tuple[datetime, datetime]): A tuple representing the date range to filter on.

    Returns:
        List[List[str]]: A list of lists representing the filtered CSV data.
    """
    header = input_data[0]
    data = input_data[1:]
    output_data = []
    start_date = datetime.strptime(date_range[0][:19], '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(date_range[1][:18], '%Y-%m-%d %H:%M:%S')
    for row in data:
        date_string = row[header.index('created_at')]
        date = datetime.strptime(date_string[:10], '%Y-%m-%d')
        if start_date <= date <= end_date:
            output_data.append(row)
    return output_data
