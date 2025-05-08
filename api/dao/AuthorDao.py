from sqlite3 import Connection, Cursor
from dao.Dao import Dao


class AuthorDao(Dao):
    
    @staticmethod
    def insert(name: str) -> int:
        # First check if author exists
        sql_check = """
        SELECT author_id FROM author WHERE name = ?
        """
        
        conn: Connection = AuthorDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql_check, (name,))
        existing_author = cursor.fetchone()
        
        if existing_author:
            return existing_author[0]
        
        # If author doesn't exist, create new one
        sql_insert = """
        INSERT INTO author (name) VALUES (?)
        """
        
        cursor.execute(sql_insert, (name,))
        conn.commit()
        
        return AuthorDao.select_last_rowid()
    
    @staticmethod
    def select_by_author_id(author_id: int) -> str:
        sql = """
        SELECT name FROM author WHERE author_id = ?
        """
        
        conn: Connection = AuthorDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (author_id,))
        name = cursor.fetchone()

        return name[0] if name else None
    
    @staticmethod
    def delete(author_id: int):
        sql = """
        DELETE FROM author WHERE author_id = ?
        """
        
        conn: Connection = AuthorDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (author_id,))
        conn.commit()
        
    @staticmethod
    def select_last_rowid() -> int:
        sql = """
        SELECT author_id FROM author ORDER BY rowid DESC LIMIT 1
        """
        
        conn: Connection = AuthorDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql)
        rowid = cursor.fetchone()
        
        return rowid[0] if rowid else None


if __name__ == "__main__":
    AuthorDao.insert("Lauren Roberts")