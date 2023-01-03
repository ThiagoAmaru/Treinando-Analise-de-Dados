import pandas as pd
data = pd.read_csv('dataset/kc_house_data.csv')
print(data[['id', 'price']].sort_values('price',ascending= False))