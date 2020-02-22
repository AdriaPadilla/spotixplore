import pandas as pd
import spotify_track_data.starting_point as st
import spotify_track_data.extraction.playlist_data as plr
import spotify_track_data.extraction.playlist_parser as trr
import spotify_track_data.extraction.playlist_features as pld
import spotify_track_data.extraction.track_features as tf
import spotify_track_data.extraction.data_treatment as dt

#import spotify_track_data.extraction.recommended_tracks as rec

# First, you need to define credentials in "credentials.py"
# Second, you have to define playlists in "starting_pint.py"

playlists = st.PLAYLISTS

if __name__ == "__main__":

	L = []

	for playlist in playlists:
		
		# For playlist, query for tracks inside the playlist
		playlist_api_response = plr.grab_playlist(playlist)
		
		# For track in playlist_api_response, query for track features
		track_features_api_response = trr.playlist_parser(playlist_api_response)
		
		# For each track in playlist, make an object with all the data
		playlist_data = pld.grab_playlist_features(playlist_api_response)
		
		# For playlist, parse info and get track info to create an object
		tracks_features_list = tf.track_features(track_features_api_response)
		
		# Join 2 objects: track features and playlist info, to create a dataframe. 
		# Output 1: dataframe with all playlist tracks (info + features) / Output 2: Track ID's to use them to get recommeded tracks.
		df = dt.data_framing(tracks_features_list, playlist_data)

		# Get recommeded tracks for tracks in "tracks_id_list" <- This are all tracks inside the playlist
		#recommended_api_response = rec.recommended_tracks(playlist_data)

		# Append Dataframe to Global List to join all playlists in extraction
		L.append(df)

	# Concatenate all dataframes and Output a xlsx file
	final_dataframe = pd.concat(L, ignore_index=True)
		
	print(final_dataframe)
	final_dataframe.to_excel("output.xlsx")
