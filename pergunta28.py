import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

dia = data[['yr_built']].sort_values('yr_built', ascending= True)

print(dia.head(1))


#Qual a data mais antiga de construçao de um imovel