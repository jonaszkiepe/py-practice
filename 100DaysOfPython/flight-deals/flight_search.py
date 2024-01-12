import requests
import os
from datetime import datetime, timedelta

HEADERS = {
    "apikey": os.environ.get("FLIGHT_SEARCH_API"),
}

API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    def __init__(self, from_city, to_city):
        self.from_city = from_city
        self.to_city = to_city
        self.from_date = datetime.now().date().strftime("%d/%m/%Y").encode()
        self.to_date = (datetime.now().date() + timedelta(weeks=24)).strftime("%d/%m/%Y").encode()
        self.flights = []
        self.search_flights()

    def search_flights(self):
        for (city, price) in self.to_city.items():
            parameters = {
                "fly_from": self.from_city,
                "fly_to": city,
                "date_from": self.from_date,
                "date_to": self.to_date,
                 }
            response = requests.get(url=API_ENDPOINT, params=parameters, headers=HEADERS)
            for flight in response.json()["data"]:
                if int(flight["price"]) <= price:
                    departure = flight["local_departure"].split("T")
                    flight_data = {
                        "from": flight["cityFrom"],
                        "to": flight["cityTo"],
                        "price": flight["price"],
                        "link": flight["deep_link"],
                        "departure": departure[0]
                    }
                    self.flights.append(flight_data)
                    print(self.flights)
                    break
