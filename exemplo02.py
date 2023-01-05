import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

data['date'] = pd.to_datetime(data['date'])

# dia = data[['date']].sort_values('date', ascending=True)

# #print(data.dtypes)

# print('Qual a data do imovel, mais antigo do portifolio?')
# print('R= A data do imovel mais antigo é ', dia.head(1))
# print('='*70)
# ***************************************************************************************************************************
# andar = data['floors'].unique()
# andares = sorted(andar, reverse=True)
# soma = data.loc[data['floors'] == andares[0]]

# print('Quantos imóveis possuem o numero máximo de andares?')
# print('R= ', soma.shape[0])


# ***************************************************************************************************************************

# data.loc[data['price'] > 540000, 'standart'] = 'high'
# data.loc[data['price'] < 540000, 'standart'] = 'low'


# ***************************************************************************************************************************


# relatorio = data[['id', 'price', 'date', 'bedrooms', 'sqft_lot','standart']].sort_values('price', ascending= True)

# print(relatorio)

# relatorio.to_csv('dataset/report_aula_02.csv', index= False)
# print('Gostaria de um Relatorio Ordenado pelo preço e contendo: id, data, quartos, tamanho total, classificacao')

# print(relatorio)



# ***************************************************************************************************************************
# 5. Onde as casas estao localizadas geograficamente