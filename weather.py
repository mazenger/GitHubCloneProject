import requests

api_key = "9f9d3a6f2b1a1ebcb5168cb6fb839ab3"
lat = 30.0444
lon = 31.2357
exclude = "minutely,hourly"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}")

print(response.status_code)

data = response.json()

print(data)