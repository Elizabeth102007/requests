# Weather Lookup CLI

A simple command-line weather application built with Python. The program accepts a city name, uses a geocoding API to find the city's coordinates, and then retrieves its current weather conditions.

## How It Works

1. The user enters a city name.
2. The application sends the city name to the Open-Meteo Geocoding API.
3. The API returns the city's:

   * Name
   * Country
   * Latitude
   * Longitude
4. The application uses the coordinates to request current weather data.
5. The current weather information is displayed in the terminal.

## Features

* Search for a city by name
* Retrieve geographic coordinates
* Fetch current weather conditions
* Display temperature and its unit
* Display wind speed and its unit
* Display relative humidity and its unit
* Display dew point and its unit
* Handle cities that cannot be found
* Handle unsuccessful API responses

## Example Output

```text
Enter city name: Cairo

City: Cairo, Egypt
Latitude: 30.0444
Longitude: 31.2357
Temperature: 32.5°C
Wind: 14.2 km/h
Relative Humidity: 35%
Dew point: 15.8°C
```

## How To Run

Install the required dependency:

```bash
pip install requests
```

Then run:

```bash
python weather_lookup.py
```

## APIs Used

This project uses two endpoints from Open-Meteo:

* **Geocoding API** — Converts a city name into geographic coordinates.
* **Forecast API** — Retrieves current weather conditions using latitude and longitude.

## Topics Covered

* HTTP requests with `requests`
* REST API interaction
* GET requests
* Query parameters
* JSON responses
* Nested dictionaries and lists
* API status codes
* Data extraction
* Conditional statements
* Error handling for missing search results

## Example Concepts Demonstrated

* A city name is sent as a query parameter to a geocoding endpoint.
* The API response is converted from JSON into Python data using `.json()`.
* Latitude and longitude are extracted from the geocoding response.
* Those coordinates are then used to make a second API request.
* Weather data and its corresponding units are extracted from the API response.

This project demonstrates a practical **API chaining workflow**: one API request provides the data needed to make a second API request.
