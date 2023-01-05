import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['date'] = pd.to_datetime(data['date'])

dia = data[['date']].sort_values('date', ascending=True)

#print(data.dtypes)

print('Qual a data do imovel, mais antigo do portifolio?')
print('R= A data do imovel mais antigo é ', dia.head(1))
print('='*70)