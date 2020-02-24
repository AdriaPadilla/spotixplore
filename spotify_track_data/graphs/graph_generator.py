import pandas as pd

def graph_gen(recom_objects_list):

	nodes_pairs_list = []

	for track in recom_objects_list:

		data = track.__dict__

		seed_id = data["seed_id"]
		seed_name = data["seed_name"]
		recommend_id = data["recommended_id"]
		recommend_name = data["recommended_track_name"]

		node_pair = str(seed_id)+";"+str(recommend_id)
		nodes_pairs_list.append(node_pair)

		print("Creating NODES AND PAIRS:" + node_pair)

	graph_frame = pd.DataFrame(nodes_pairs_list)

	return graph_frame