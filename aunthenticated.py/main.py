from dotenv import load_dotenv

import os

load_dotenv()


api_key = os.getenv("API_KEY")

port = os.getenv("PORT")
database = os.getenv("DATABASE", "sqlite")

print(f"Api key: {api_key}")
print(f"Port: {port}")
print(f"Database: {database}")