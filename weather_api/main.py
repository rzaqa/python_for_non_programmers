import requests as requests

API_KEY = ""
degree_symbol = "°"
lat, lon = "50.0755", "14.4378"


class City:

    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={API_KEY}")
        except Exception as e:
            print(f"There is an exception: {e}")
        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol == "F"
        print(f"In {self.name} today is {self.temp}{degree_symbol} {units_symbol}")
        print(f"Today's High is {self.temp_max}{degree_symbol} {units_symbol}")
        print(f"Today's Low is {self.temp_min}{degree_symbol} {units_symbol}")


my_city = City("Prague", "50.0755", "14.4378")
my_city.temp_print()
