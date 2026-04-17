import requests
import datetime as dt

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = open('API_KEY.txt', 'r').read().strip()

city = str(input("Enter city name: "))

def kelvin_to_celsius(temp_kelvin):
    temp_celsius = temp_kelvin - 273.15
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_celsius, temp_fahrenheit

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

# Temperature in C
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius(feels_like_kelvin)

humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
description = response['weather'][0]['description']

local_tz = dt.timezone(dt.timedelta(seconds=response['timezone']))
sunrise_timestamp = dt.datetime.fromtimestamp(response['sys']['sunrise'], tz=dt.timezone.utc).astimezone(local_tz)
sunset_timestamp = dt.datetime.fromtimestamp(response['sys']['sunset'], tz=dt.timezone.utc).astimezone(local_tz)

# Weather Output
print(f"Weather in {city}:")
print(f"General Weather: {description}")

print(f"Temperature in Celsius: {temp_celsius:.2f}°C")
print(f"Temperature in Fahrenheit: {temp_fahrenheit:.2f}°F")

print(f"Feels like in Celsius: {feels_like_celsius:.2f}°C in {city}")
print(f"Feels like in Fahrenheit: {feels_like_fahrenheit:.2f}°F in {city}")
      
print(f"Humidity: {humidity}%")
print(f"Weather description: {description}")
print(f"Wind speed: {wind_speed} m/s")

print(f"Sunrise: {sunrise_timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Sunset: {sunset_timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

