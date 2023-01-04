import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')


mar = data.loc[data['waterfront'] == 1]

print('13P: Quantas casas tem vista para o mar?')
print('R= O numero de casa é: ', mar.shape[0])