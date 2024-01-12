import os
import requests
from bs4 import BeautifulSoup
from spotipy import oauth2
import spotipy

year = input("What date would you like to travel back to? Format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{year}/"

soup = BeautifulSoup(requests.get(URL).text, "html.parser")

titles = soup.select("div ul li ul li h3")
title_text = [title.getText().replace("\n", "").replace("\t","") for title in titles]

songs = [f"track:{title} year:{year.split("-")[0]}" for title in title_text]

client_id = os.environ.get("id")
client_secret = os.environ.get("secret")
username = os.environ.get("username")


sp = oauth2.SpotifyOAuth(client_id=id,
                         client_secret=client_secret,
                         redirect_uri="https://google.com/",
                         scope="playlist-modify-public",
                         username=username)

sp.get_access_token(code=sp.get_auth_response(), as_dict=True, check_cache=True)

spotify = spotipy.Spotify(auth_manager=sp)
song_uris = []
for song in songs:
    result = spotify.search(q=song, type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass
playlist_name = f"{year} Billboard 100"
idpl = spotify.user_playlist_create(user=username, name=playlist_name,
                                    public=True, collaborative=False, description='hell')["id"]
spotify.user_playlist_add_tracks(user=username, playlist_id=idpl, tracks=song_uris, position=None)
