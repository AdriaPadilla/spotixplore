import spotixplore.starting_point as st

import spotixplore.tracks.get_tracks as track
import spotixplore.artists.get_artists as artist

import spotixplore.output.graph as tg
import spotixplore.output.dataframing as df

# First, you need to define credentials in "credentials.py"
# Second, you have to define playlists in "starting_pint.py"

playlists = st.PLAYLISTS
recommended_tracks = True
recommended_artists = True

def spotixplore(playlists):

	for playlist in playlists:

		track_list = track.explore_tracks(playlist, recommended_tracks)
		artist_list = artist.explore_artists(track_list, recommended_artists)

		tg.graph_generator(track_list, artist_list, playlist)

		df.dataframing(track_list, artist_list, playlist)

		print("Job Done!")


if __name__ == "__main__":
	spotixplore(playlists)
	






