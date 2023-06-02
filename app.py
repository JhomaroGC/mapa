import pandas as pd
import folium
import numpy as np
import imageio
import os
import csv


os.system('cls')

with open('src\data\data2.csv', encoding='utf-8') as file:
    df = pd.read_excel('src\data\data.xlsx')      

map = folium.Map(location=[6.265198062116244, -75.49490823894898],tiles="cartodbpositron", zoom_start=16, control_scale=True)

for index, row in df.iterrows():
    # Write the html code for the popups
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup= f" <h1 style='font: Sans serif'>{row['nombre']}</h1><p style = 'font: Sans serif'>sasdadasdad aasd asd asdasd asd adsa dasd asd </p><img src = 'D4.png' width = 400/>",
        tooltip= row['nombre'],
        icon=folium.Icon(color="blue", icon="tower", icon_color='white')
    ).add_to(map)    
    
map.save(outfile= "parqueComfamaArví.html")
