import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['dormitory_type'] = 'dormitorio'
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartament'
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'

data = data[['id', 'dormitory_type', 'price']].sort_values('price', ascending= False)


print(data.loc[data['dormitory_type'] == 'studio'].head(1))



# 14. Qual o valor do imovel mais caro do tipo "studio"