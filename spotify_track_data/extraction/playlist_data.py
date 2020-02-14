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

	json_playlist_list = []

	response = sp.playlist_tracks(playlist, fields=None, limit=None, offset=0, market=None)

	### RESPONSE TREATMENT

	### Create dir for each playlist:

	output_folder = "output"
	save_path = os.path.join(output_folder, playlist)
	if not os.path.exists(save_path):
		os.makedirs(save_path)

	### Save playlist info in json format:

	file_name = playlist+"_data_"+".json"
	json_playlist_list.append(file_name)

	with open(os.path.join(save_path, file_name), "w") as write_file:

		### Dump response content in json_filename
		json.dump(response, write_file, sort_keys=True, indent=4)

		### Print response
		print("playlist data in file: "+file_name)

	return json_playlist_list, playlist
