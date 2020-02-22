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
		recommeded_release_date,
		recommeded_duration,
        ):

		self.seed_id = seed_id
		self.seed_name = seed_name
		self.seed_album = seed_album
		self.recommended_id = recommended_id
		self.recommended_track_name = recommended_track_name
		self.recommeded_artist = recommeded_artist
		self.recommended_album = recommended_album
		self.recommeded_release_date = recommeded_release_date
		self.recommeded_duration = recommeded_duration

def recommended(playlist_data):

	recom_objects_list = []

	# Open Playlist_data
	for track in playlist_data:
		temporal_seed_list = []

		playlist_info = track.__dict__

		seed_id = playlist_info["id"]
		print("Getting recommended songs from API for track ID: "+ seed_id)

		temporal_seed_list.append(seed_id)

		recommended_api_response = sp.recommendations(seed_tracks=temporal_seed_list, limit=10, country=None)

		recommended_songs = recommended_api_response["tracks"]

		for track in recommended_songs:

			try:
				info = Recommended_t(
					playlist_info.get("id", "Nan"),
					playlist_info.get("track_name", "Nan"),
					playlist_info.get("album_name"),
					track.get("id", "Nan"),
					track.get("name", "Nan"),
					track["artists"][0].get("name", "Nan"),
					track["album"].get("name", "Nan"),
					track["album"].get("release_date", "Nan"),
					track.get("duration", "Nan")
					)
			except AttributeError:
				continue

			recom_objects_list.append(info)

	return(recom_objects_list)