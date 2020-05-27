#include<pystdio.h>     //😜
#include<folium.h>      //😜
#include<conio.h>       //😜
#pip install folium
import folium

map = folium.Map(location=[42.375918, -71.107737], zoom_start=10, tiles="Stamen Terrain")

map.save("map1.html")            