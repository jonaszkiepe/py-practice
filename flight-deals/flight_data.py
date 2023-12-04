import requests
import os

HEADERS = {
    "apikey": os.environ.get("FLIGHT_DATA_API"),
    "content-type": "application/json",
}

LOCATIONS_API_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"


class FlightData:
    def __init__(self, to_cities, from_city):
        self.to_cities = to_cities
        self.from_city = from_city
        self.to_cities_codes = self.get_codes(to_cities)

    def get_codes(self, cities):
        codes = {}
        for (city, value) in cities.items():
            parameters = {
                "term": city,
                "location_types": "city"
            }
            response = requests.get(LOCATIONS_API_ENDPOINT, params=parameters, headers=HEADERS)
            codes[response.json()["locations"][0]["code"]] = value
        print(codes)
        return codes
