import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

casa_preco = data[['id', 'price']].sort_values('price', ascending= False)


print('04P: Qual a casa mais cara?')
print('R= A casa mais cara é a: \n', casa_preco.head(1))

# Ver as limitações das funções utilizadas