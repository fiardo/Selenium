import requests

url = "https://api-next.devbeta.in/v1/mix/country-list"

response = requests.get(url=url)

print(response)
