import requests
import datetime as dt

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = open('API_KEY.txt', 'r').read().strip()
print(api_key)
print(repr(api_key))
city = "London"

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

print(response)
