import pandas as pd 
import spotipy
import json
import os
import glob

from spotipy.oauth2 import SpotifyClientCredentials
import spotify_track_data.credentials as cr
import spotify_track_data.extraction.track_features as tf


### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

def playlist_parser(playlist_data):

	track_features_list = []
	tracks_id_list = []

	songs = playlist_data["items"]

	for song in songs:

		track_id = song["track"]["uri"]
		track_id = track_id.split(":")[2]
		tracks_id_list.append(track_id)


						
	for track_id in tracks_id_list:
		track_features = sp.audio_features(track_id)
		track_features_list.append(track_features)

	return track_features_list