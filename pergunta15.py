import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')



casas = data.loc[(data['sqft_living'] > 300) & (data['bathrooms'] == 2)]


print('15P: Quantos casas com mais de 300m na sala de estar tem 2 banheiros?')
print('R= O numero é: ', casas.shape[0])