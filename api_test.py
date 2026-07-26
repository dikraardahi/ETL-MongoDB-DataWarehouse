import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=34.02&longitude=-6.84&current=temperature_2m"

response = requests.get(url)

data = response.json()

weather_df = pd.DataFrame([
    {
        "Time": data["current"]["time"],
        "Temperature": data["current"]["temperature_2m"]
    }
])

print(weather_df)