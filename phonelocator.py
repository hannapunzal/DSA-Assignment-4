# inspo video: https://www.youtube.com/watch?v=Geisa_ib5hs
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
# get phone number
number = input("Enter the number you want to locate: ")
phoneNumber = phonenumbers.parse(number)
# get service provider
# get gps lat long
# save in html
