import requests


def get_city_coordinates(city):
    

    url = "https://geocoding-api.open-meteo.com/v1/search"

    parameters = {
        "name": city
    }

    response = requests.get(url, params=parameters)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        print("City not found")
        return None

    result = data["results"][0]

    return {
        "name": result["name"],
        "country": result["country"],
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }


def get_weather(latitude, longitude):
    

    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "wind_speed_10m",
            "relative_humidity_2m",
            "dew_point_2m"
        ]
    }

    response = requests.get(url, params=parameters)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    return response.json()


def display_city_info(city_data):
    

    print(f"City: {city_data['name']}, {city_data['country']}")
    print(f"Latitude: {city_data['latitude']}")
    print(f"Longitude: {city_data['longitude']}")


def display_weather(weather_data):
    
    current = weather_data["current"]
    units = weather_data["current_units"]

    temperature = current["temperature_2m"]
    wind = current["wind_speed_10m"]
    humidity = current["relative_humidity_2m"]
    dew_point = current["dew_point_2m"]

    print(f"Temperature: {temperature}{units['temperature_2m']}")
    print(f"Wind: {wind} {units['wind_speed_10m']}")
    print(f"Relative Humidity: {humidity}{units['relative_humidity_2m']}")
    print(f"Dew point: {dew_point}{units['dew_point_2m']}")


def main():
    city = input("Enter city name: ")

    city_data = get_city_coordinates(city)

    if city_data is None:
        return

    display_city_info(city_data)

    weather_data = get_weather(
        city_data["latitude"],
        city_data["longitude"]
    )

    if weather_data is None:
        return

    display_weather(weather_data)


if __name__ == "__main__":
    main()