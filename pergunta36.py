
import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data = data[['bedrooms']].sort_values('bedrooms', ascending= False)

print(data.head(1))

# 16. Qual o maior numero de quartos que um imovel do tipo house possui?