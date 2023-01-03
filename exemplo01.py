import pandas as pd
#Comando para carregar o documentos
data = pd.read_csv('dataset/kc_house_data.csv')

#mostra as colunas desejadas, de maneira ordenada, a partir da coluna escolhida, neste caso do valor maior para o menor
preco = data[['id', 'price']].sort_values('price', ascending = False)
quartos = (data[['bedrooms']])
soma_quartos = (quartos.sum(axis=0))
print(soma_quartos)