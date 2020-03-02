class Artist():
	
	def __init__(self,
		seed,
		external_urls,
		followers,
		genres,
		genres_1,
		genres_2,
		href,
		id,
		artist_name,
		popularity,
		type,
		uri,
		):
		self.seed = seed
		self.external_urls = external_urls
		self.followers = followers
		self.artist_genres = genres
		self.genres_1 = genres_1
		self.genres_2 = genres_2
		self.href = href
		self.id = id
		self.artist_name = artist_name
		self.popularity = popularity
		self.type = type
		self.uri = uri