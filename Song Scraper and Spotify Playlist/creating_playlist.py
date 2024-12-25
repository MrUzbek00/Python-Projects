from songScraper import SongScraper
from spotify_api_calls import SpotifySetting

date = "2020-08-12"
song_names = SongScraper(date=date).SongList()

print("""     Song List        """)
print(song_names)

print("""Song list ends""")
sp = SpotifySetting().SpotifyAuth()
user_id =SpotifySetting().SpotifyAuth().current_user()["id"]
song_uris =SpotifySetting().SpotifySearch(song_list=song_names, date=date)

#print(song_uris)


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# # print(playlist)

sp.user_playlist_add_tracks(playlist_id=playlist["id"], tracks=song_uris, user=user_id)
# sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=uris,user=USER_ID)

