import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['dormitory'] = 'dormitorio'

data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'

data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartament'

data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'


print(data.head(10))

# 2. Crie uma nova coluna chamada "dormitory_type"
# 	se o valor da coluna 'bedrooms, for igual a 1 => 'studio'
#   se o valor da coluna 'bedrooms, for igual a 2 => 'apartament'
#   se o valor da coluna 'bedrooms, for igual maior que dois => 'house'
