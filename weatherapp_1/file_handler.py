import json


class FileHandler:
    def __init__(self, path_to_file):
        self.file = path_to_file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        try:
            with open(self.file) as file:
                return json.loads(file.read())
        except FileNotFoundError:
            print(f"File '{self.file}' not found.")
            self.data = None
        except json.JSONDecodeError:
            print(f"File '{self.file}' has invalid JSON format.")
            self.data = None

    def save_data_to_file(self):
        with open(self.file, mode="w") as file:
            file.write(json.dumps(self.data))

    def upload_new_city_to_data(self, city, date, result):
        self.data[city] = {date: result}



