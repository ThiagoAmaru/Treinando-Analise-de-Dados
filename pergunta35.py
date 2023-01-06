import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['yr_renovated'] = data['yr_renovated'].apply(lambda x: pd.to_datetime('1970', format= '%Y')  if x == 0 else pd.to_datetime( x, format= '%Y') )

data['dormitory_type'] = 'dormitorio'
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartament'
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'

data.loc[(data['dormitory_type'] == 'apartament') & (data['yr_renovated'] == pd.to_datetime('2015', format= '%Y')), 'id'].shape[0]

print(data.loc[(data['dormitory_type'] == 'apartament') & (data['yr_renovated'] == pd.to_datetime('2015', format= '%Y')), 'id'].shape[0])





# 15. Quantos imoveis do tipo apartment, foram reformados em 2015
# erro na correcao