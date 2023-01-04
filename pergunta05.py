import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

quartos = data[['id', 'bedrooms']].sort_values('bedrooms', ascending= False)

print('05P: Qual a casa maior numero de quartos?')
print('R= A casa maior numero de quartos é a: \n', quartos.head(1))