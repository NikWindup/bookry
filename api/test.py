from dao.BookDao import BookDao
from dao.GenreDao import GenreDao
from dao.BookGenreDao import BookGenreDao


def get_book(book_id):
    book = BookDao.select_by_id(book_id)
    genre_ids = BookGenreDao.select_by_book_id(book_id=book_id)
    genres = []
    for id in genre_ids:
        genres.append(GenreDao.select_by_genre_id(genre_id=id))
    return {"book" : book, "genres" : genres}

print(get_book(1))