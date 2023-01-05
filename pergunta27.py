import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data = data.drop(['sqft_living15', 'sqft_lot15'], axis=1)

print(data)
# Delete as colunas
# 	sqft -> living e lot.