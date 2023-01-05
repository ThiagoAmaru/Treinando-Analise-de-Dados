import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')


andar = data['floors'].unique()
andares = sorted(andar, reverse=True)
soma = data.loc[data['floors'] == andares[0]]

print('Quantos imóveis possuem o numero máximo de andares?')
print('R= ', soma.shape[0])