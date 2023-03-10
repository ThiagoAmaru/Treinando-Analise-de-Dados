import pandas as pd

#importando o arquivo
data = pd.read_csv('dataset/kc_house_data.csv')

#Obtendo o número de linhas e colunas
tamanho = data.shape
atributos = data.columns
preco = data[['id', 'price']].sort_values('price', ascending = False)
quartos = data[['id', 'bedrooms']].sort_values('bedrooms', ascending = False)
quartos2 = (data[['bedrooms']])
soma_quartos = (quartos2.sum(axis=0))


print('01P: Quantas casas estão disponiveis para compra?')
print('R= Estão disponiveis', tamanho[0], 'casas para a compra')
print('='*70)
print('02P: Quantos atributos as casas possuem?')
print('R= As casas possuem', tamanho[0], 'atributos')
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
print('='*70)
print('06P: Qual a soma total de quarto do conjunto de dados?')
print('R= A soma total dos', soma_quartos, 'quartos')
print('='*70)
print('07P: Quantas casas possuem 2 banheiros?')
print('R= ')
print('='*70)
print('08P: Qual preço médio de todas as casa do conjunto?')
print('R= ')
print('='*70)
print('09P: Qual o preço médio de casas com dois banheiros')
print('R= ')
print('='*70)
print('10P: Qual o preço minimo entre as casa com três quartos?')
print('R= ')
print('='*70)
print('11P: Quantas casa possuem mais de 300 metros quadrados na sala de estar?')
print('R= ')
print('='*70)
print('12P: Quantas casas tem mais de 2 andares?')
print('R= ')
print('='*70)
print('13P: Quantas casas tem vista para o mar?')
print('R= ')
print('='*70)
print('14P: Das casas com vista para o mar, quantas tem 3 quartos?')
print('R= ')
print('='*70)
print('15P: Quantos casas com mais de 300m na sala de estar tem 2 banheiros?')
print('R= ')