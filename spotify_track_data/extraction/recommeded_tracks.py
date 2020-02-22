import glob
import json

class recommended(): 

	def __init__(self,
		seed_id,
		seed_name,
		recommended_id,
		recommeded_artist,
		recommended_track_name,
		recommended_album,
		recommeded_release_date,
		recommeded_duration,
        ):

		self.seed_id = seed_id
		self.seed_name = seed_name
		self.recommended_id = recommended_id
		self.recommeded_artist = recommeded_artist
		self.recommended_track_name = recommended_track_name
		self.recommended_album = recommended_album
		self.recommeded_release_date = recommeded_release_date
		self.recommeded_duration = recommeded_duration

def recommended(playlist_data):

	# Open Playlist_data

	# Get Track ID

	# Create a list for each ID

	tracks_id_list = []

	songs = playlist_data["items"]

	for song in songs:

		track_id = song["track"]["uri"]
		track_id = track_id.split(":")[2]
		tracks_id_list.append(track_id)

	print(tracks_id_list)

"""
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
"""



