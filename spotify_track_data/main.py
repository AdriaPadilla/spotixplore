import spotify_track_data.starting_point as st
import spotify_track_data.extraction.playlist_data as pl
import spotify_track_data.extraction.playlist_parser as tr


# First, you need to define credentials in "credentials.py"
# Second, you have to define playlists in "starting_pint.py"

playlists = st.PLAYLISTS

if __name__ == "__main__":
	for playlist in playlists:
		pl.grab_playlist(playlist)
		
	tr.playlist_parser()

