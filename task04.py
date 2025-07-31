class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

m1 = Movie("Inception", "fantastika", 148, 8.8)
print(m1.title, m1.genre, m1.duration, m1.rating)
