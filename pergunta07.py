import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

casas = len(data[['bathrooms']])
casas_2_banheiros = data[['bathrooms']] == 2
soma_casas = (data.loc[data['bathrooms'] == 2]).shape

print('07P: Quantas casas possuem 2 banheiros?')
print('Das', casas, 'casas', soma_casas[0], 'possuem dois banheiros')
