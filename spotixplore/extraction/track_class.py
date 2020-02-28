class Track(): 

	def __init__(self,
		seed,
		id,
        added_at,
        added_by,
        artist_name,
        release_date,
        album_name,
        popularity,
        track_number,
        track_name,
        disc_number,
        album_id,
        genres,
		acousticness,
        analysis_url,
        danceability,
        duration_ms,
        energy,
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
		self.seed = seed
		self.id = id
		self.added_at = added_at
		self.added_by = added_by
		self.artist_name = artist_name
		self.release_date = release_date
		self.album_name = album_name
		self.popularity = popularity
		self.track_number = track_number
		self.track_name = track_name
		self.disc_number = disc_number
		self.album_id = album_id
		self.album_genres = genres
		self.acousticness = acousticness
		self.analysis_url = analysis_url
		self.danceability = danceability
		self.duration_ms = duration_ms
		self.energy = energy
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
