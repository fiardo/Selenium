import requests
import json

url = "https://api-prod.universityliving.com/v1/cities/popular"


response = requests.get(url=url)
print(type(response))
formatted = response.json()
print(type(formatted))
# j = json.dumps(formatted,indent=4)
# print(type(formatted))

