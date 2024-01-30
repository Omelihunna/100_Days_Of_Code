# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests

sheety_endpoint = "https://api.sheety.co/ac29fee641de1a9335e3e133e5513808/omzy'sFlightDeals/prices"

response = requests.get(url=sheety_endpoint)
sheet_first = response.text
sheet_data = sheet_first["prices"]
print(sheet_data)

