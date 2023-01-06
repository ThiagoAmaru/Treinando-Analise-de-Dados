import pandas as pd
data = pd.read_csv('dataset/kc_house_data.csv')

data['condition_type'] = 'condicao'

data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[data['condition'] == 3 , 'condition_type'] = 'regular'
data.loc[data['condition'] == 4 , 'condition_type'] = 'regular'
data.loc[data['condition'] > 4, 'condition_type'] = 'good'


new_data = data.loc[(data['waterfront'] > 0) & (data['condition_type'] == 'bad'), 'id']

print(new_data.shape[0])


# 12. Quantos imoveis estao com a condicao igual bad e possuem "vista para o mar"
#Demorei nessa questao por nao por os condicionais entre parenteses
#principal erro, esquecer que é necessario um segundo parametro para funcao loc, nesse caso o id