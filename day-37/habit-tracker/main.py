import requests
from datetime import datetime

today = datetime(year=2022, month=8, day=27)
token = "qwerty1334242"
username = "omelihunna"

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# PIXELA USER CREATION
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_id = "omzy1"

graph_params = {
    "id": graph_id,
    "name": "cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": token
}

# report = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(report.text)

track_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
date = today.strftime("%Y%m%d")
track_params = {
    "date": date,
    "quantity": "15.23"
}
# track = requests.post(url=track_endpoint, json=track_params, headers=headers)
# print(track.text)
# /v1/users/<username>/graphs/<graphID>
update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"
update_params = {
    "quantity": "19.09"
}
# update = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(update.text)

delete = requests.delete(url=update_endpoint, json=update_params, headers=headers)
print(delete.text)
