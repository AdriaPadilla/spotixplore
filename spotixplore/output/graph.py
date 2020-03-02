import pandas as pd

def graph_generator(object_track_recommendations_list, recommended_artists_list, playlist):

	track_nodes_pairs_list = []
	artist_nodes_pairs_list = []

	for track in object_track_recommendations_list:
		
		data = track.__dict__
		source = data["seed"]
		target = data["id"]

		node_pair = str(source)+";"+str(target)
		
		track_nodes_pairs_list.append(node_pair)

		print("Creating edges: " + node_pair)

	graph_frame = pd.DataFrame(track_nodes_pairs_list)
	graph_frame.to_csv(playlist+"_recommended_tracks_graph.csv", index=False, header=False)

	for artist in recommended_artists_list:
		
		data = artist.__dict__
		source = data["seed"]
		target = data["id"]

		node_pair = str(source)+";"+str(target)
		
		artist_nodes_pairs_list.append(node_pair)

		print("Creating edges: " + node_pair)

	graph_frame = pd.DataFrame(artist_nodes_pairs_list)
	graph_frame.to_csv(playlist+"_recommended_artists_graph.csv", index=False, header=False)