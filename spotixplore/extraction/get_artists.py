import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotixplore.credentials as cr
import spotixplore.classes.artist_class as ar


### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))


def get_artists(object_track_list):

	original_artists_list = []
	recommended_artists_list = []
	artists_seeds = []

	for track in object_track_list:
		data = track.__dict__
		artist_id = data["artist_id"]
		artists_seeds.append(artist_id)

		print("Getting artist info for: "+artist_id)

		a_info = sp.artist(artist_id)
		try:
			artist_genres = a_info["genres"][0]
		except IndexError:
			artist_genres = "Nan"
		try:
			genres_1 = a_info["genres"][1]
		except IndexError:
			genres_1 = "Nan"
		try:
			genres_2 = a_info["genres"][2]
		except IndexError:
			genres_2 = "Nan"

		artist_object = ar.Artist(
		"from playlist",
		a_info["external_urls"].get("spotify", "Nan"),
		a_info["followers"].get("total", "Nan"),
		artist_genres,
		genres_1,
		genres_2,
		a_info.get("href", "Nan"),
		a_info.get("id", "Nan"),
		a_info.get("name", "Nan"),
		a_info.get("popularity", "Nan"),
		a_info.get("type", "Nan"),
		a_info.get("uri", "Nan"),
		)
		original_artists_list.append(artist_object)

	for seed in artists_seeds:

		print("Getting related artitsts for: "+seed)
		a_info = sp.artist_related_artists(seed)
		artists = a_info["artists"]

		for artist in artists:
			try:
				artist_genres = artist["genres"][0]
			except IndexError:
				artist_genres = "Nan"
			try:
				genres_1 = artist["genres"][1]
			except IndexError:
				genres_1 = "Nan"
			try:
				genres_2 = artist["genres"][2]
			except IndexError:
				genres_2 = "Nan"

			artist_object = ar.Artist(
				seed,
				artist["external_urls"].get("spotify", "Nan"),
				artist["followers"].get("total", "Nan"),
				artist_genres,
				genres_1,
				genres_2,
				artist.get("href", "Nan"),
				artist.get("id", "Nan"),
				artist.get("name", "Nan"),
				artist.get("popularity", "Nan"),
				artist.get("type", "Nan"),
				artist.get("uri", "Nan"),
				)

			recommended_artists_list.append(artist_object)

	return original_artists_list, recommended_artists_list