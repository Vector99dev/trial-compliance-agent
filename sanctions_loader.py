import os
import csv

DATA_DIR = "data/sanctions"

class SanctionsDataLoader:
    def __init__(self):
        self.sanctioned_names = set()
        self.load_data()

    def load_data(self):
        # Load OFAC SDN CSV as example
        sdn_path = os.path.join(DATA_DIR, "ofac_sdn.csv")
        with open(sdn_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row.get('Name')
                if name:
                    self.sanctioned_names.add(name.strip().lower())

        # TODO: Repeat for other files...

    def is_sanctioned(self, name: str) -> bool:
        return name.strip().lower() in self.sanctioned_names

