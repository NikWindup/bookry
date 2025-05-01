from sqlite3 import Connection, Cursor
from dao.Dao import Dao
import os


class SaltDao(Dao):
    
    @staticmethod
    def insert(user_id: int) -> None:
        sql = """
        INSERT INTO salt (user_id, salt) VALUES (?, ?)
        """
        
        salt = SaltDao.generate_salt()
        
        conn: Connection = SaltDao.connect()
        cursor: Cursor = conn
        cursor.execute(sql, (user_id, salt))
        conn.commit()
        
        return salt
    
    @staticmethod
    def select_by_user_id(user_id: int) -> str:
        sql = """
        SELECT salt FROM salt WHERE user_id = ?
        """
        
        conn: Connection = SaltDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        salt = cursor.fetchone()
        return salt[0]
    
    @staticmethod
    def delete_by_user_id(user_id: int) -> None:
        sql = """
        DELETE FROM salt WHERE user_id = ?
        """
        
        conn: Connection = SaltDao.connect()
        cursor: Cursor = conn
        cursor.execute(sql, (user_id,))
        conn.commit()
    
    def generate_salt():
        salt = os.urandom(16)
        return salt.hex()


if __name__ == "__main__":
    print(SaltDao.generate_salt())