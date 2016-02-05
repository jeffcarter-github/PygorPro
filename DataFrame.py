import time
import pandas as pd
import os


class DataFrame():
    def __init__(self, name=None, project=None, source=None):
        self.name = name
        self.project = project
        self.source = source
        self.date_created = time.asctime()
        self.data = None
        self.n_columns = None
        self.n_rows = None

    def from_text(self, text_file_path):
        pass

    def from_csv(self, csv_file_path):
        self.name = os.path.split(csv_file_path)[1]
        self.source = csv_file_path
        if self.data is None:
            self.data = pd.read_csv(csv_file_path)
            self.update_meta_data()

    def get_keys(self):
        return self.data.keys()

    def get_dataFrame(self):
        return self.data

    def get_point(self, label, row):
        return self.data[label][row]

    def get_series(self, label):
        return self.data[label]

    def update_meta_data(self):
        self.n_rows, self.n_columns = self.data.shape
