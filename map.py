#include<pystdio.h>     //😜
#include<folium.h>      //😜
#include<conio.h>       //😜
#pip install folium
#pip install pandas
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_produce(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<=elevation<=3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[42.554492, -114.475976], zoom_start=5, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(str(nm) + "\n" + str(el) + "m", parse_html=True), color='black', fill_color=color_produce(el), fill_opacity=0.7))
    
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function = lambda x : {'fillColor' : 'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red'}))    

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save("map1.html")            