from sqlite3 import Connection, Cursor
from dao.Dao import Dao
import hashlib


class HashDao(Dao):
    
    @staticmethod
    def insert(user_id: int, password: str, salt: str) -> None:
        sql = """
        INSERT INTO hash (user_id, hash) VALUES (?, ?)
        """
        hash = HashDao.hash(password=password, salt=salt)
        conn: Connection = HashDao.connect()
        cursor: Cursor = conn
        cursor.execute(sql, (user_id, hash))
        conn.commit()
        
        return hash
    
    @staticmethod
    def select_by_user_id(user_id: int) -> str:
        sql = """
        SELECT hash FROM hash WHERE user_id = ?
        """
        
        conn: Connection = HashDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        hash = cursor.fetchone()
        print(user_id)
        return hash[0]
    
    @staticmethod
    def delete_by_user_id(user_id: int) -> None:
        sql = """
        DELETE FROM hash WHERE user_id = ?
        """
        
        conn: Connection = HashDao.connect()
        cursor: Cursor = conn
        cursor.execute(sql, (user_id,))
        conn.commit()
    
    @staticmethod
    def hash(password: str, salt: str):
        hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return hash
