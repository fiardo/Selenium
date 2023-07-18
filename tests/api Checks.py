import requests
import json

responseOne = requests.get("https://api-prod.universityliving.com/v1/cities/popular")

if responseOne.status_code == 200:
  data = responseOne.json()
  formatted_data = json.dumps(data, indent=4)
  
  # print(data)

for i in range(0,len(data)):
  print(data[i]['numberOfBeds'])
