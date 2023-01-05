import pandas as pd
import plotly.express as px

data = pd.read_csv('dataset/kc_house_data.csv')

data['date'] = pd.to_datetime(data['date'])

data_mapa = data[['lat', 'long', 'id', 'price']]

mapa = px.scatter_mapbox(data_mapa, lat= 'lat', lon= 'long', hover_name= 'id' ,hover_data = ['price'], color_discrete_sequence=['fuchsia'], zoom= 3, height=300)

mapa.update_layout(mapbox_style = 'open-street-map')

mapa.update_layout(height= 600, margin = {'r' : 0,'t': 0,'l':0,'b': 0})

mapa.show()

mapa.write_html('dataset/mapa_kc_house.html')