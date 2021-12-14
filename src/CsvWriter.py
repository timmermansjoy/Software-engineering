class CsvWriter():
    @staticmethod
    def write_file(data, filename):
        data.to_csv(f'./data/{filename}', index=False)