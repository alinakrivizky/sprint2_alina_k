from Movies import Movies

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        print(f"Драмы: {self.list_of_movies}")

movies = Drama([])
movies.add_movie('Оружейный барон')