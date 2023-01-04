import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

quartos = data[['bedrooms']]
soma_quartos = quartos.sum()


print('06P: Qual a soma total de quarto do conjunto de dados?')
print('R= A soma total dos', soma_quartos, 'quartos')