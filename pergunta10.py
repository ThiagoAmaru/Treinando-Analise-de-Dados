import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')


casas = data.loc[data['bedrooms'] == 3]

valor_min = casas[['price']].sort_values('price', ascending= True)

print('10P: Qual o preço minimo entre as casa com três quartos?')
print('R= O valor minimo é', valor_min.head(1))


#pode usar a função min do pandas