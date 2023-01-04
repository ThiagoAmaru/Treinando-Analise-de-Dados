import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

atributos = data.columns

print('03P: Quais os atributos das casas?')
print('R= Os atributos das casas analisados são:')
for x in atributos: print(x, end=", ")

#tirar a virgula do final
