import json
import os

import requests


def get_uniprot_entry(entry_id):
    """Get UniProt entry data using the UniProt REST API.

    Args:
        entry_id (str): UniProt entry ID

    Returns:
        dict: UniProt entry data in JSON format if successful, None otherwise
    """
    base_url = f"https://rest.uniprot.org/uniprotkb/{entry_id}"
    params = {
        "format": "json",
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def main():
    # Change the working directory to the directory of this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Read input IDs from a file
    with open("./input_ids.txt", "r") as file:
        entry_ids = [line.strip() for line in file.readlines() if line.strip()]

    # Get UniProt entry data for each entry ID
    if entry_ids:
        for entry_id in entry_ids:
            print(f"Getting UniProt entry data for {entry_id}...")
            entry_data = get_uniprot_entry(entry_id)

            if entry_data:
                # Save results to a file named after the entry ID using json.dumps()
                with open(f"{entry_id}.json", "w") as f:
                    json.dump(entry_data, f, indent=4)
                print(f"Results saved to {entry_id}.json")
            else:
                print(f"Failed to get UniProt entry data for {entry_id}")


if __name__ == "__main__":
    main()
