import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

tamanho = data.shape

print('02P: Quantos atributos as casas possuem?')
print('R= As casas possuem', tamanho[1], 'atributos')

#Compreender quais colunas podem ser consideradas como atributo 