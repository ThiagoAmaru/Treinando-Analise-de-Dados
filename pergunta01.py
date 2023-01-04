import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

print('01P: Quantas casas estão disponiveis para compra?')
print('R= Estão disponiveis', len(data['id'].unique()), 'casas para a compra')

# É necessário ficar atento com os dados duplicados
