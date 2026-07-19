import os
import requests
from dotenv import load_dotenv


load_dotenv()


def get_user_input():
    

    amount = int(input("Enter the amount you want to convert: "))
    base_currency = input("Which currency do you want to convert from: ").upper()
    target_currency = input("Which currency do you want to convert to: ").upper()

    return amount, base_currency, target_currency


def get_exchange_rates():
   
    api_key = os.getenv("MY-KEY")

    headers = {
        "X-API-Key": api_key
    }

    url = "https://api.fastforex.io/fetch-all"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    return response.json()


def validate_currencies(base_currency, target_currency, results):
    

    if base_currency != "USD" and base_currency not in results:
        print("Base currency not found")
        return False

    if target_currency not in results:
        print("Target currency not found")
        return False

    return True


def convert_currency(amount, base_currency, target_currency, results):
    

    if base_currency == "USD":
        converted = amount * results[target_currency]

    else:
        amount_in_usd = amount / results[base_currency]
        converted = amount_in_usd * results[target_currency]

    return converted


def display_result(amount, base_currency, target_currency, converted, updated):
    

    print(
        f"{amount} {base_currency} in {target_currency}: "
        f"{converted:.2f} {target_currency}"
    )

    print(f"Updated at {updated}")


def main():
    amount, base_currency, target_currency = get_user_input()

    data = get_exchange_rates()

    if data is None:
        return

    results = data["results"]

    if not validate_currencies(base_currency, target_currency, results):
        return

    converted = convert_currency(amount, base_currency, target_currency, results)

    display_result(amount, base_currency, target_currency, converted, data["updated"])


if __name__ == "__main__":
    main()