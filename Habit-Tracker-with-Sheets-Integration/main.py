import requests
import os
from requests.auth import HTTPBasicAuth
from datetime import datetime

USERNAME = "Omelihu"
PASSWORD = "qwerty1234"
today = datetime.now()
exercise_text = input("Tell me which exercises you did? ")
API_ID = "64fc6722"
API_KEY = "c3beae20b65bbe8e536644dd845e7857"
os.environ["APP_ID"] = API_ID
os.environ["API_KEY"] = API_KEY

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query": "exercise_text",
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 190,
    "age": 20
}
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
basic_auth = HTTPBasicAuth(USERNAME, PASSWORD)

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers, auth=basic_auth)
result = response.json()
# print(result)

session_date = today.strftime("%d/%m/%Y")
session_time = today.strftime("%H:%M:%S")
for exercise in result["exercises"]:
    body = {
        "workout": {
            "date": session_date,
            "time": session_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
session_endpoint = "https://api.sheety.co/ac29fee641de1a9335e3e133e5513808/copyOfMyWorkouts/workouts"
session = requests.post(url=session_endpoint, json=body, auth=basic_auth)


print(os.environ)
print(session.text)

