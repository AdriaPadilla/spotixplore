import pandas as pd
import spotify_track_data.starting_point as st
import spotify_track_data.extraction.playlist_data as plr
import spotify_track_data.extraction.playlist_parser as trr
import spotify_track_data.extraction.playlist_features as pld
import spotify_track_data.extraction.track_features as tf
import spotify_track_data.extraction.data_treatment as dt

# First, you need to define credentials in "credentials.py"
# Second, you have to define playlists in "starting_pint.py"

playlists = st.PLAYLISTS

if __name__ == "__main__":

	L = []

	for playlist in playlists:
		playlist_api_response = plr.grab_playlist(playlist)
		track_features_api_response = trr.playlist_parser(playlist_api_response)
		playlist_data = pld.grab_playlist_features(playlist_api_response)
		tracks_features_list = tf.track_features(track_features_api_response)
		df = dt.data_framing(tracks_features_list, playlist_data)

		L.append(df)

	final_dataframe = pd.concat(L, ignore_index=True)
		
	print(final_dataframe)
	final_dataframe.to_excel("output.xlsx")
