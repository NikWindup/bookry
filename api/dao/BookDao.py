from sqlite3 import Connection, Cursor
from api.dao.Dao import Dao
from api.schemas.Book import Book
import time


class BookDao(Dao):
    
    @staticmethod
    def insert(book: Book) -> None:
        sql = """
        INSERT INTO book (title, author, started, isbn) VALUES (?, ?, ?, ?)
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (
            book.title,
            book.author,
            BookDao.__get_current_time(),
            book.isbn
        ))
        conn.commit()

    @staticmethod
    def update_language(language: str, book_id: int):
        sql = """
        UPDATE book SET language = ? WHERE book_id = ?
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (language, book_id))
        conn.commit()
    
    @staticmethod
    def update_finished(book_id: int):
        sql = """
        UPDATE book SET finished = ? WHERE book_id = ?
        """
        
        finished_time = BookDao.__get_current_time()
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (finished_time, book_id))
        conn.commit()
    
    @staticmethod
    def update_rating(rating: int, book_id: int):
        sql = """
        UPDATE book SET rating = ? WHERE book_id = ?
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (rating, book_id))
        conn.commit()
    
    @staticmethod
    def select_by_id(book_id: int) -> Book:
        sql = """
        SELECT title, author, language, started, finished, rating, isbn FROM book WHERE book_id = ?
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (book_id,))
        book_data = cursor.fetchone()
        print(book_data)
        
        return Book(
            id=book_id,
            title=book_data[0] ,
            author=book_data[1],
            language=book_data[2],
            started=book_data[3],
            finished=book_data[4],
            rating=book_data[5],
            isbn=book_data[6]
        )
    
    @staticmethod
    def __get_current_time():
        current_time = f"{time.localtime().tm_mday}-{time.localtime().tm_mon}-{time.localtime().tm_year}"
        return current_time
        


if __name__ == "__main__":
    
    #print(BookDao.get_current_time(), type(BookDao.get_current_time()))
    BookDao.update_rating(rating=9, book_id=1)
    print(BookDao.select_by_id(1))