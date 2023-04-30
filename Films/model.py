import pickle
import os


class Film:
    def __init__(self, title,genre, author,year, duration,   studio, actors):
        self.title = title
        self.author = author
        self.duration = duration
        self.year = year
        self.genre = genre
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.author})"


class FilmModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.film = self.load_data()

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.film[film.title] = film

    def get_all_film(self):
        return self.film.values()

    def get_single_film(self, user_title):
        film = self.film[user_title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "режиссер": film.author,
            "длительность": film.duration,
            "год выпуска": film.year,
            "студия": film.studio,
            "актеры": film.actors

        }
        return dict_film

    def remove_film(self, user_title):
        return self.film.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.film, f)
