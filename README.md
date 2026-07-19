# Weather Lookup CLI

A modular command-line weather application built with Python. The program accepts a city name, retrieves its geographic coordinates through the Open-Meteo Geocoding API, and then uses those coordinates to fetch and display current weather conditions.

The project separates responsibilities into individual functions, making the code easier to read, test, maintain, and extend.

## How It Works

1. The user enters a city name.
2. `get_city_coordinates()` sends the city name to the Open-Meteo Geocoding API.
3. The application retrieves the city's name, country, latitude, and longitude.
4. `display_city_info()` displays the location information.
5. `get_weather()` uses the latitude and longitude to request current weather data.
6. `display_weather()` extracts and displays the weather values and their units.

## Features

* Search for a city by name
* Retrieve city coordinates
* Display city and country information
* Fetch current weather conditions
* Display temperature
* Display wind speed
* Display relative humidity
* Display dew point
* Display the correct unit for each weather measurement
* Handle unsuccessful API responses
* Handle cities that cannot be found
* Separate API logic from display logic

## How To Run

Install the required dependency:

```bash
pip install requests
```

Then run:

```bash
python weather_lookup.py
```

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

## APIs Used

This project uses two endpoints from Open-Meteo:

* **Geocoding API** — Converts a city name into geographic coordinates.
* **Forecast API** — Retrieves current weather data using latitude and longitude.

## Topics Covered

* HTTP requests with `requests`
* REST API interaction
* GET requests
* Query parameters
* JSON responses
* API status codes
* Nested dictionaries
* Functions
* Function parameters and return values
* Conditional statements
* Separation of concerns
* Modular program design
* Error handling

## Functions

### `get_city_coordinates(city)`

Sends a city name to the geocoding API and returns location information:

```python
{
    "name": "...",
    "country": "...",
    "latitude": ...,
    "longitude": ...
}
```

Returns `None` if the city cannot be found or the API request fails.

### `get_weather(latitude, longitude)`

Uses the city's coordinates to request current weather data and returns the API's JSON response.

### `display_city_info(city_data)`

Displays the city name, country, latitude, and longitude.

### `display_weather(weather_data)`

Extracts the current weather values and their corresponding units from the API response and displays them.

### `main()`

Controls the overall program flow by coordinating the input, API requests, and display functions.

## Example Concepts Demonstrated

This project demonstrates a complete API workflow:

```text
City Name
    ↓
Geocoding API
    ↓
Latitude + Longitude
    ↓
Weather API
    ↓
Current Weather Data
    ↓
Formatted Output
```

The project also demonstrates **separation of concerns** by keeping API requests, data processing, and user output in separate functions. This makes each function responsible for one specific task instead of putting the entire application inside one large block of code.



# Currency Converter CLI

A command-line currency conversion application built with Python. The program retrieves current exchange rates from an external API, securely loads an API key from an environment variable, validates the requested currencies, and converts an amount from one currency to another.

The project is organized into separate functions for user input, API communication, currency validation, conversion logic, and result display.

## How It Works

1. The user enters:

   * The amount to convert
   * The base currency
   * The target currency
2. The application loads an API key from the `.env` file.
3. It sends a request to the FastForex API to retrieve exchange rates.
4. The requested currencies are validated.
5. The amount is converted using the retrieved exchange rates.
6. The converted amount and the latest update time are displayed.

## Features

* Convert between different currencies
* Retrieve current exchange rates from an external API
* Securely load API credentials using environment variables
* Validate base and target currencies
* Handle API request errors
* Display the time when exchange rates were last updated
* Support conversion from currencies other than USD

## Project Structure

```text
currency-converter/
│
├── currency_converter.py
├── main.py
├── .env
└── .gitignore
```

### `main.py`

Contains the main application logic, including:

* User input
* API requests
* Currency validation
* Currency conversion
* Result display

### `.env`

Stores the API key locally:

```env
MY-KEY=your_api_key
```

The `.env` file contains sensitive credentials and should **not** be committed to GitHub.

### `.gitignore`

The `.gitignore` file prevents sensitive files such as `.env` from being uploaded to the repository.

Your `.gitignore` should include:

```gitignore
.env
```

## How To Run

Install the required dependencies:

```bash
pip install requests python-dotenv
```

Create a `.env` file in the project directory:

```env
MY-KEY=your_api_key
```

Then run:

```bash
python main.py
```

## Example Usage

```text
Enter the amount you want to convert: 100
Which currency do you want to convert from: EUR
Which currency do you want to convert to: GBP
```

Example output:

```text
100 EUR in GBP: 86.42 GBP
Updated at 2026-07-19T20:30:00Z
```

## APIs Used

This project uses the **FastForex API** to retrieve exchange rates.

The application sends an API request containing an API key through the request headers and processes the returned JSON data.

## Topics Covered

* HTTP requests with `requests`
* REST API interaction
* API authentication using request headers
* Environment variables
* `.env` files
* `python-dotenv`
* JSON responses
* API status codes
* Functions
* Function parameters and return values
* Data validation
* Currency conversion logic
* Error handling
* `.gitignore` and sensitive information management

## Functions

### `get_user_input()`

Collects the amount, base currency, and target currency from the user.

### `get_exchange_rates()`

Loads the API key from the environment and sends a request to the exchange-rate API.

Returns the API response as JSON or `None` if the request fails.

### `validate_currencies()`

Checks whether the selected base and target currencies are available in the returned exchange-rate data.

### `convert_currency()`

Converts the requested amount using the retrieved exchange rates.

The function handles two cases:

* Conversion from USD
* Conversion between two non-USD currencies through USD

For example:

```text
EUR → USD → GBP
```

### `display_result()`

Displays the converted amount and the time the exchange-rate data was last updated.

### `main()`

Coordinates the complete application workflow:

```text
User Input
    ↓
Load Exchange Rates
    ↓
Validate Currencies
    ↓
Convert Currency
    ↓
Display Result
```

## Security

The API key is loaded using:

```python
api_key = os.getenv("MY-KEY")
```

Instead of writing the API key directly inside the Python code, it is stored in a `.env` file. This keeps sensitive credentials separate from the source code.

The `.env` file should always be included in `.gitignore` before pushing the project to GitHub.

