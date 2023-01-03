import pandas as pd

#importando o arquivo
data = pd.read_csv('dataset/kc_house_data.csv')

#Obtendo o número de linhas e colunas
tamanho = (data.shape)
print(tamanho)
print(tamanho[0])
print(tamanho[1])


print('P: Quantas casas estão disponiveis para compra?')
print('R= Estão disponiveis', tamanho[0], 'casas para a compra')
print('='*70)
print('P: Quantos atributos as casas possuem?')
print('R= As casas possueme', tamanho[0], 'atributos')
print('='*70)