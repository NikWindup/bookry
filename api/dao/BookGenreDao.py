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
        SELECT genre_id FROM book_genre WHERE book_id = ?
        """
        
        conn: Connection = BookGenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (book_id,))
        genre_ids = cursor.fetchall()
        
        return genre_ids
    
    @staticmethod
    def delete_by_book_id(book_id: int):
        sql = """
        DELETE FROM book_genre WHERE book_id = ?
        """
        
        conn: Connection = BookGenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (book_id,))
        conn.commit()


if __name__ == "__main__":
    pass