from sqlite3 import Connection, Cursor
from dao.Dao import Dao
import hashlib


class HashDao(Dao):
    
    @staticmethod
    def insert(user_id: int, salt: str) -> None:
        sql = """
        INSERT INTO hash (user_id, hash) VALUES (?, ?)
        """
        
        conn: Connection = HashDao.connect()
        cursor: Cursor = conn
        cursor.execute(sql, (user_id, salt))
        conn.commit()
    
    @staticmethod
    def select_by_user_id(user_id: int) -> str:
        sql = """
        SELECT hash FROM hash WHERE user_id = ?
        """
        
        conn: Connection = HashDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        salt = cursor.fetchone()
        
        return salt[0]
    
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
        hash = hashlib.sha256(password + salt).hexdigest
        return hash


if __name__ == "__main__":
    HashDao.insert(1, "Kristi123")
    print(HashDao.select_by_user_id(1))
    HashDao.delete_by_user_id(1)
