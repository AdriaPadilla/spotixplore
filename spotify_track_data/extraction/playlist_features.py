import glob
import json

class Playlist(): 

	def __init__(self,
		id,
        added_at,
        added_by,
        artist_name,
        release_date,
        popularity,
        track_number,
        track_name,
        disc_number,
        album_id,
        ):

		self.id = id
		self.added_at = added_at
		self.added_by = added_by
		self.artist_name = artist_name
		self.release_date = release_date
		self.popularity = popularity
		self.track_number = track_number
		self.track_name = track_name
		self.disc_number = disc_number
		self.album_id = album_id

def grab_playlist_features(playlist_api_response):

	playlist_features_list = []
	transitional_data_list = []

	tracks = playlist_api_response["items"]

	for data in tracks:
		transitional_data_list.append(data)

	for song in transitional_data_list:	

		try:
			info = Playlist(
				song["track"].get("id", "Nan"),
				song.get("added_at", "Nan"),
				song["added_by"].get("id", "Nan"),
				song["track"]["artists"][0].get("name", "Nan"),
				song["track"]["album"].get("release_date", "Nan"),
				song["track"].get("popularity", "Nan"),
				song["track"].get("track_number", "Nan"),
				song["track"].get("name", "Nan"),
				song["track"].get("disc_number", "Nan"),
				song["track"]["album"].get("id", "Nan"),
				)
		except AttributeError:
			continue

		playlist_features_list.append(info)

	return playlist_features_list




