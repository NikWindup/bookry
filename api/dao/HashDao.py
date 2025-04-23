from sqlite3 import Connection, Cursor
from dao.Dao import Dao


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
        return salt
    
    @staticmethod
    def delete_by_user_id(user_id: int) -> None:
        sql = """
        DELETE FROM hash WHERE user_id = ?
        """
        
        conn: Connection = HashDao.connect()
        cursor: Cursor = conn
        cursor.execute(sql, (user_id,))
        conn.commit()


if __name__ == "__main__":
    HashDao.insert(0, "Kristi123")
    print(HashDao.select_by_user_id(0))
    HashDao.delete_by_user_id(0)