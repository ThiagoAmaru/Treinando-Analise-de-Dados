import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

precos = data[['price']]

soma_dos_valores = precos.sum()

quantidade_casa = (data.shape)[0]

valor = soma_dos_valores/quantidade_casa


print('08P: Qual preço médio de todas as casa do conjunto?')
print('R= O preço médio de todas casas do conjunto é de ', valor)
# poderia utilizar essa função do panddas (precos.mean())
#estudar e explorar mais a documentação
