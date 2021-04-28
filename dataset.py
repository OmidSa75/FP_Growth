class Dataset:
    def __init__(self, data_path):
        self.data_path = data_path
        self.pp_data = self.preprocessing()

    def __call__(self):
        return self.pp_data

    def open_file(self):
        """open data file text"""
        with open(self.data_path, 'r') as f:
            data = f.readlines()

        return data

    def preprocessing(self):
        data = self.open_file()
        data = list(map(self.str2num, data))
        return data

    @staticmethod
    def str2num(line: str):
        line = line.split(' ')
        line.pop()
        line = list(map(int, line))

        return line
