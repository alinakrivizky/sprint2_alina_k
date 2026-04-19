from movies import Movies

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        print(f"Драмы: {self.list_of_movies}")
        
drama_movies = Drama([])
drama_movies.add_movie('Оружейный барон')