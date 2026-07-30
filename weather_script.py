import requests
import csv
from datetime import datetime
import os

API_KEY = "d4f813ebdfd2363efceeb67116e32715"
CITIES = ["Bengaluru", "Mumbai", "Delhi", "Chennai", "Kolkata"]
FILE_PATH = "weather_log.csv"

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "city": city,
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "condition": data["weather"][0]["main"]
    }

def log_weather():
    file_exists = os.path.isfile(FILE_PATH)
    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "city", "temp", "humidity", "wind_speed", "condition"])
        if not file_exists:
            writer.writeheader()
        for city in CITIES:
            writer.writerow(fetch_weather(city))

if __name__ == "__main__":
    log_weather()