import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['yr_renovated'] = data['yr_renovated'].apply(lambda x: pd.to_datetime('1970', format= '%Y-%m-%d')  if x == 0 else pd.to_datetime( x, format= '%Y-%m-%d') )


print(data['yr_renovated'])
print(data['yr_renovated'].dtypes)

# 7. Modifique a Coluna 
# 	yr_renovated para date
# Mudei para o metodo apply e lambda