
import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')


data['standart'] = 'low'
data.loc[data['price'] > 540000, 'standart'] = 'high'

print(data.head(10))