import os
import json
import pandas as pd
import requests as rs
from pathlib import Path

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

def main() -> None:
    DATA_DIR: str = Path.cwd()
    api: str = "https://www.unihomes.co.uk/student-accommodation/leicester?page={}&reload=true"
    fetch(api, 14, DATA_DIR)
    
if __name__ == "__main__":
    main()