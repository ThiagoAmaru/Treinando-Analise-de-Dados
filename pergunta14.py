import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')


mar = data.loc[(data['waterfront'] == 1) & (data['bedrooms'] == 3)]

print('14P: Das casas com vista para o mar, quantas tem 3 quartos?')
print('R= O numero de casas é: ', mar.shape[0])