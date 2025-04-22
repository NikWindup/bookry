from sqlite3 import Connection, Cursor
from dao.Dao import Dao
from schemas.Genre import Genre

class GenreDao(Dao):
    
    @staticmethod
    def insert(genre_name: str):
        sql = """
        INSERT INTO genre (name) VALUES (?)
        """
        
        conn: Connection = GenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (genre_name,))
        conn.commit()
    
    @staticmethod
    def select_by_genre_id(genre_id: int):
        sql = """
        SELECT name FROM genre WHERE genre_id = ?
        """
        
        conn: Connection = GenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (genre_id,))
    
    @staticmethod
    def delete_by_genre_id(genre_id: int):
        sql = """
        DELETE FROM genre WHERE genre_id = ?
        """
        
        conn: Connection = GenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (genre_id,))
        conn.commit()
