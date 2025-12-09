class MockWeatherAPI:
    def fetch(self, city):
        return {"temp_c": 21, "desc": "Clear sky"}


class WeatherAPIAdapter:
    def __init__(self, client):
        self.client = client

    def get_weather(self, city):
        raw = MockWeatherAPI().fetch(city)
        return {
            "temperature": raw["temp_c"],
            "condition": raw["desc"]
        }
