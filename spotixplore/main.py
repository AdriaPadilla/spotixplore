import spotixplore.starting_point as st

import spotixplore.extraction.original_tracks as ot
import spotixplore.extraction.recommended_tracks as rt
import spotixplore.output.graph as gg
import spotixplore.output.dataframing as df

# First, you need to define credentials in "credentials.py"
# Second, you have to define playlists in "starting_pint.py"

playlists = st.PLAYLISTS

def spotixplore(playlists):
	for playlist in playlists:
			object_track_list, seeds_list = ot.get_tracks_from_playlist(playlist)
			object_track_recommendations_list, recom_tracks_id_list = rt.get_recommended_from_seeds(seeds_list)


			gg.graph_generator(object_track_recommendations_list)
			df.dataframing(object_track_list, object_track_recommendations_list)

			print("Job Done!")


if __name__ == "__main__":
	spotixplore(playlists)
	






