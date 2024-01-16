from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.books_genre.get('Шерлок Холмс') == 'Детективы'

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмc')
        collector.set_book_genre('Шерлок Холмc', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    def test_get_books_with_specific_genre_passed(self):
        collect = BooksCollector()
        collect.books_genre = {'Шерлок Холм': 'Ужасы', 'Шерлок Хол_1': 'Детективы', 'Шерлок Холм_2': 'Ужасы',
                               'Шерлок Холм_3': 'Мультфильмы'}
        assert len(collect.get_books_with_specific_genre('Ужасы')) == 2




