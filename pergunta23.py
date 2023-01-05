import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['condition_type'] = 'condicao'

data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'

data.loc[data['condition'] == 3 , 'condition_type'] = 'regular'
data.loc[data['condition'] == 4 , 'condition_type'] = 'regular'

data.loc[data['condition'] > 4, 'condition_type'] = 'good'


print(data.head(10))


# 3. Crie uma nova coluna chamada condition_type
# 	se o valor da coluna 'condition', for menor igual a => 'bad'
#   se o valor da coluna 'condition', for igual a 3 ou 4 => 'regular'
#   se o valor da coluna 'condition', for igual a 5 => 'good'

