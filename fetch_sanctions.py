import os
import requests

DATA_DIR = "data/sanctions"

# Make sure directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# List of sources
SOURCES = {
    "ofac_sdn.csv": "https://www.treasury.gov/ofac/downloads/sdn.csv",
    "un_sanctions.xml": "https://scsanctions.un.org/resources/xml/en/consolidated.xml",
    "eu_sanctions.csv": "https://webgate.ec.europa.eu/europeaid/fsd/fsf/public/files/Consolidated_list_of_sanctions.csv",
    "uk_sanctions.csv": "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1155107/UK_Sanctions_List.csv",
    # For PEPs use OpenSanctions dump link or their API (may require API key)
    "pep_list.csv": "https://data.opensanctions.org/datasets/latest/peps.csv",
}

def fetch_files():
    for filename, url in SOURCES.items():
        print(f"Fetching {filename} ...")
        response = requests.get(url)
        if response.status_code == 200:
            path = os.path.join(DATA_DIR, filename)
            with open(path, "wb") as f:
                f.write(response.content)
            print(f"Saved to {path}")
        else:
            print(f"Failed to fetch {url}: Status {response.status_code}")

