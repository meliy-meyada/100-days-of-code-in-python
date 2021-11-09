import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

REDIRECT_URI = "Your Redirect Uri"
CLIENT_ID = "Your spotify client id"
CLIENT_SECRET ="Your spotify client secret"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
date_song = input("Which year do you want travel to? Type The data in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/"+date_song)

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

song_uris = []
year = date_song.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")



playlist = sp.user_playlist_create(user=user_id, name=f"{date_song} Billboard 100", public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


