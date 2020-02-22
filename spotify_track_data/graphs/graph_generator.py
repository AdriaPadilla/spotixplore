import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotify_track_data.credentials as cr

import json
import os


### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

### AUTH 
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))


def graphgenerator(tracks_id_list):

	node_pairs = []

	# Loop over seeds
	for track_id in tracks_id_list:

		# make the query
		track_list = [] # Important: each seed must be in a list itself. That's the way this API works. 
		track_list.append(track_id)
		recommendation_api_response = sp.recommendations(seed_tracks=track_list, seed_artists=None, seed_genres=None, limit=10, country=None,)

		data = recommendation_api_response["tracks"]

		data_lecture = json.dumps(data, sort_keys=True, indent=4)
		print(data_lecture)



"""
		jsons = json.dumps(data, sort_keys=True, indent=4)
		print(jsons)

"""


			# Aquí s'han de separar els 10 tracks que retorna de la recomanació
"""
			recommended = [] # Llista d'Ids dels tracks recommanats

	
		node_pair = str(track_id+","+ #aqui va la recomanació!)
		
"""



