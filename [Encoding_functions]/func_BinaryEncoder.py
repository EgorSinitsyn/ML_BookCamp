import pandas as pd
class BinaryEncoder:
    def __init__(self, columns):
        self.columns = columns
        self.binary_mapping = {}

    def fit(self, data):
        for col in self.columns:
            unique_values = data[col].unique()
            binary_repr_len = len(bin(len(unique_values) - 1)[2:])
            self.binary_mapping[col] = {
                value: format(index, '0{}b'.format(binary_repr_len))
                for index, value in enumerate(unique_values)
            }

    def transform(self, data):
        encoded_data = data.copy()
        for col, mapping in self.binary_mapping.items():
            encoded_data[col] = encoded_data[col].map(mapping)
        return encoded_data

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)
