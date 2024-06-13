# Класс для представления информации о фильме
class Movie:
    
    # Инициализация объекта класса Movie
    def __init__(self, title, genre, year):
        """
        Инициализация объекта класса Movie.

        Args:
            title (str): Название фильма.
            genre (str): Жанр фильма.
            year (int): Год выпуска фильма.
        """
        self.title = title
        self.genre = genre
        self.year = year
        # Список оценок фильма
        self.rating_sp = []

    # Вывод информации о фильме
    def info(self):
        """
        Вывод информации о фильме.

        Если фильм еще не был оценен, выводится рейтинг 0, иначе выводится среднее значение оценок.
        """
        if len(self.rating_sp) == 0:
            print('Название: ', self.title, ',', 'Жанр: ', self.genre, ',', 'Год: ', self.year, 'Рейтинг: 0')
        else:            
             print('Название: ', self.title, ',', 'Жанр: ', self.genre, ',', 'Год: ', self.year, 'Рейтинг:', sum(self.rating_sp)/len(self.rating_sp ))                        

    # Добавление оценки фильму
    def watch(self, grade):
        """
        Добавление оценки фильму.

        Args:
            grade (int): Оценка фильма.
        """
        self.rating_sp.append(grade)


# Создание объектов класса Movie
candyman = Movie('Кэндимэн', 'ужасы', 1992)
dune = Movie('Дюна', 'фантастика', 2023)
# Список фильмов
film_sp = [candyman, dune]

# Вывод списка фильмов
print('Список фильмов:')
for film in film_sp:
    film.info()

# Выбор фильма пользователем
film_choice = input("Какой фильм хотите посмотреть?")

# Поиск выбранного фильма в списке фильмов
for film in film_sp:
    if film_choice == film.title:
        print("Фильм найден, приятного просмотра!")
        # Получение оценки фильма от пользователя
        grade = int(input("Оцените фильм "))
        # Добавление оценки фильму
        film.watch(grade)
        break
else:
    print('Фильм не найден')

# Вывод сообщения о завершении программы
print('До скорых встреч')