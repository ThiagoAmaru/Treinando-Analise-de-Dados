import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')


data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])

print(data['yr_renovated'].dtypes)

# 7. Modifique a Coluna 
# 	yr_renovated para date