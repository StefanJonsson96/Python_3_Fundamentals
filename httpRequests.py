import requests

response = requests.get('https://api.sampleapis.com/coffee/hot')
json = response.json()

for something in json:
    print(something)
