import spotify_track_data.starting_point as st
import spotify_track_data.extraction.playlist_data as pl
import spotify_track_data.extraction.playlist_parser as tr

# First, you need to define credentials in "credentials.py"
# Second, you have to define playlists in "starting_pint.py"

playlists = st.PLAYLISTS

if __name__ == "__main__":
	for playlist in playlists:
		json_playlist_list, playlist_id = pl.grab_playlist(playlist)

	for playlist in json_playlist_list:
		tracks_id_list = tr.track_data(playlist, playlist_id)
		print(tracks_id_list)

