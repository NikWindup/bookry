from sqlite3 import Connection, Cursor
from dao.Dao import Dao
from schemas.Book import Book
import time


class BookDao(Dao):
    
    @staticmethod
    def insert(book: Book) -> int:
        sql = """
        INSERT INTO book (user_id, title, author_id, language, started, isbn) VALUES (?, ?, ?, ?, ?, ?)
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(
            sql,
            (
                book.user_id,
                book.title,
                book.author_id,
                book.language,
                BookDao.__get_current_time(),
                book.isbn
            )
        )
        conn.commit()
        
        return BookDao.select_last_rowid()

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
        SELECT user_id, title, author_id, language, started, finished, rating, isbn FROM book WHERE book_id = ?
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (book_id,))
        book_data = cursor.fetchone()
        print(book_data)
        
        return Book(
            id=book_id,
            user_id=book_data[0],
            title=book_data[1] ,
            author_id=book_data[2],
            language=book_data[3],
            started=book_data[4],
            finished=book_data[5],
            rating=book_data[6],
            isbn=book_data[7]
        )
        
    @staticmethod
    def delete(book_id: int):
        sql = """
        DELETE FROM book WHERE book_id = ?
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(
            sql,
            (book_id,)
        )
        conn.commit()
        
        
    @staticmethod
    def select_last_rowid():
        sql = """
        select book_id from book order by rowid desc LIMIT 1
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql)
        rowid = cursor.fetchone()
        
        return rowid[0]

    @staticmethod
    def __get_current_time():
        current_time = f"{time.localtime().tm_mday}-{time.localtime().tm_mon}-{time.localtime().tm_year}"
        return current_time
        


if __name__ == "__main__":
    BookDao.insert(user_id=1, title="Reckless", author_id=1, language="en", isbn="123342345")
    print(BookDao.select_by_id(3))
    
