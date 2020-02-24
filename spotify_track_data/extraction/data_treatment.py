import pandas as pd
import glob
import json
import os

track_features_dataframe = pd.DataFrame()
playlist_features_dataframe = pd.DataFrame()
general_tracks_id_list = []


def data_framing(track_features_data, playlist_data, recom_objects_list):

	### TRACK FEATURES

	transitional_track_df = []

	for track in track_features_data:
		data = track.__dict__

		track_dataframe = pd.DataFrame({
		"acousticness": data["acousticness"],
	    "danceability": data["danceability"],
	    "duration_ms": data["duration_ms"],
	    "energy": data["energy"],
	    "id": data["id"],
	    "instrumentalness": data["instrumentalness"],
	    "key": data["key"],
	    "liveness": data["liveness"],
	    "loudness": data["loudness"],
	    "mode": data["mode"],
	    "speechiness": data["speechiness"],
	    "tempo": data["tempo"],
	    "time_signature": data["time_signature"],
	    "track_href": data["track_href"],
	    "valence": data["valence"],
		}, index=[0])

		transitional_track_df.append(track_dataframe)

	track_features_dataframe = pd.concat(transitional_track_df, ignore_index=True)

	### PLAYLISTS INFO

	transitional_playlist_df = []

	for playlist in playlist_data:
		playlist_info = playlist.__dict__

		playlist_dataframe = pd.DataFrame({
		"seed": "user_playlist",
		"added_by": playlist_info["added_by"],
		"id": playlist_info["id"],
		"added_at": playlist_info["added_at"],
		"artist_name": playlist_info["artist_name"],
		"release_date": playlist_info["release_date"],
		"popularity": playlist_info["popularity"],
		"track_name": playlist_info["track_name"],
		}, index=[0])

		transitional_playlist_df.append(playlist_dataframe)

	playlist_features_dataframe = pd.concat(transitional_playlist_df, ignore_index=True)

	### Recommended Tracks

	transitional_recommended_df = []

	for recommend in recom_objects_list:
		data = recommend.__dict__

		recommended_dataframe = pd.DataFrame({
		"seed": data["seed_id"],
		"added_by": "Spoty_response",
		"id": data["recommended_id"],
		"added_at": "Spoty_response",
		"artist_name": data["recommeded_artist"],
		"release_date": data["recommeded_release_date"],
		"popularity": data["recommended_popularity"],
		"track_name": data["recommended_track_name"],
		"acousticness": data["acousticness"],
	    "danceability": data["danceability"],
	    "duration_ms": data["duration_ms"],
	    "energy": data["energy"],
	    "id": data["id"],
	    "instrumentalness": data["instrumentalness"],
	    "key": data["key"],
	    "liveness": data["liveness"],
	    "loudness": data["loudness"],
	    "mode": data["mode"],
	    "speechiness": data["speechiness"],
	    "tempo": data["tempo"],
	    "time_signature": data["time_signature"],
	    "track_href": data["track_href"],
	    "valence": data["valence"],
		}, index=[0])

		transitional_recommended_df.append(recommended_dataframe)

	semifinal_final_df = pd.merge(playlist_features_dataframe, track_features_dataframe, on="id")

	final_df = semifinal_final_df.append(transitional_recommended_df)

	return final_df

	##	notes:
	##	argument ignore_index=true in concat allow to reset dataframe index

