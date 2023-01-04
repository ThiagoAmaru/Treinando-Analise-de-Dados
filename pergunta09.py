import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

banheiros = data.loc[data['bathrooms'] == 2]

precos = banheiros[['price']]

print('09P: Qual o preço médio de casas com dois banheiros')
print('R= O preço médio é de ', precos.mean())
