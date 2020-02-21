import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotify_track_data.credentials as cr


### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

def graphgenerator(tracks_id_list):
	# client auth
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

	# Loop over seeds
	for track_id in tracks_id_list:

		# make the query
		track_list = [] # Important: each seed must be in a list itself. That's the way this API works. 
		track_list.append(track_id)
		recommendation = sp.recommendations(seed_tracks=track_list, seed_artists=None, seed_genres=None, limit=10, country=None,)
			# Aquí s'han de separar els 10 tracks que retorna de la recomanació

			recommended = [] # Llista d'Ids dels tracks recommanats

	
		node_pair = str(track_id+","+ #aqui va la recomanació!)
		




