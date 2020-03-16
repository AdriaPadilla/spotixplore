import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotixplore.credentials as cr

import tracks.track_class as T

### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))	


def get_tracks_from_playlist(playlist):

	track_list = []

	print("Connecting Spotify's API... WAIT")

	playlist_api_response = sp.playlist_tracks(playlist, fields=None, limit=None, offset=0, market=None)

	tracks = playlist_api_response["items"]

	for track in tracks: 

	# GET TRACK FEATURES

		track_id = track["track"]["id"]
		t_features = sp.audio_features(track_id)

		print("Getting Audio Features for ID: " +track_id)

	# GET ALBUM GENRE + SUBGENRE

		artist_id = track["track"]["artists"][0]["id"] 

		artist_info = sp.artist(artist_id)

		try:
			main_genre = artist_info["genres"][0]
		except IndexError:
			main_genre = "not_classified"

		try:
			sub_genre = artist_info["genres"][1]
		except IndexError:
			sub_genre = "not_classified"


	# CREATING THE TRACK OBJECT	

		tf = t_features[0]

		try:
			track_data = T.Track(
				"from_playlist",
				track["track"].get("id", "Nan"),
				track.get("added_at", "Nan"),
				track["added_by"].get("id", "Nan"),
				track["track"]["artists"][0].get("name", "Nan"),
				track["track"]["album"].get("release_date", "Nan"),
				track["track"]["album"].get("name", "Nan"),
				track["track"].get("popularity", "Nan"),
				track["track"].get("track_number", "Nan"),
				track["track"].get("name", "Nan"),
				track["track"].get("disc_number", "Nan"),
				track["track"]["album"].get("id", "Nan"),
				main_genre,
				sub_genre,
				artist_id,
				tf.get("acousticness", "Nan"),
				tf.get("analysis_url", "Nan"),
				tf.get("danceability", "Nan"),
				tf.get("duration_ms", "Nan"),
				tf.get("energy", "Nan"),
				tf.get("instrumentalness", "Nan"),
				tf.get("key", "Nan"),
				tf.get("liveness", "Nan"),
				tf.get("loudness", "Nan"),
				tf.get("mode", "Nan"),
				tf.get("speechiness", "Nan"),
				tf.get("tempo", "Nan"),
				tf.get("time_signature", "Nan"),
				tf.get("track_href", "Nan"),
				tf.get("type", "Nan"),
				tf.get("uri", "Nan"),
				tf.get("valence", "Nan")
				)
		except AttributeError:
			continue

		track_list.append(track_data)

	return track_list

# GET RECOMMENDED TRACKS FOR ORIGINAL TRACKS (Conditional at bottom)

def get_recommended_from_seeds(track_list):

	recommended_track_list = []

	for track in track_list:

		seed = track.id

		transitional_seed_list = [] # recommendations method need a list, with single or multiple seeds
		transitional_seed_list.append(seed)

		recommended_api_response = sp.recommendations(seed_tracks=transitional_seed_list, limit=1, country=None)

		#AFEGIT NOVA CONSULTA A LA API DE SPOTIFY PER RECOLLIR LES FEATURES DE CADA TRACK

		recommended_songs = recommended_api_response["tracks"]

		for track in recommended_songs:

			recommended_track_features = sp.audio_features(track["id"])
			tf = recommended_track_features[0]

			print("get audio features for recommended: "+tf["id"])

			# GET ALBUM GENRES
			artist_id = track["artists"][0]["id"] 

			artist_info = sp.artist(artist_id)

			try:
				main_genre = artist_info["genres"][0]
			except IndexError:
				main_genre = "not_classified"
				
			try:
				sub_genre = artist_info["genres"][1]
			except IndexError:
				sub_genre = "not_classified"

			try:
				r_track = T.Track(
					seed,
					track.get("id", "Nan"),
					"recommended",
					"recommended",
					track["artists"][0].get("name", "Nan"),
					track["album"].get("release_date", "Nan"),
					track["album"].get("name", "Nan"),
					track.get("popularity", "Nan"),
					track.get("track_number", "Nan"),
					track.get("name", "Nan"),
					track.get("disc_number", "Nan"),
					track["album"].get("id", "Nan"),
					main_genre,
					sub_genre,
					artist_id,
					tf.get("acousticness", "Nan"),
					tf.get("analysis_url", "Nan"),
					tf.get("danceability", "Nan"),
					tf.get("duration_ms", "Nan"),
					tf.get("energy", "Nan"),
					tf.get("instrumentalness", "Nan"),
					tf.get("key", "Nan"),
					tf.get("liveness", "Nan"),
					tf.get("loudness", "Nan"),
					tf.get("mode", "Nan"),
					tf.get("speechiness", "Nan"),
					tf.get("tempo", "Nan"),
					tf.get("time_signature", "Nan"),
					tf.get("track_href", "Nan"),
					tf.get("type", "Nan"),
					tf.get("uri", "Nan"),
					tf.get("valence", "Nan")
					)
			except AttributeError:
				continue

			recommended_track_list.append(r_track)

	return recommended_track_list

def explore_tracks(playlist, recommended_tracks):
	if recommended_tracks == True:

		track_list = get_tracks_from_playlist(playlist)
		recommended_track_list = get_recommended_from_seeds(track_list)
		print(">>>>> Total Tracks in playlist: "+str(len(track_list)))
		print(">>>>> Total recommended Tracks: "+str(len(recommended_track_list)))
		Total_tracks = len(recommended_track_list)+len(track_list)
		print(">>>>> Total Tracks in dataset: "+str(Total_tracks))
		track_list.extend(recommended_track_list)
		return track_list

	else:
		track_list = get_tracks_from_playlist(playlist)
		print(">>>>> Total Tracks in playlist: "+str(len(track_list)))
		print("Get recommended tracks = FALSE")
		return track_list
		pass
