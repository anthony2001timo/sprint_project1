from typing import Dict
import os
import requests
from pandas import DataFrame, read_csv, to_datetime

def get_public_holidays(public_holidays_url: str, year: str) -> DataFrame:
    """
    Get the public holidays for the given year for Brazil.

    Args:
        public_holidays_url (str): URL to the public holidays.
        year (str): The year to get the public holidays for.

    Raises:
        SystemExit: If the request fails.

    Returns:
        DataFrame: A DataFrame with the public holidays.
    """
    
    url = f"{public_holidays_url}/{year}/BR"
    
    try:
        
        response = requests.get(url)
        response.raise_for_status()  
    except requests.RequestException as e:
        raise SystemExit(f"Error fetching public holidays: {e}")

    
    holidays = DataFrame(response.json())

    
    holidays.drop(columns=["types", "counties"], errors="ignore", inplace=True)

    
    holidays["date"] = to_datetime(holidays["date"])

    return holidays


def extract(
    csv_folder: str, csv_table_mapping: Dict[str, str], public_holidays_url: str
) -> Dict[str, DataFrame]:
    """
    Extract the data from the CSV files and load them into DataFrames.

    Args:
        csv_folder (str): The path to the CSV folder.
        csv_table_mapping (Dict[str, str]): The mapping of the CSV file names to the
            table names.
        public_holidays_url (str): The URL to the public holidays.

    Returns:
        Dict[str, DataFrame]: A dictionary with keys as the table names and values as
        the DataFrames.
    """
    dataframes = {}

    
    for csv_file, table_name in csv_table_mapping.items():
        file_path = os.path.join(csv_folder, csv_file)  

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found: {file_path}")

        try:
            dataframes[table_name] = read_csv(file_path)
        except Exception as e:
            raise ValueError(f"Error reading file {csv_file}: {e}")

    
    holidays = get_public_holidays(public_holidays_url, "2017")
    dataframes["public_holidays"] = holidays

    return dataframes
