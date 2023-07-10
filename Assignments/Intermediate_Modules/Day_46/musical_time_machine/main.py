from bs4 import BeautifulSoup
import requests

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + year)

soup = BeautifulSoup(response.text, "html.parser")
top_hundred_songs = soup.select("li ul li h3")
t100_titles = [song.getText().strip() for song in top_hundred_songs]

print(t100_titles)


