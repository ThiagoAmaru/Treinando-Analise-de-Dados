import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')


data['condition'] = str(data['condition'])

print(data['condition'].dtypes)



# modifique o tipo da coluna conditioon para String
#virou um objeto, esperar correção
