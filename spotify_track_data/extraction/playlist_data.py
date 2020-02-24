import spotipy
import json
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotify_track_data.credentials as cr


### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

### EXTRACTION

def grab_playlist(playlist):

	playlist_api_response = sp.playlist_tracks(playlist, fields=None, limit=None, offset=0, market=None)

	return playlist_api_response

