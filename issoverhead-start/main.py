import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG <= iss_longitude <= MY_LONG:
        return True
#Your position is within +5 or -5 degrees of the ISS position.

time_now = datetime.now()

#If the ISS is close to my current position
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

def mail():
    if is_night and is_iss_overhead()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="omzycodes@gmail.com", password="Omzy@Codes123")
        connection.sendmail(
            from_addr="omzycodes@gmail.com",
            to_addrs="omzycodes@hotmail.com",
            msg="Look up"
        )


is_night()
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



