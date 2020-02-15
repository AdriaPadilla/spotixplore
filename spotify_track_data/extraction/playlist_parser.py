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

	user_id_list = []
	playlist_id_list = []
	track_name_list = []
	added_at_list = []
	artist_name_list = []
	album_name_list = []
	track_id_list = []
	danceability_list = []
	instrumentalness_list = []
	duration_ms_list = []
	duration_sc_list = []
	duration_mn_list = []
	energy_list = []
	tempo_list = []
	mode_list = []
	mode_notation_list = []
	key_list = []
	key_notation_list = []
	cover_img_list = []
	popularity_list = []
	available_markets_count_lists = []
	loudness_list = []

	files = glob.glob("output_playlists/*.json")

	for file in files:

		tracks_id_list = []

		## PLAYLIST DATA EXTRACTION

		with open(file) as f:

				data = json.load(f)
				items = data["items"]

				for track in items:

					user_id_list.append(track["added_by"]["id"])

					playlist_id = file.split("__")[1]
					playlist_id_list.append(playlist_id)
					track_name = track["track"]["name"]
					track_name_list.append(track_name)
					print("Parsing data for track: "+track_name)

					track_id = track["track"]["uri"]
					track_id = track_id.split(":")[2]
					track_id_list.append(track_id)

					added_at_list.append(track["added_at"])

					artist_name_list.append(track["track"]["album"]["artists"][0]["name"])
					album_name_list.append(track["track"]["album"]["name"])
					cover_img_list.append(track["track"]["album"]["images"][0]["url"])

					popularity_list.append(int(track["track"]["popularity"]))

					available_markets = track["track"]["available_markets"]
					available_markets = len(available_markets)
					available_markets_count_lists.append(available_markets)

					# Append track ID to use in the next function.		
					tracks_id_list.append(track_id)

		## AUDIO FEATURES DATA EXTRCTION
						
		for track_id in tracks_id_list:
			print("Extracting audio features for track ID: "+track_id )
			track_features = sp.audio_features(track_id)

			track_data = track_features[0]
			danceability_list.append(track_data["danceability"])
			instrumentalness_list.append(track_data["instrumentalness"])
			duration_ms_list.append(track_data["duration_ms"])
			duration_sc = round(track_data["duration_ms"]/1000, 2)
			duration_sc_list.append(duration_sc)
			duration_mn = round(duration_sc/60, 2)
			duration_mn_list.append(duration_mn)
			energy_list.append(track_data["energy"])
			loudness_list.append(track_data["loudness"])
			tempo_list.append(track_data["tempo"])
			mode_list.append(track_data["mode"])
			key_list.append(track_data["key"])

			output_folder = "output_audio_features__"+file
			if not os.path.exists(output_folder):
				os.makedirs(output_folder)

			file_name = track_id+"__audio_features__"+".json"

			with open(os.path.join(output_folder, file_name), "w") as write_file:

				### Dump response content in json_filename
				json.dump(track_features, write_file, sort_keys=True, indent=4)

	# KEY Transform
	for key in key_list:
		if key == 0:
			key_notation_list.append("C")
		elif key == 1:
			key_notation_list.append("C#")
		elif key == 2:
			key_notation_list.append("D")
		elif key == 3:
			key_notation_list.append("D#")
		elif key == 4:
			key_notation_list.append("E")
		elif key == 5:
			key_notation_list.append("F")
		elif key == 6:
			key_notation_list.append("F#")
		elif key == 7:
			key_notation_list.append("G")
		elif key == 8:
			key_notation_list.append("G#")
		elif key == 9:
			key_notation_list.append("A")
		elif key == 10:
			key_notation_list.append("A#")
		elif key == 11:
			key_notation_list.append("B")
		elif key == -1:
			key_notation_list.append("null")
		else:
			pass

	# Mode Transformation
	for mode in mode_list:
		if mode == 1:
			mode_notation_list.append("major")
		elif mode == 0:
			mode_notation_list.append("minor")
		else:
			mode_notation_list.append("null")

	print("Creating and exporting DataFrame. PLASE WAIT!")

	df = pd.DataFrame({
	"user_id":user_id_list,
	"playlist_id":playlist_id_list,
	"track_id":track_id_list,
	"added_at":added_at_list,
	"track_name":track_name_list,
	"artist":artist_name_list,
	"available_markets": available_markets_count_lists,
	"album":album_name_list,
	"popularity":popularity_list,
	"danceability":danceability_list,
	"instrumentalness":instrumentalness_list,
	"duration_ms":duration_ms_list,
	"duration_sec":duration_sc_list,
	"duration_min":duration_mn_list,
	"energy":energy_list,
	"tempo":tempo_list,
	"loudness": loudness_list, 
	"mode":mode_list,
	"mode_notation":mode_notation_list,
	"key":key_list,
	"key_notation":key_notation_list,
	"cover_img":cover_img_list,
	})

	df.to_excel("your_output_file.xlsx")

	print(df)		
	print("Job Done!")


