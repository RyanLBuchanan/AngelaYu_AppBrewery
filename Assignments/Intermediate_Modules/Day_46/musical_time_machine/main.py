import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

""" Scraping the Billboard 100 """
# date = input("Welcome to the Music Time Machine!\nWhich year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# URL = f"https://www.billboard.com/charts/hot-100/{date}/"
# response = requests.get(URL)
#
# soup = BeautifulSoup(response.text, "html.parser")
# songs = soup.select("li ul li h3")
# song_titles = [song.getText().strip() for song in songs]
# artists = soup.find_all(name="span", class_="u-max-width-330")
# artist_names = [name.getText().strip("\n\t") for name in artists]
# song_and_artist = dict(zip(song_titles, artist_names))
#
# print(f"{song_and_artist}\n")
# print("Searching for songs on Spotify and creating new playlist...")

""" Spotify Authentication """
# Constants
OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_APP_REDIRECT_URL="http://example.com"
SPOTIFY_DISPLAY_NAME="Ryan Lowell Buchanan"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Ryan Lowell Buchanan"
    )
)

user_id = sp.current_user()["id"]
#
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
#

#
#
#
#
