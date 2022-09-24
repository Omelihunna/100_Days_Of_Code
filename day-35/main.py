import requests
from twilio.rest import Client
api_key = "69f04e4613056b159c2761a9d9e664d2"
weather_params = {
    "lon": 53.408371, # 3.379206,
    "lat": -2.991573, # 6.524379,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}
account_sid = "ACae8be3b1e6b6afa2179ecfe2bc28c456"
auth_token = "6552e3524bd62b349953f06b6ddbf7ac"

part = "daily"
weather = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
# weather.raise_for_status()
weather_data = weather.json()
hourly_list = weather_data["hourly"][0:12]

will_rain = False

for i in hourly_list:
    if i["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Nancy You're stressing me, The rain won't be easy",
        from_='+12184166819',
        to='+2348166843093'
    )
    print(message.status)
