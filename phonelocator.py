# inspo video: https://www.youtube.com/watch?v=Geisa_ib5hs
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium
#key for opencage
key = "9383f21a761044d7beaef312e78a7973"

# get phone number
number = input("Enter the number you want to locate: ")
phoneNumber = phonenumbers.parse(number)

# get location
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print(yourLocation)

# get service provider
provider = phonenumbers.parse(number)
print(carrier.name_for_number(provider,"en"))

# get gps lat long
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
result = geocoder.geocode(query)
print(result)

lat = result[0]["geometry"]["lat"]
lng = result[0]["geometry"]["lng"]
print(lat,lng)
map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat,lng], popup=yourLocation).add_to(map)

# save in html
map.save("location.html")