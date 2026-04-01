import requests

api_key = "bfeec1c836c01d2265cb961e60413f04" # generoitu API avain

kaupunki = input("Anna paikkakunta: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data)

saa = data["weather"][0]["description"]
lampötila_kelvin = data["main"]["temp"]

lampötila_c = lampötila_kelvin - 273.15

print("Sää:", saa)
print("Lämpötila:", round(lampötila_c, 1), "°C")