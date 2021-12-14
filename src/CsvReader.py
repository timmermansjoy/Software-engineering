import pandas as pd


class CsvReader:
    @staticmethod
    def read_file(filename):
        data = pd.read_csv(f"./data/{filename}")
        if "group_number" not in data:
            data["group_number"] = 0
        return data
