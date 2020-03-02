import spotixplore.starting_point as st

import spotixplore.extraction.get_tracks as gt
import spotixplore.extraction.get_recommended_tracks as gr
import spotixplore.extraction.get_artists as ga

import spotixplore.output.graph as tg
import spotixplore.output.dataframing as df

# First, you need to define credentials in "credentials.py"
# Second, you have to define playlists in "starting_pint.py"

playlists = st.PLAYLISTS

def spotixplore(playlists):
	for playlist in playlists:
			object_track_list, seeds_list = gt.get_tracks_from_playlist(playlist)
			object_track_recommendations_list, recom_tracks_id_list = gr.get_recommended_from_seeds(seeds_list)

			original_artists_list, recommended_artists_list = ga.get_artists(object_track_list)

			tg.graph_generator(object_track_recommendations_list, recommended_artists_list, playlist, object_track_list, original_artists_list)
			df.dataframing(object_track_list, object_track_recommendations_list, original_artists_list, recommended_artists_list, playlist)

			print("Job Done!")


if __name__ == "__main__":
	spotixplore(playlists)
	






