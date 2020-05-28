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

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(str(nm) + "\n" + str(el) + "m", parse_html=True), color='black', fill_color=color_produce(el), fill_opacity=0.7))

map.add_child(fg)

map.save("map1.html")            