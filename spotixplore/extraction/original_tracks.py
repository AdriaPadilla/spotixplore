import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotixplore.credentials as cr

### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))	

class Track(): 

	def __init__(self,
		seed,
		id,
        added_at,
        added_by,
        artist_name,
        release_date,
        album_name,
        popularity,
        track_number,
        track_name,
        disc_number,
        album_id,
        genres,
		acousticness,
        analysis_url,
        danceability,
        duration_ms,
        energy,
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
		self.seed = seed
		self.id = id
		self.added_at = added_at
		self.added_by = added_by
		self.artist_name = artist_name
		self.release_date = release_date
		self.album_name = album_name
		self.popularity = popularity
		self.track_number = track_number
		self.track_name = track_name
		self.disc_number = disc_number
		self.album_id = album_id
		self.album_genres = genres
		self.acousticness = acousticness
		self.analysis_url = analysis_url
		self.danceability = danceability
		self.duration_ms = duration_ms
		self.energy = energy
		self.instrumentalness = instrumentalness
		self.key = key
		self.liveness = liveness
		self.loudness = loudness
		self.mode = mode
		self.speechiness = speechiness
		self.tempo = tempo
		self.time_signature = time_signature
		self.track_href = track_href
		self.type = type
		self.uri = uri
		self.valence = valence

def get_tracks_from_playlist(playlist_id):

	object_track_list = []
	seeds_list = []

	playlist_api_response = sp.playlist_tracks(playlist_id, fields=None, limit=None, offset=0, market=None)

	tracks = playlist_api_response["items"]

	for track in tracks: 

		# GET TRACK FEATURES
		track_id = track["track"]["id"]
		seeds_list.append(track_id)
		t_features = sp.audio_features(track_id)
		print("Getting Audio Features for ID: " +track_id)

		# GET ALBUM GENRE
		artist_id = track["track"]["artists"][0]["id"] 
		artist_info = sp.artist(artist_id)
		try:
			main_genre = artist_info["genres"][0]
		except IndexError:
			main_genre = "not_classified"

		tf = t_features[0]

		try:
			track_data = Track(
				"from_user",
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

		object_track_list.append(track_data)

	return object_track_list, seeds_list

"""
		recommended_api_response = sp.recommendations(seed_tracks=temporal_seed_list, limit=100, country=None)
		recommended_track_features = sp.audio_features(track["id"])
"""
