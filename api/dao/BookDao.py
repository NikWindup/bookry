from sqlite3 import Connection, Cursor
from dao.Dao import Dao
from schemas.Book import Book
from schemas.ReadingStatus import ReadingStatus
import time
from dao.AuthorDao import AuthorDao


class BookDao(Dao):
    
    @staticmethod
    def insert(title: str, author: str, status: str, user_id: int, cover_id: int = None, publish_year: int = None) -> int:
        # First insert the author
        author_id = AuthorDao.insert(author)
        
        sql = """
        INSERT INTO book (user_id, title, author_id, language, started, isbn, reading_status) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(
            sql,
            (
                user_id,
                title,
                author_id,
                "en",  # Default language
                BookDao.__get_current_time(),
                f"ISBN-{int(time.time())}",  # Generate a temporary ISBN
                status
            )
        )
        conn.commit()
        
        return BookDao.select_last_rowid()

    @staticmethod
    def update_finished(book_id: int):
        sql = """
        UPDATE book SET finished = ? WHERE book_id = ?
        """
        
        finished_time = BookDao.__get_current_time()  # Date-Format: dd-(m)m-yyyy
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (finished_time, book_id))
        conn.commit()
    
    @staticmethod
    def update_reading_status(book_id: int, status: ReadingStatus):
        sql = """
        UPDATE book SET reading_status = ? WHERE book_id = ?
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (status, book_id))
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
        SELECT b.user_id, b.title, b.author_id, b.language, b.started, b.finished, b.rating, b.isbn, b.reading_status, a.name as author_name
        FROM book b
        LEFT JOIN author a ON b.author_id = a.author_id
        WHERE b.book_id = ?
        """
        
        conn: Connection = BookDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (book_id,))
        book_data = cursor.fetchone()
        
        if not book_data:
            return None
            
        return Book(
            id=book_id,
            user_id=book_data[0],
            title=book_data[1],
            author=book_data[9],  # author_name from the join
            author_id=book_data[2],
            language=book_data[3],
            started=book_data[4],
            finished=book_data[5],
            rating=book_data[6],
            isbn=book_data[7],
            status=book_data[8]  # reading_status
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
    BookDao.insert(user_id=1, title="Reckless", author_id=1, isbn="123342345")
    print(BookDao.select_by_id(3))
    
