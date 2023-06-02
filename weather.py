import requests

api_key = "5490e354625147dda8bab23263e49753"

url = "http://api.weatherbit.io/v2.0/current"

city_name = input("Введите название города: ")

payload = {
    'key': api_key,
    'city': city_name,
    'lang': 'ru'
}
response = requests.get(url, params=payload)

data = response.json()

if 'error' in data:
    print('Error:', data['error'])
else:
    data = data['data'][0]

    temperature = data["temp"]
    pressure = data["pres"]
    humidity = data["rh"]
    wind = data["wind_spd"]
    weather = data["weather"]
    description = data["weather"]["description"]

    print(f"Tемпература = {temperature}\N{DEGREE SIGN}C")
    print(f"Атмосферное давление = {round(pressure, 2)} Мбар")
    print(f"Влажность = {humidity}%")
    print(f"Ветер = {round(wind, 2)} м/с")
    print(f"Описание погоды = {description}")