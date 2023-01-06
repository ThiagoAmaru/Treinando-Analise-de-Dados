import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data.loc[data['yr_renovated'] == 0 , 'yr_renovated'] = 2023

dia = data[['yr_renovated']].sort_values('yr_renovated', ascending= True)

print(dia.head(1))
# Qual a data mais antiga de renovacao de um imovel
# pode melhorar
# Utilizou operadores de comparaçao e comando min