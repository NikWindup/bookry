from sqlite3 import Connection, Cursor
from dao.Dao import Dao
from schemas.Book import Book

class BookDao(Dao):
    
    @staticmethod
    def insert(book: Book):
        sql = """
        INSERT INTO book (title, author, language, started, finished)
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (book.title, book.author, book.language))
    