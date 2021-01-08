import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from pprint import pprint
scope = "playlist-modify-public user-library-read playlist-read-collaborative playlist-read-private"
user = "ciaraporter-gb" #Place UserID here ,
token = util.prompt_for_user_token(user,scope,client_id="9c41b618d60e48d7a7e2c093c2dd032f",client_secret="71cbb1794cb443d3885cc5db5ccf906d",redirect_uri='http:/localhost:8080/%27')
sp = spotipy.Spotify(auth=token)

def get_playlists(sp, user):
    listPlaylist = []
    sp.current_user_playlists(limit=50, offset=0)
    for counter in range(len(current_user_playlists)):
        listPlaylist[counter] = current_user_playlists(counter)

    return listPlaylist

def get_songs(listPlaylist):
    for counter in range(len(listPlaylist)):
        for i in range(len(listPlaylist[counter])):
            songs = []
            songs[i] = playlist_items(listPlaylist[counter])
    return songs

def create(user):
    user_playlist_create(user, name = "Merged",)
    return playlist_id

def add_songs(playlist_id, user, songs):
    for counter in range(len(songs)):
        user_playlist_add_track(user, playlist_id, songs[counter])




listOfPlaylists = get_playlists(sp,user)
listOfSongs = get_songs()
id = create(user)
add_songs(id, user, listOfSongs)
