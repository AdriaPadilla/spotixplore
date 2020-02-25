import pandas as pd


def dataframing(object_track_list, object_track_recommendations_list):

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

	all_tracks_frame.to_excel("output.xlsx")


	print(all_tracks_frame)
