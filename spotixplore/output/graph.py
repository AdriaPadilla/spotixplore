import pandas as pd

def graph_generator(track_list, artist_list, playlist):

#
# EDGES TABLE
#
	nodes_pairs_list = []
#
# Original tracks --> Recommended Track 
#

	for track in track_list:
		
		source = track.seed
		target = track.id

		node_pair = str(source)+";"+str(target)
		
		nodes_pairs_list.append(node_pair)

		print("Creating edges: " + node_pair)


#
#  Tracks (recommended + Original) --> Artists
#

	for track in track_list:
		
		source = track.id
		target = track.artist_id

		node_pair = str(source)+";"+str(target)
		
		nodes_pairs_list.append(node_pair)

		print("Creating artists / songs graph: " + node_pair)

#
# Artists original --> Related Artists
#

	for artist in artist_list:
		
		source = artist.seed
		target = artist.id

		node_pair = str(source)+";"+str(target)
		
		nodes_pairs_list.append(node_pair)

		print("Creating edges: " + node_pair)

	nodes_pairs_frame = pd.DataFrame(nodes_pairs_list)
	nodes_pairs_frame.to_csv(playlist+"_graph_adjacency_list.csv", index=False, header=False)

#
# NODES TABLE AND INFORMATION 
#

# We have 5 different objects:
# 1 Original tracks from Playlists
# 2 Recommended tracks
# 3 Original artits from playlists
# 4 Artits from recommended tracks

# List for dataframes

	all_nodes_info = []

# Object 1: ORIGINAL TRACKS FROM PLAYLIST

	for track in track_list:

		data = track.__dict__

		if data["seed"] == "from_playlist":
			track_type = data["seed"]
		else:
			track_type = "recommended_track"

		df = pd.DataFrame({
			"name": "track - " + data["track_name"] + " - " + data["artist_name"],
			"genre": data["album_genre"],
			"type": track_type,
			"global_type": "song",
			"popularity": data["popularity"],
			"id": data["id"],
			}, index=[0])
		all_nodes_info.append(df)


# Object 3: Original Artist from PLaylist

	for artist in artist_list:

		data = artist.__dict__

		df = pd.DataFrame({
			"name": "artist - " + data["artist_name"],
			"genre": data["artist_genres"],
			"type": data["origin"],	
			"global_type": "artist",
			"popularity": data["popularity"],
			"id": data["id"],
			}, index=[0])
		all_nodes_info.append(df)

# EXPORT ALL Data

	all_nodes_frame = pd.concat(all_nodes_info, ignore_index=True)
	all_nodes_frame.to_excel(playlist+"_all_nodes_output.xlsx")

	print(all_nodes_frame)



