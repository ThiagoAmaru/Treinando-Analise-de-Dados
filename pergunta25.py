import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['yr_built'] = pd.to_datetime(data['yr_built'])

print(data['yr_built'].dtypes)

# 6. Modifique a Coluna yr_built para o tipo date