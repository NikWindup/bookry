from sqlite3 import Connection, Cursor
from dao.Dao import Dao
from schemas.Genre import Genre

class GenreDao(Dao):
    
    @staticmethod
    def insert(genre_name: str) -> int:
        sql = """
        INSERT INTO genre (name) VALUES (?)
        """
        
        conn: Connection = GenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (genre_name,))
        conn.commit()
        
        return GenreDao.select_last_rowid()
    
    @staticmethod
    def select_by_genre_id(genre_id: int) -> None:
        sql = """
        SELECT name FROM genre WHERE genre_id = ?
        """
        
        conn: Connection = GenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (genre_id,))
    
    @staticmethod
    def delete_by_genre_id(genre_id: int) -> None:
        sql = """
        DELETE FROM genre WHERE genre_id = ?
        """
        
        conn: Connection = GenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (genre_id,))
        conn.commit()
    
    @staticmethod
    def select_last_rowid() -> int:
        sql = """
        select genre_id from genre order by rowid desc LIMIT 1
        """
        
        conn: Connection = GenreDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql)
        rowid = cursor.fetchone()
        
        return rowid[0]


if __name__ == "__main__":
    GenreDao.insert(Genre.romance)