import pandas as pd 
import json
import glob

tracks_id_list = []

def track_data(playlist, playlist_id):

	file ="output/"+playlist_id+"/"+playlist

	with open(file) as f:
			data = json.load(f)
			items = data["items"]
			for track in items:
				track_name = track["track"]["name"]
				track_id = track["track"]["uri"]
				track_id = track_id.split(":")[2]

				artist = track["track"]["album"]["artists"][0]["name"]

				tracks_id_list.append(track_id)
				print("song name: "+track_name + " - " + artist)
	return tracks_id_list

