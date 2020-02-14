import pandas as pd 
import spotipy
import json
import os
import glob

from spotipy.oauth2 import SpotifyClientCredentials
import spotify_track_data.credentials as cr


### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

def playlist_parser():

	files = glob.glob("output_playlists/*.json")

	for file in files:

		tracks_id_list = []

		with open(file) as f:
				data = json.load(f)
				items = data["items"]
				for track in items:
					track_name = track["track"]["name"]
					track_id = track["track"]["uri"]
					track_id = track_id.split(":")[2]

					artist = track["track"]["album"]["artists"][0]["name"]

					tracks_id_list.append(track_id)
					print("song name: "+track_name + " - " + artist)

		for track_id in tracks_id_list:
			track_features = sp.audio_features(track_id)

			output_folder = "output_audio_features__"+file
			if not os.path.exists(output_folder):
				os.makedirs(output_folder)

			file_name = track_id+"__audio_features__"+".json"

			with open(os.path.join(output_folder, file_name), "w") as write_file:

				### Dump response content in json_filename
				json.dump(track_features, write_file, sort_keys=True, indent=4)

				### Print response
				print("Audio Data analysis saved in file: "+file_name)


		



