import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')


andar = data.loc[data['floors'] > 2]

print('12P: Quantas casas tem mais de 2 andares?')
print('R= O numero de casas com mais de dois andares é', andar.shape[0])