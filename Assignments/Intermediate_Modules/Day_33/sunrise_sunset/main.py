import requests

MY_LAT = 41.222759
MY_LONG = -111.970421

# International Space Station API
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get(url="https://api.sunrise-sunset.org/json")
response.raise_for_status()
data = response.json()
print(data)
