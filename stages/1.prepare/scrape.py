import os
import json
import pandas as pd
import requests as rs
from pathlib import Path
from typing import List

def fetch(api: str, pages: int, path: str) -> None:
    """
    Fetch data from the API and save as JSON files.
    
    Args:
    api(str): The API endpoint with a placeholder for page number.
    path(str): The path where the json files will be saved.
    pages(int): Number of pages to fetch.
    
    Raises:
    ValueError: if any of the arguments are invalid.
    """

    if not isinstance(api, str) or not api:
        raise ValueError("The API must be a non-empty string.")
    if not isinstance(path, str) or not path:
        raise ValueError("The path must be a non-empty string")
    if not isinstance(pages, int) or pages <= 1:
        raise ValueError("The number of pages must be a positive integer.")

    if not os.path.isdir(path):
        os.mkdir(path)

    for page in range(pages):
        try:
            response = rs.get(api.format(page + 1), headers={"accept": "application/json"})
            response.raise_for_status()  # Check for HTTP request errors
            data = response.json()  # Parse JSON response

            with open(os.path.join(path, f"{page}.json"), mode="w") as file:
                json.dump(data, file)  # Save JSON data to file

        except rs.RequestException as e:
            print(f"Failed to fetch data for page {page + 1}: {e}")
            continue

def load_and_process(path: str) -> pd.DataFrame:
    """
    Load data from JSON files, process it, and return a DataFrame.
    
    Args:
    path(str): The path from which JSON files will be loaded.
    
    Returns:
    pd.DataFrame: DataFrame containing the processed data.
    
    Raises:
    ValueError: If the data path is not a string or is empty.
    """

    if not isinstance(path, Path) or not path:
        raise ValueError("The data path must be a non-empty string.")
    
    properties_list: List[dict] = []

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if not os.path.isfile(file_path):
            print(f"Skipping non-file {filename}")
            continue
        with open(file_path) as file:
            try:
                data = json.load(file)  # Load JSON data from file

                for property in data.get("properties", []):
                    landlord = property.get("landlord", {})
                    property_data = {
                        "id": property.get("id"),
                        "lat": property.get("latitude"),
                        "long": property.get("longitude"),
                        "postcode": property.get("postcode"),
                        "price": property.get("price"),
                        "rooms": property.get("roomsAvailableCount"),
                        "images": property.get("imagesCount"),
                        "type": property.get("type"),
                        "addressShort": property.get("addressShort"),
                        "street": property.get("street"),
                        "landlord_id": landlord.get("id"),
                        "fname": landlord.get("first_name"),
                        "sname": landlord.get("last_name"),
                        "company": landlord.get("company"),
                        "added": property.get("added")
                    }
                    properties_list.append(property_data)  # Add property data to list
            except json.JSONDecodeError as e:
                print(f"Failed to load JSON data from {filename}: {e}")
                continue

    df = pd.DataFrame(properties_list)  # Create DataFrame from list
    return df

def main() -> None:
    DATA_DIR: str = Path.cwd().joinpath("stages","1.collect","data")
    #api: str = "https://www.unihomes.co.uk/student-accommodation/leicester?page={}&reload=true"
    #fetch(api, 14, DATA_DIR)
    df = load_and_process(DATA_DIR)
    print(df.head(10))
    df.to_csv("house.csv", index=False)
        
if __name__ == "__main__":
    main()