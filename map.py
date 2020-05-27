#include<pystdio.h>     //😜
#include<folium.h>      //😜
#include<conio.h>       //😜
#pip install folium
import folium

map = folium.Map(location=[42.375918, -71.107737], zoom_start=10, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[42.375918, -71.107737], popup="Hi i am a marker", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("map1.html")            