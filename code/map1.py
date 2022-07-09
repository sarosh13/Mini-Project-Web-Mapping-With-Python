import folium   # to visualize geospatial data
import pandas as pd

df = pd.read_csv("C:/Users/imroz/PycharmProjects/Web Mapping/Volcanoes.txt")

map = folium.Map(location=[38.58,-99.09],zoom_start=4,tiles="Stamen Terrain")   #create a base map

fg_elev = folium.FeatureGroup(name="Elevation")

fg_population = folium.FeatureGroup(name="Population")

latitude = df['LAT']
longitude = df['LON']
elevation = df['ELEV']
volcano_name = df['NAME']

html = """
Volcano name: 
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_gen(elevation):
    if elevation <= 1000:
        return 'green'
    elif 1000 < elevation <= 3000:
        return 'orange'
    else:
        return 'red'

for lt,ln,el,nm in zip(latitude,longitude,elevation,volcano_name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100) # to create html
    fg_elev.add_child(folium.Marker([lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color=color_gen(el),icon='')))

fg_population.add_child(folium.GeoJson(data=open("C:/Users/imroz/PycharmProjects/Web Mapping/world.json",'r',encoding='utf-8-sig').read(),
                            style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<10000000
                                                        else 'orange' if 10000000<=x['properties']['POP2005']<20000000
                                                        else 'red'}))
map.add_child(fg_elev)
map.add_child(fg_population)
map.add_child(folium.LayerControl())

map.save("Map1.html")