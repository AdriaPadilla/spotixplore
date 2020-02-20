import glob
import json

class Track(): 

	def __init__(self,
		acousticness,
        analysis_url,
        danceability,
        duration_ms,
        energy,
        id,
        instrumentalness,
        key,
        liveness,
        loudness,
        mode,
        speechiness,
        tempo,
        time_signature,
        track_href,
        type,
        uri,
        valence
		):

		self.acousticness = acousticness
		self.analysis_url = analysis_url
		self.danceability = danceability
		self.duration_ms = duration_ms
		self.energy = energy
		self.id = id
		self.instrumentalness = instrumentalness
		self.key = key
		self.liveness = liveness
		self.loudness = loudness
		self.mode = mode
		self.speechiness = speechiness
		self.tempo = tempo
		self.time_signature = time_signature
		self.track_href = track_href
		self.type = type
		self.uri = uri
		self.valence = valence

def track_features(track_features_api_response):

	tracks_features_list = []

	for track_features in track_features_api_response:

		data = track_features[0]
		try:
			track = Track(
				data.get("acousticness", "Nan"),
				data.get("analysis_url", "Nan"),
				data.get("danceability", "Nan"),
				data.get("duration_ms", "Nan"),
				data.get("energy", "Nan"),
				data.get("id", "Nan"),
				data.get("instrumentalness", "Nan"),
				data.get("key", "Nan"),
				data.get("liveness", "Nan"),
				data.get("loudness", "Nan"),
				data.get("mode", "Nan"),
				data.get("speechiness", "Nan"),
				data.get("tempo", "Nan"),
				data.get("time_signature", "Nan"),
				data.get("track_href", "Nan"),
				data.get("type", "Nan"),
				data.get("uri", "Nan"),
				data.get("valence", "Nan")
				)
		except AttributeError:
			continue

		tracks_features_list.append(track)
		
	return tracks_features_list



