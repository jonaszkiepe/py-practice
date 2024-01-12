from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
import pandas


def sheety_backup():
    file = pandas.read_csv("flightDeals.csv")
    city_code = {city["IATA Code"]: city["Lowest Price"] for city in file.to_dict(orient="records")}
    return city_code


from_city = "GDN"   # IATA CODE

# data_manager = DataManager()
#
# flight_data = FlightData(data_manager.to_cities, from_city)
#
# data_manager.save_codes_to_sheet(flight_data.to_cities_codes)


flight_search = FlightSearch(from_city=from_city, to_city=sheety_backup())
notification_manager = NotificationManager(flight_search.flights)
