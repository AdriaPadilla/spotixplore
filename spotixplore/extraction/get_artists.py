import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotixplore.credentials as cr
import spotixplore.classes.artist_class as ar


### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))


def get_artists(object_track_list, object_track_recommendations_list):

	original_artists_list = []
	recommended_artists_list = []

	for track in object_track_list:
		data = track.__dict__
		artist_id = data["artist_id"]

		print("Getting artist info for: "+artist_id)

		a_info = sp.artist(artist_id)
		artist_genres = a_info["genres"][0]

		
		artist_object = ar.Artist(
		a_info["external_urls"].get("spotify", "Nan"),
		a_info["followers"].get("total", "Nan"),
		artist_genres,
		a_info.get("href", "Nan"),
		a_info.get("id", "Nan"),
		a_info.get("name", "Nan"),
		a_info.get("popularity", "Nan"),
		a_info.get("type", "Nan"),
		a_info.get("uri", "Nan"),
		)
		original_artists_list.append(artist_object)

	for track in object_track_recommendations_list:

		data = track.__dict__
		artist_id = data["artist_id"]

		print("Getting artist info for: "+artist_id)

		a_info = sp.artist(artist_id)
		artist_genres = a_info["genres"][0]

		
		artist_object = ar.Artist(
		a_info["external_urls"].get("spotify", "Nan"),
		a_info["followers"].get("total", "Nan"),
		artist_genres,
		a_info.get("href", "Nan"),
		a_info.get("id", "Nan"),
		a_info.get("name", "Nan"),
		a_info.get("popularity", "Nan"),
		a_info.get("type", "Nan"),
		a_info.get("uri", "Nan"),
		)

		recommended_artists_list.append(artist_object)

	return original_artists_list, recommended_artists_list