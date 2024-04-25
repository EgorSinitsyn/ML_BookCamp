import pandas as pd
from encoding_functions.func_BinaryEncoder import BinaryEncoder

data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'M', 'M'],
    'Value': [10, 20, 15, 30, 25, 40, 45, 45]
}

df = pd.DataFrame(data)
encoder = BinaryEncoder(columns=['Category'])
encoded_df = encoder.fit_transform(df)
print(df)
print(encoded_df)
