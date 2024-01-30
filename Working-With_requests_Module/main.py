import requests
trivia = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
trivia.raise_for_status()
data = trivia.json()
print(data)