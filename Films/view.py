def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "*"))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title(" Ввод пользовательских данных ")
    def wait_user_answer(self):
        print("Действие c фильмами: ")
        print("1 - создание фильма\n"
              "2 - список всех фильмов\n"
              "3 - просмотр определенной фильма\n"
              "4 - удаление фильма\n"
              "q - выход из программы\n")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Создание Фильма")
    def add_user_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссера": None,
            "год выпуска": None,
            "длительность": None,
            "студию": None,
            "актеров": None,
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        return dict_film

    @add_title("Список фильмов")
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")

    @add_title("Ввод названия фильма")
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_title("Просмотр данных фильма")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма = {film[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с таким названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_film(self, film):
        print(f"Фильм {film} - был удалена")

    @add_title("Ошибка ввода")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")
