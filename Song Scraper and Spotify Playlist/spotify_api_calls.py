import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from songScraper import SongScraper 

TOKEN_PATH = "D:/Python/100 days Python Challenge/Intermediate/token.txt"
class SpotifySetting():
    def __init__(self):
        self.SPOTIFY_CLIENT_ID = "" #Spotify Client ID
        self.SPOTIFY_CLIENT_SECRET = "" #Spotify CLient Secret
        self.SPOTIFY_END_POINT = "https://api.spotify.com."
        

        self.TOKEN = {} #Token

    def SpotifyAuth(self):
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://example.com",
                client_id=self.SPOTIFY_CLIENT_ID,
                client_secret=self.SPOTIFY_CLIENT_SECRET,
                show_dialog=True,
                cache_path=TOKEN_PATH,
                username="", #Spotify Username  
        )
    )
        return sp
    
    def SpotifySearch(self, song_list, date):
        song_uris = []
        year = date.split("-")[0]
        for song in song_list:
            result = self.SpotifyAuth().search(q=f"track:{song} year:{year}", type="track")
            #print(result)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        return song_uris
# test = SpotifySetting()
# date = "2019-08-12"
# song_names = SongScraper(date=date).SongList()
# uris = test.SpotifySearch(song_list=song_names, date=date)
# print(uris)


