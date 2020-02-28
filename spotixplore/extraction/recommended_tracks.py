import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotixplore.credentials as cr
import spotixplore.extraction.track_class as tc


### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

def get_recommended_from_seeds(seeds_list):

	recom_tracks_objects_list = []
	recom_tracks_id_list = []

	# Open Playlist_data
	for seed in seeds_list:

		transitional_seed_list = []
		transitional_seed_list.append(seed)

		recommended_api_response = sp.recommendations(seed_tracks=transitional_seed_list, limit=5, country=None)

		#AFEGIT NOVA CONSULTA A LA API DE SPOTIFY PER RECOLLIR LES FEATURES DE CADA TRACK

		recommended_songs = recommended_api_response["tracks"]

		for track in recommended_songs:

			recommended_track_features = sp.audio_features(track["id"])
			tf = recommended_track_features[0]

			print("get audio features for recommended: "+tf["id"])
			recom_tracks_id_list.append(tf["id"])

			# GET ALBUM GENRES
			artist_id = track["artists"][0]["id"] 
			artist_info= sp.artist(artist_id)
			try:
				main_genre = artist_info["genres"][0]
			except IndexError:
				main_genre = "not_classified"

			try:
				info = tc.Track(
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

			recom_tracks_objects_list.append(info)

	return(recom_tracks_objects_list, recom_tracks_id_list)