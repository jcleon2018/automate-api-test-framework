import json
import os

class DataLoader:
    @staticmethod
    def load_data(file_name="test_data.json"):
        file_path = os.path.join(os.path.dirname(__file__), "../config", file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Test data file not found: {file_path}")
        with open(file_path, "r") as file:
            return json.load(file)

