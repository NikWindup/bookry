from sqlite3 import Connection, Cursor
from dao.Dao import Dao


class SaltDao(Dao):
    
    @staticmethod
    def insert(user_id: int, salt: str) -> None:
        sql = """
        INSERT INTO salt (user_id, salt) VALUES (?, ?)
        """
        
        conn: Connection = SaltDao.connect()
        cursor: Cursor = conn
        cursor.execute(sql, (user_id, salt))
        conn.commit()
    
    @staticmethod
    def select_by_user_id(user_id: int) -> str:
        sql = """
        SELECT salt FROM salt WHERE user_id = ?
        """
        
        conn: Connection = SaltDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        salt = cursor.fetchone()
        return salt
    
    @staticmethod
    def delete_by_user_id(user_id: int) -> None:
        sql = """
        DELETE FROM salt WHERE user_id = ?
        """
        
        conn: Connection = SaltDao.connect()
        cursor: Cursor = conn
        cursor.execute(sql, (user_id,))
        conn.commit()


if __name__ == "__main__":
    print(SaltDao.delete_by_user_id(0))