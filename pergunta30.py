import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

andares = data.loc[data['floors'] == 2]

print(andares.shape[0])
# Quantos imoves tem 2 andares