import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['condition_type'] = 'condicao'

data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'

data.loc[data['condition'] == 3 , 'condition_type'] = 'regular'
data.loc[data['condition'] == 4 , 'condition_type'] = 'regular'

data.loc[data['condition'] > 4, 'condition_type'] = 'good'

print(data.loc[data['condition_type'] == 'regular'].shape[0])





# 11. Quantos imoveis estao com a condicao igual a regular