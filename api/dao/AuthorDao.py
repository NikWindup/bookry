from sqlite3 import Connection, Cursor
from api.dao.Dao import Dao


class AuthorDao(Dao):
    
    @staticmethod
    def insert(name: str):
        sql = """
        INSERT INTO author (name) VALUES (?)
        """
        
        conn: Connection = AuthorDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (name,))
        conn.commit()
    
    @staticmethod
    def select_by_author_id(author_id: int):
        sql = """
        SELECT name FROM author WHERE author_id = ?
        """
        
        conn: Connection = AuthorDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (author_id,))
        name = cursor.fetchone()

        return name[0]
    
    @staticmethod
    def delete(author_id: int):
        sql = """
        DELETE FROM author WHERE author_id = ?
        """
        
        conn: Connection = AuthorDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (author_id,))
        conn.commit()


if __name__ == "__main__":
    AuthorDao.insert("Lauren Roberts")