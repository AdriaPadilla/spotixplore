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

					try:
						artist_name_list.append(track["track"]["album"]["artists"][0]["name"])
					except IndexError:
						artist_name_list.append("NaN")
								
					album_name_list.append(track["track"]["album"]["name"])
					try:
						cover_img_list.append(track["track"]["album"]["images"][0]["url"])
					except IndexError:
						cover_img_list.append("NaN")

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
			try:
				danceability_list.append(track_data["danceability"])
			except TypeError:
				danceability_list.append("NaN")
			try:
				instrumentalness_list.append(track_data["instrumentalness"])
			except TypeError:
				instrumentalness_list.append("NaN")
			

			### DURATION TRACK
			try:	
				duration_ms = track_data["duration_ms"]
				duration_ms_list.append(duration_ms)
			except TypeError:
				duration_ms_list.append("NaN")

			try:	
				duration_sc = duration_ms/1000
				duration_sc_list.append(round(duration_sc, 2))
			except TypeError:
				duration_sc_list.append("NaN")

			try:	
				duration_mn_list.append(round(duration_sc/60, 2))
			except TypeError:
				duration_mn_list.append("NaN")





			try:	
				energy_list.append(track_data["energy"])
			except TypeError:
				energy_list.append("NaN")
			try:
				loudness_list.append(track_data["loudness"])
			except TypeError:
				loudness_list.append("NaN")
			try:
				tempo_list.append(track_data["tempo"])
			except TypeError:
				tempo_list.append("NaN")
			try:
				mode_list.append(track_data["mode"])
			except TypeError:
				mode_list.append("NaN")
			try:
				key_list.append(track_data["key"])
			except TypeError:
				key_list.append("NaN")


			### OUTPUT THE RESPONSE

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
			key_notation_list.append("NaN")

	# Mode Transformation
	for mode in mode_list:
		if mode == 1:
			mode_notation_list.append("major")
		elif mode == 0:
			mode_notation_list.append("minor")
		else:
			mode_notation_list.append("null")

	print("Creating and exporting DataFrame. PLASE WAIT!")

	print(
	len(user_id_list),
	len(playlist_id_list),
	len(track_name_list),
	len(added_at_list),
	len(artist_name_list),
	len(album_name_list),
	len(track_id_list),
	len(danceability_list),
	len(instrumentalness_list),
	len(duration_ms_list),
	len(duration_sc_list),
	len(duration_mn_list),
	len(energy_list),
	len(tempo_list),
	len(mode_list),
	len(mode_notation_list),
	len(key_list),
	len(key_notation_list),
	len(cover_img_list),
	len(popularity_list),
	len(available_markets_count_lists),
	len(loudness_list),
		)



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


