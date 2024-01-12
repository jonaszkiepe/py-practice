import requests
import os

SHEETY_API_ENDPOINT = "https://api.sheety.co/1950a9535c8fdfd3ee5ec043c0476517/flightDeals/prices"
HEADERS = {
    "Authorization": os.environ.get("SHEETY_API"),
    "Content-Type": "application/json",
}


class DataManager:
    def __init__(self):
        self.to_cities = {}
        self.lowest_prizes = []
        self.get_to_cities()

    def get_to_cities(self):
        response = requests.get(SHEETY_API_ENDPOINT, headers=HEADERS)
        print(response)
        for entry in response.json()["prices"]:
            self.to_cities[entry["city"]] = entry["lowestPrice"]

    def save_codes_to_sheet(self, codes):
        index = 2
        for code in codes:

            body = {
                "price": {
                    "iataCode": code,
                }
            }
            response = requests.put(url=f"{SHEETY_API_ENDPOINT}/{index}", headers=HEADERS, json=body)
            index += 1
