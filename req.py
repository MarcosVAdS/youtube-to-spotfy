import requests

request = requests.get('http://localhost:3000/api/getPokes')

print(request.text)