import urllib , json
from urllib import request

url = "https://api-prod.universityliving.com/v1/search?searchTerm=london"

response = urllib.request.urlopen(url)
data = json.loads(response.read())

jsonFormat = json.dumps(data, indent=4)
print(jsonFormat)

print(data['cities'][1]['slug'])