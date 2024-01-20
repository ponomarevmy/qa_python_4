import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['Герой нашего времени', 'Детство', 'Война и мир'])
    def test_add_new_book_no_genre_success(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize('name', ['', '11111111111111111111111111111111111111111'])
    def test_add_new_book_negative(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre == {}

    def test_add_new_book_add_double(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Шерлок Холмс')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()
        collector.books_genre = {'Оно': 'Ужасы', 'Шерлок Холмс': 'Детективы', 'Крик': 'Ужасы',
                                 'Шрек': 'Мультфильмы'}
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_for_children_success(self):
        collector = BooksCollector()
        collector.books_genre = {'Оно': 'Ужасы', 'Шерлок Холмc': 'Детективы', 'Шрек': 'Мультфильмы',
                                 'Назад в будущее': 'Комедии'}
        books_for_children = ['Шрек', 'Назад в будущее']
        assert collector.get_books_for_children() == books_for_children

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.books_genre = {'Оно': 'Ужасы', 'Шерлок Холмc': 'Детективы', 'Шрек': 'Мультфильмы'}
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Оно']

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.favorites = ['Оно']
        collector.delete_book_from_favorites('Оно')
        assert collector.get_list_of_favorites_books() == []
