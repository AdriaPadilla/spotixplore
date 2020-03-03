import pandas as pd

def graph_generator(object_track_recommendations_list, recommended_artists_list, playlist, object_track_list, original_artists_list):

#
# EDGES TABLE
#
	nodes_pairs_list = []
#
# Original tracks --> Recommended Track 
#

	for track in object_track_recommendations_list:
		
		data = track.__dict__
		source = data["seed"]
		target = data["id"]

		node_pair = str(source)+";"+str(target)
		
		nodes_pairs_list.append(node_pair)

		print("Creating edges: " + node_pair)


#
#  Tracks (recommended + Original) --> Artists
#

	for track in object_track_recommendations_list:
		
		data = track.__dict__
		source = data["artist_id"]
		target = data["id"]

		node_pair = str(source)+";"+str(target)
		
		nodes_pairs_list.append(node_pair)

		print("Creating artists / songs graph: " + node_pair)

#
# Artists original --> Related Artists
#

	for artist in recommended_artists_list:
		
		data = artist.__dict__
		source = data["seed"]
		target = data["id"]

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
# 5 Related artists

# List for dataframes

	all_nodes_info = []

# Object 1: ORIGINAL TRACKS FROM PLAYLIST

	for track in object_track_list:

		data = track.__dict__
			
		df = pd.DataFrame({
			"name": "track - " + data["track_name"] + " - " + data["artist_name"],
			"genre": data.get("album_genres", "Nan"),
			"type": "playlist_track",
			"global_type": "song",
			"popularity": data["popularity"],
			"id": data["id"],
			}, index=[0])
		all_nodes_info.append(df)

# Object 2: Recommended TRACKS 

	for track in object_track_recommendations_list:

		data = track.__dict__

		df = pd.DataFrame({
			"name": "track - " + data["track_name"] + " - " + data["artist_name"],
			"genre": data.get("album_genres", "Nan"),
			"type": "recommended_track",
			"global_type": "song",
			"popularity": data["popularity"],
			"id": data["id"],
			}, index=[0])
		all_nodes_info.append(df)

# Object 3: Original Artist from PLaylist

	for artist in original_artists_list:

		data = artist.__dict__

		df = pd.DataFrame({
			"name": "artist - " + data["artist_name"],
			"genre": data.get("artist_genres", "Nan"),
			"type": "playlist_artist",
			"global_type": "artist",
			"popularity": data["popularity"],
			"id": data["id"],
			}, index=[0])
		all_nodes_info.append(df)

# Object 4: Artists From recommended Tracks

	for artist in object_track_recommendations_list:

		data = artist.__dict__
			
		df = pd.DataFrame({
			"name": "artist - " + data["artist_name"],
			"genre": data.get("album_genres", "Nan"),
			"type": "recommended_artist",
			"global_type": "artist",
			"popularity": data["popularity"],
			"id": data["artist_id"],
			}, index=[0])
		all_nodes_info.append(df)

# Object 5: Related Artists

	for artist in recommended_artists_list:

		data = artist.__dict__
			
		df = pd.DataFrame({
			"name": "artist - " + data["artist_name"],
			"genre": data.get("artist_genres", "Nan"),
			"type": "related_artist",
			"global_type": "artist",
			"popularity": data["popularity"],
			"id": data["id"],
			}, index=[0])
		all_nodes_info.append(df)


# EXPORT ALL Data

	all_nodes_frame = pd.concat(all_nodes_info, ignore_index=True)
	all_nodes_frame.to_excel(playlist+"_all_nodes_output.xlsx")



