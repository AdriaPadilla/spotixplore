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

	response = sp.playlist_tracks(playlist, fields=None, limit=None, offset=0, market=None)

	### RESPONSE TREATMENT

	### Create dir for each playlist:

	output_folder = "output_playlists"
	save_path = os.path.join(output_folder)
	if not os.path.exists(save_path):
		os.makedirs(save_path)

	### Save playlist info in json format:

	file_name = "playlits__"+playlist+"__data__"+".json"

	with open(os.path.join(save_path, file_name), "w") as write_file:

		### Dump response content in json_filename
		json.dump(response, write_file, sort_keys=True, indent=4)

		### Print response
		actual_path = os.getcwd()
		print("File saved on: "+actual_path)
		print("Playlist data in file: "+file_name)