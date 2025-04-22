import sqlite3
from sqlite3 import Connection, Cursor
from dao.Dao import Dao


class BookGenreDao(Dao):
    
    @staticmethod
    def insert(book_id: int, genre_id: int):
        sql = """
        INSERT INTO book_genre (book_id, genre_id) VALUES (?, ?)
        """
        
        conn: Connection = BookGenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (book_id, genre_id))
        conn.commit()
    
    @staticmethod
    def select_by_book_id(book_id: int):
        sql = """
        SELECT * FROM genre WHERE book_id = ?
        """
        
        conn: Connection = BookGenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (book_id,))
        genres = cursor.fetchall()
        return genres
    
    @staticmethod
    def delete_by_book_id(book_id: int):
        sql = """
        DELETE FROM book_genre WHERE book_id = ?
        """
        
        conn: Connection = BookGenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (book_id,))
        conn.commit()
