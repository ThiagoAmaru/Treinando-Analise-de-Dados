import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

casa = data.loc[data['sqft_living'] > 300]


print('11P: Quantas casa possuem mais de 300 metros quadrados na sala de estar?')
print('R= ', casa.shape[0], 'casas')


#tem que fazer a conversão para metros quadrados 