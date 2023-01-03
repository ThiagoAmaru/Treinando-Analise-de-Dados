import pandas as pd

#importando o arquivo
data = pd.read_csv('dataset/kc_house_data.csv')

#Obtendo o número de linhas e colunas
tamanho = data.shape
atributos = data.columns
preco = data[['id', 'price']].sort_values('price', ascending = False)
quartos = data[['id', 'bedrooms']].sort_values('bedrooms', ascending = False)


print('01P: Quantas casas estão disponiveis para compra?')
print('R= Estão disponiveis', tamanho[0], 'casas para a compra')
print('='*70)
print('02P: Quantos atributos as casas possuem?')
print('R= As casas possueme', tamanho[0], 'atributos')
print('='*70)
print('03P: Quais os atributos das casas?')
print('R= Os atributos das casas analisados são:')
for x in atributos: print(x, end=", ")
print('\n','='*70)
print('04P: Qual a casa mais cara?')
#verificar outra alternativa para essa questão, existem falhas
print('R= A casa mais cara é a', preco.iloc[0])
print('='*70)
print('05P: Qual a casa maior numero de quartos?')
print('R= A casa mais cara é a', quartos.iloc[0])