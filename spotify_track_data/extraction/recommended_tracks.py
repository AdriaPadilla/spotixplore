import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotify_track_data.credentials as cr


### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

class Recommended_t(): 

	def __init__(self,
		seed_id,
		seed_name,
		seed_album,
		recommended_id,
		recommended_track_name,
		recommeded_artist,
		recommended_album,
		recommended_popularity,
		recommended_track_number,
		recommended_disc_number,
		recommeded_release_date,
		recommeded_duration,
		acousticness,
		analysis_url,
		danceability,
		duration_ms,
		energy,
		id,
		instrumentalness,
		key,
		liveness,
		loudness,
		mode,
		speechiness,
		tempo,
		time_signature,
		track_href,
		type,
		uri,
		valence
        ):
		
		self.seed_id = seed_id
		self.seed_name = seed_name
		self.seed_album = seed_album
		self.recommended_id = recommended_id
		self.recommended_track_name = recommended_track_name
		self.recommeded_artist = recommeded_artist
		self.recommended_album = recommended_album
		self.recommended_popularity = recommended_popularity
		self.recommended_track_number = recommended_track_number
		self.recommended_disc_number = recommended_disc_number
		self.recommeded_release_date = recommeded_release_date
		self.recommeded_duration = recommeded_duration
		self.acousticness = acousticness
		self.analysis_url = analysis_url
		self.danceability = danceability
		self.duration_ms = duration_ms
		self.energy = energy
		self.id = id
		self.instrumentalness = instrumentalness
		self.key = key
		self.liveness = loudness
		self.loudness = loudness
		self.mode = mode
		self.speechiness = speechiness
		self.tempo = tempo
		self.time_signature = time_signature
		self.track_href = track_href
		self.type = type
		self.uri = uri
		self.valence = valence

def recommended(playlist_data):

	recom_objects_list = []

	# Open Playlist_data
	for track in playlist_data:
		temporal_seed_list = []

		playlist_info = track.__dict__

		seed_id = playlist_info["id"]
		#print("Getting recommended songs from API for track ID: "+ seed_id)

		temporal_seed_list.append(seed_id)

		recommended_api_response = sp.recommendations(seed_tracks=temporal_seed_list, limit=100, country=None)

		#AFEGIT NOVA CONSULTA A LA API DE SPOTIFY PER RECOLLIR LES FEATURES DE CADA TRACK

		recommended_songs = recommended_api_response["tracks"]

		for track in recommended_songs:

			recommended_track_features = sp.audio_features(track["id"])
			tf = recommended_track_features[0]

			print("get audio features for recommended: "+tf["id"])
			try:
				info = Recommended_t(
					playlist_info.get("id", "Nan"),
					playlist_info.get("track_name", "Nan"),
					playlist_info.get("album_name"),
					track.get("id", "Nan"),
					track.get("name", "Nan"),
					track["artists"][0].get("name", "Nan"),
					track["album"].get("name", "Nan"),
					track.get("popularity", "Nan"),
					track.get("track_number", "Nan"),
					track.get("disc_number", "Nan"),
					track["album"].get("release_date", "Nan"),
					track.get("duration", "Nan"),
					tf.get("acousticness", "Nan"),
					tf.get("analysis_url", "Nan"),
					tf.get("danceability", "Nan"),
					tf.get("duration_ms", "Nan"),
					tf.get("energy", "Nan"),
					tf.get("id", "Nan"),
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
					tf.get("valence", "Nan"),
					)
			except AttributeError:
				continue

			recom_objects_list.append(info)

	return(recom_objects_list)