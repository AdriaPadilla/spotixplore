import pandas as pd

def generator(recom_objects_list):

	nodes_pairs_list = []

	for track in recom_objects_list:
		data = track.__dict__

		seed_id = data["seed_id"]
		recommend_id = data["recommended_id"]

		node_pair = str(seed_id)+";"+str(recommend_id)

		nodes_pairs_list.append(node_pair)

	graph_frame = pd.DataFrame(nodes_pairs_list)

	print(graph_frame)

	graph_frame.to_csv("graph.csv", index=False, header=False)

	return graph_frame