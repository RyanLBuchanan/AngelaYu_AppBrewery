import requests
from datetime import datetime, timezone, timedelta

MY_LAT = 41.222759
MY_LONG = -111.970421

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_str = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_str = data["results"]["sunset"].split("T")[1].split(":")[0]

# Convert sunrise and sunset strings to datetime objects
sunrise_dt = datetime.strptime(sunrise_str, "%H")
sunset_dt = datetime.strptime(sunset_str, "%H")

# Get the current time in UTC
time_now_utc = datetime.now(timezone.utc)

# Calculate the current time with the UTC offset (-7:00) without considering daylight saving time
utc_offset = timedelta(hours=-7)
time_now = time_now_utc + utc_offset

# Adjust for daylight saving time
# In the US, daylight saving time starts on the second Sunday of March and ends on the first Sunday of November
# Check if the current date falls within the daylight saving time period
is_daylight_saving = time_now.month > 3 and time_now.month < 11
is_sunday = time_now.weekday() == 6
is_second_sunday = time_now.day - time_now.weekday() >= 8

if is_daylight_saving and is_sunday and is_second_sunday:
    # Adjust the UTC offset for daylight saving time (-6:00 instead of -7:00)
    utc_offset = timedelta(hours=-7)
    time_now = time_now_utc + utc_offset

# Apply the UTC offset to sunrise and sunset
sunrise_with_offset = (sunrise_dt + utc_offset).hour
sunset_with_offset = (sunset_dt + utc_offset).hour

print("Sunrise with offset:", sunrise_with_offset)
print("Sunset with offset:", sunset_with_offset)
print("Current hour with offset:", time_now.hour)
