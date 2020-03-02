import pandas as pd


def dataframing(
	object_track_list,
	object_track_recommendations_list,
	original_artists_list, 
	recommended_artists_list,
	playlist,
	):

###
###
###   TRACKS OUTPUT DATAFRAMES 
###
###


	tracks_dataframe = []

	for track in object_track_list:
		data = track.__dict__

		original_track_frame = pd.DataFrame({
		"seed": data["seed"],
		"id": data["id"],
		"added_at": data["added_at"],
		"added_by": data["added_by"],
		"artist_name": data["artist_name"],
		"release_date": data["release_date"],
		"album_name": data["album_name"],		
		"popularity": data["popularity"],
		"track_number": data["track_number"],		
		"track_name": data["track_name"],
		"disc_number": data["disc_number"],
		"album_id": data["album_id"],
		"album_genres": data["album_genres"],
		"artist_id": data["artist_id"],
		"acousticness": data["acousticness"],
	    "danceability": data["danceability"],
	    "duration_ms": data["duration_ms"],
	    "energy": data["energy"],
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

		tracks_dataframe.append(original_track_frame)

	for track in object_track_recommendations_list:

		data = track.__dict__

		recommended_track_frame = pd.DataFrame({
		"seed": data["seed"],
		"id": data["id"],
		"added_at": data["added_at"],
		"added_by": data["added_by"],
		"artist_name": data["artist_name"],
		"release_date": data["release_date"],
		"album_name": data["album_name"],		
		"popularity": data["popularity"],
		"track_number": data["track_number"],		
		"track_name": data["track_name"],
		"disc_number": data["disc_number"],
		"album_id": data["album_id"],
		"album_genres": data["album_genres"],
		"artist_id": data["artist_id"],
		"acousticness": data["acousticness"],
	    "danceability": data["danceability"],
	    "duration_ms": data["duration_ms"],
	    "energy": data["energy"],
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

		tracks_dataframe.append(recommended_track_frame)

	all_tracks_frame = pd.concat(tracks_dataframe, ignore_index=True)

	all_tracks_frame.to_excel(playlist+"_all_tracks_output.xlsx")

###
###
###   ARTISTS OUTPUT DATAFRAMES 
###
###

	artists_dataframe = []

	for artist in original_artists_list:

		data = artist.__dict__

		original_artists_frame = pd.DataFrame({
		"origin": data["seed"],
		"external_urls": data["external_urls"],
		"followers": data["followers"],
		"genres": data["genres"],
		"genres_1": data["genres_1"],
		"genres_2": data["genres_2"],
		"href": data["href"],
		"id": data["id"],
		"name": data["name"],
		"popularity": data["popularity"],
		"type": data["type"],
		"uri": data["uri"],
		}, index=[0])

		artists_dataframe.append(original_artists_frame)

	for artist in recommended_artists_list:

		data = artist.__dict__

		recommended_artists_frame = pd.DataFrame({
		"origin": data["seed"],
		"external_urls": data["external_urls"],
		"followers": data["followers"],
		"genres": data["genres"],
		"genres_1": data["genres_1"],
		"genres_2": data["genres_2"],
		"href": data["href"],
		"id": data["id"],
		"name": data["name"],
		"popularity": data["popularity"],
		"type": data["type"],
		"uri": data["uri"],
		}, index=[0])

		artists_dataframe.append(recommended_artists_frame)

	all_artists_frame = pd.concat(artists_dataframe, ignore_index=True)

	all_artists_frame.to_excel(playlist+"_all_artists_output.xlsx")

