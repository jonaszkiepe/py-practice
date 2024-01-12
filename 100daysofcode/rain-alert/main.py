import requests
from twilio.rest import Client
import os

parameters = {
    "appid": os.environ.get("APPID"),
    "lat": float(os.environ.get("LAT")),
    "lon": float(os.environ.get("LON")),
}

print(parameters)

account_sid = "AC7697523006391bccf0b468d881cfbb6f"
auth_token = "0c17f9ef4a4dee089eca39073b4fccf5"

client = Client(account_sid, auth_token)


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
weather_3hours = data["list"]
umbrella_time: bool
for weather in weather_3hours[:4]:
    weather_id = weather["weather"][0]["id"]
    if weather_id < 700:
        umbrella_time = True
        break
if umbrella_time:
    message = client.messages \
        .create(
            body='Its going to rain today',
            from_='+12314000512',
            to='+48453465960'
        )
    print(message.status())
