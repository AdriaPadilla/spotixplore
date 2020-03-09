import pandas as pd


def dataframing(track_list, artist_list, playlist):

###
###
###   TRACKS OUTPUT DATAFRAMES 
###
###


	tracks_dataframe = []

	for track in track_list:
		data = track.__dict__

		track_df = pd.DataFrame({
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
		"album_genre": data["album_genre"],
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

		tracks_dataframe.append(track_df)

	all_tracks_frame = pd.concat(tracks_dataframe, ignore_index=True)

	all_tracks_frame.to_excel(playlist+"_all_tracks_output.xlsx")

###
###
###   ARTISTS OUTPUT DATAFRAMES 
###
###

	artists_dataframe = []

	for artist in artist_list:

		data = artist.__dict__

		artists_frame = pd.DataFrame({
		"origin": data["origin"],
		"seed": data["seed"],
		"external_urls": data["external_urls"],
		"followers": data["followers"],
		"genres": data["artist_genres"],
		"genres_1": data["genres_1"],
		"genres_2": data["genres_2"],
		"href": data["href"],
		"id": data["id"],
		"artist_name": data["artist_name"],
		"popularity": data["popularity"],
		"type": data["type"],
		"uri": data["uri"],
		}, index=[0])

		artists_dataframe.append(artists_frame)

	all_artists_frame = pd.concat(artists_dataframe, ignore_index=True)

	all_artists_frame.to_excel(playlist+"_all_artists_output.xlsx")

