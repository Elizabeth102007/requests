import requests
city = input("Enter city name: ")
URL = "https://geocoding-api.open-meteo.com/v1/search"
parameter = {
    "name": city
}

r = requests.get(URL, params=parameter)

if r.status_code == 200:
    data = r.json()

    if "results" not in data or len(data["results"]) == 0:
        print("City not found")

    else:
       result = data["results"][0]
       latitude = result["latitude"]
       longitude = result["longitude"]
       name = result["name"]
       country = result["country"]
       print(f"City: {name}, {country}")
       print(f"Latitude: {latitude}")
       print(f"Longitude: {longitude}")
       
       b_url = "https://api.open-meteo.com/v1/forecast"
       params= {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m","wind_speed_10m","relative_humidity_2m", "dew_point_2m"]
         }
       response = requests.get(b_url, params=params)
       
       if response.status_code == 200:
          open_data = response.json()

          temperature = open_data["current"]["temperature_2m"]
          unit_temp = open_data["current_units"]["temperature_2m"]
          wind = open_data["current"]["wind_speed_10m"]
          unit_wind = open_data["current_units"]["wind_speed_10m"]
          humidity = open_data["current"]["relative_humidity_2m"]
          unit_humid = open_data["current_units"]["relative_humidity_2m"]
          dew = open_data["current"]["dew_point_2m"]
          unit_dew = open_data["current_units"]["dew_point_2m"]
          print(f"Temperature: {temperature}{unit_temp}")
          print(f"Wind: {wind} {unit_wind}")
          print(f"Relative Humidity: {humidity}{unit_humid}")
          print(f"Dew point: {dew}{unit_dew}")
else: 
    print(f"Error: {r.status_code}")

    