import folium
from geopy.geocoders import Nominatim
import time
import pandas as pd

# List of addresses
data = pd.read_excel("location.xlsx")
data = data.head(10) # take 10 for test
addresses = data["address"]


geolocator = Nominatim(user_agent="map_pinner")

map_center = [51.107883, 17.038538]  # Set to Wroclaw
map_obj = folium.Map(location=map_center, zoom_start=5)

counter = 0
NUM_OF_RECORDS = data.shape[0]

for address in addresses:
    address_stripped = address[address.find("ul.")+4:]
    location = geolocator.geocode(address_stripped)
    if location:
        folium.Marker(
            location=[location.latitude, location.longitude],
            popup=address,
            tooltip="Click for address"
        ).add_to(map_obj)
        counter += 1
        print(f"Found {counter} of {NUM_OF_RECORDS}")
    else:
        print(f"Could not geocode address: {address}")
    time.sleep(0.2) # to be not banned 


map_obj.save("map_with_pins.html")
print("Map saved as 'map_with_pins.html'")
