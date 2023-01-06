import pandas as pd
data = pd.read_csv('dataset/kc_house_data.csv')

data['condition_type'] = 'condicao'

data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[data['condition'] == 3 , 'condition_type'] = 'regular'
data.loc[data['condition'] == 4 , 'condition_type'] = 'regular'
data.loc[data['condition'] > 4, 'condition_type'] = 'good'

data['date'] = pd.to_datetime(data['date'])
data['house_age'] = 'tempo'
data.loc[data['date'] > pd.to_datetime('2014-01-01'), 'house_age'] = 'new_house'
data.loc[data['date'] < pd.to_datetime('2014-01-01'), 'house_age' ]= 'old_house'


# 13. Quantos imoveis estao com a condicao igual a good e sao "new house"

print(data.loc[(data['house_age'] == 'new_house') & (data['condition_type'] == 'good') , 'id'].shape[0])