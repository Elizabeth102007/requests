import os
import requests
from dotenv import load_dotenv
load_dotenv()
amount = int(input("Enter the amount you want to convert: "))
base_currency = input("Which currency do you want to convert from: ").upper()
target_currency = input("Which currency do you want to convert to: ").upper()
headers = {"X-API-Key": os.getenv("MY-KEY")}

URL = "https://api.fastforex.io/fetch-all"
r = requests.get(URL, headers=headers)
if r.status_code == 200:
    data = r.json()
    results = data["results"]
    
    if base_currency not in results and base_currency != "USD":
        print("Base currency not found")
    
    elif target_currency not in results:
        print("Target currency bot found")
    
    else:
        if base_currency == "USD":
           converted = amount * results[target_currency]
        else: 
            amount_in_usd = amount/results[base_currency]
            converted = amount_in_usd * results[target_currency]
   
        print(f"{amount} {base_currency} in {target_currency}: {converted:.2f} {target_currency}")
        print(f"Updated at {data["updated"]}")

else: 
    print(f"Error: {r.status_code}")