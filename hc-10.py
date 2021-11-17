
#name: Olti Gjoni
#email: olti.gjoni13@myhunter.cuny.edu

import folium
import pandas as pd

city = pd.read_csv('Open_Restaurant_Applications.csv')

mapCity = folium.Map(location=[40.7246, -74.0019],zoom_start=14) #soho center

soho = city.groupby(['NTA']).get_group("SoHo-TriBeCa-Civic Center-Little Italy") #group all of soho

for index,row in soho.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Restaurant Name"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCity)
    
#most above is from lab 9

mapCity.save(outfile='SoHo.html')


