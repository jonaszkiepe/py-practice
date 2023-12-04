import os
import requests
from datetime import datetime

API_KEY = os.environ.get("API_KEY")
API_ID = os.environ.get("API_ID")

NUTRITIONIX_API = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT = "/v2/natural/exercise"

exercise_input = input("Tell me which exercises you did: ")

nutritionix_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

nutritionix_body = {
    "query": exercise_input,
}

response = requests.post(url=f"{NUTRITIONIX_API}{EXERCISE_ENDPOINT}", json=nutritionix_body, headers=nutritionix_headers)
response.raise_for_status()
data = response.json()

exercise = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

now = datetime.now()
date = str(now.date())
time = str(now.time().strftime("%X"))

sheety_headers = {

"Content-Type": "application/json",
"Authorization": os.environ.get("AUTH")

}

sheety_body = {
    "workout": {
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories,
        "date": date,
        "time": time,
    }

}

print(sheety_body)

spreadsheet = os.environ.get("SPREADSHEET")
project_name = os.environ.get("PROJECTNAME")
sheet_name = os.environ.get("SHEETNAME")

SHEETY_API = f"https://api.sheety.co/{spreadsheet}/{project_name}/{sheet_name}"

response = requests.post(SHEETY_API, headers=sheety_headers, json=sheety_body)
response.raise_for_status()