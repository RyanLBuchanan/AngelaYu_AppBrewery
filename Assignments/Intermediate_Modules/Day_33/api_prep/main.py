import requests

# International Space Station API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)