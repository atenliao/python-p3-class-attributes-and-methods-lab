class Song():
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        pass

    def add_song_to_count(self):
        Song.count = Song.count + 1
        
    def add_to_genres(self, genre):
        Song.genres.append(genre)

    def add_to_artists(self, artist):
        Song.artists.append(artist)
        

    def add_to_genre_count(self, genre):
        print(genre)
        if genre not in Song.genre_count.keys():
            Song.genre_count[genre] = 1
        else:
            count = Song.genre_count[genre] + 1
            Song.genre_count[genre]= count
        

    def add_to_artist_count(self, artist):
        if artist not in Song.artist_count.keys():
            Song.artist_count[artist] = 1
        else:
            artist_count = Song.artist_count[artist] + 1
            Song.artist_count[artist] = artist_count
        pass
