import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotixplore.credentials as cr

import artists.artist_class as A

### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))


def get_artists(track_list):

	artist_list = []

	for track in track_list:

		artist_id = track.artist_id

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

		if track.seed == "from_playlist":
			origin = "playlist_artist"
		else:
			origin = "recommended_artist"

		artist_object = A.Artist(
			origin,
			track.id,
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

		artist_list.append(artist_object)

	return artist_list

def get_recommended_artist(artist_list):

	recommended_artists_list = []

	for original_artist in artist_list:

		print("Getting related artitsts for: "+original_artist.id)

		a_info = sp.artist_related_artists(original_artist.id)
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

			artist_object = A.Artist(
				"related_artist",
				original_artist.id,
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

	return recommended_artists_list

def explore_artists(track_list, recommended_artists):
	if recommended_artists == True:

		artist_list = get_artists(track_list)
		recommended_artist_list = get_recommended_artist(artist_list)

		print(">>>>> Total Artists in playlist: "+str(len(track_list)))
		print(">>>>> Total Related Artists: "+str(len(recommended_artist_list)))
		total_artists = len(recommended_artist_list)+len(track_list)
		print(">>>>> Total Artists in dataset: "+str(total_artists))
		artist_list.extend(recommended_artist_list)

		return artist_list

	else:
		artist_list = get_artists(track_list)
		print(">>>>> Total Artists in playlist: "+str(len(track_list)))
		print("Get recommended Artists = FALSE")
		return artist_list
		pass
