
#import library
import folium
import pandas

#import the hiring data
data = pandas.read_csv("KCO_Hiring_Map.csv")

#convert the fields into lists
lat = list(data["Location Latitude"])
long = list(data["Location Longitude"])
popup_value = list(data["Title"])
color_value = list(data["Color"])

#create a map
map = folium.Map(location=[38,-77], zoom_start=4)
fg = folium.FeatureGroup(name="My Map")

#add data points to the map
for lat, long, popup_value, color_value in zip(lat, long, popup_value, color_value):
    fg.add_child(folium.Marker(location=[lat,long], popup="Open Position: " + str(popup_value), icon=folium.Icon(color=color_value.lower())))

#save the map
map.add_child(fg)
map.save("map1.html")
