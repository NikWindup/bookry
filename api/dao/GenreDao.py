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