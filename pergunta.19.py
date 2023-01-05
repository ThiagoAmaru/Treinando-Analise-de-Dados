import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['date'] = pd.to_datetime(data['date'])

data.loc[data['price'] > 540000, 'standart'] = 'high'
data.loc[data['price'] < 540000, 'standart'] = 'low'


relatorio = data[['id', 'price', 'date', 'bedrooms', 'sqft_lot','standart']].sort_values('price', ascending= True)

print(relatorio)

#relatorio.to_csv('dataset/report_aula_02.csv', index= False)