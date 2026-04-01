import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

data = response.json()
data["value"]

print(data["value"])

# notes:
# request.get hakee dataa netistä
# json muuttaa sen python muotoon
# value ottaa pelkän vitsin
# data["value"] hakee sanakirjasta (data) vitsin "value" avaimen avulla
# value on avaimen nimi ja vitsi on sen arvo
