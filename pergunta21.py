import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['date'] = pd.to_datetime(data['date'])

data['house_age'] = 'tempo'

data.loc[data['date'] > '2014-01-01', 'house_age'] = 'new_house'

data.loc[data['date'] < '2014-01-01', 'house_age' ]= 'old_house'

print(data.head(10))

# Crie uma nova coluna chamada "house_age"
# Se o valor da coluna "date" for maior que 2014-01-01 => 'new_house"
# Se o valor da coluna "date" for menor que 2014-01-01 => 'old_house"