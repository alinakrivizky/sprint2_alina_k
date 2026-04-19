from movies import Movies

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        print(f"Комедии: {self.list_of_movies}")

comedy_movies = Comedy([])
comedy_movies.add_movie('Большой куш')