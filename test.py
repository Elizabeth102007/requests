import requests

URL = "https://api.open-meteo.com/v1/forecast"

params= {
    "latitude": 30.0444,
    "longitude": 31.2357,
    "current": ["temperature_2m","wind_speed_10m","relative_humidity_2m", "dew_point_2m"]
    }
r = requests.get(URL, params=params)
print(r.status_code)
data = r.json()
temperature = data["current"]["temperature_2m"]
unit = data["current_units"]["temperature_2m"]
print(f"Temperature: {temperature}{unit}")
print(data)





