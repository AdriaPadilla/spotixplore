import pandas as pd

def graph_generator(object_track_recommendations_list):

	nodes_pairs_list = []

	for track in object_track_recommendations_list:
		
		data = track.__dict__
		source = data["seed"]
		target = data["id"]

		node_pair = str(source)+";"+str(target)
		
		nodes_pairs_list.append(node_pair)

		print("Creating edges: " + node_pair)

	graph_frame = pd.DataFrame(nodes_pairs_list)
	graph_frame.to_csv("graph.csv", index=False, header=False)