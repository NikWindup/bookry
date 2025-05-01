from sqlite3 import Connection, Cursor
from dao.Dao import Dao
from schemas.User import User


class UserDao(Dao):
    
    @staticmethod
    def insert(email: str, username: str) -> User:
        sql = """
        INSERT INTO user (email, username) VALUES (?, ?)
        """
    
        conn: Connection = UserDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (email, username))
        conn.commit()
        
        rowid = UserDao.select_last_rowid()
        return User(id=rowid, email=email, username=username)

    @staticmethod
    def select_user_by_id(user_id: int) -> User:
        sql = """
        SELECT email, username FROM user WHERE user_id = ?
        """
        
        conn: Connection = UserDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        user_data = cursor.fetchone()
        
        email, username = user_data[0], user_data[1]
        return User(id=user_id, email=email, username=username)

    @staticmethod
    def select_by_email(email: str) -> User:
        sql = """
        SELECT user_id, username FROM user WHERE email = ?
        """
        
        conn: Connection = UserDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (email,))
        user_data = cursor.fetchone()
        try:
            user_id, username = user_data[0], user_data[1]
            return User(id=user_id, email=email, username=username)
        except Exception:
            return None
        
        
    @staticmethod
    def delete_by_id(user_id: int) -> bool:
        sql = """
        DELETE FROM user WHERE user_id = ?
        """
        
        conn: Connection = UserDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        conn.commit()
        
    @staticmethod
    def select_last_rowid():
        sql = """
        select user_id from user order by rowid desc LIMIT 1
        """
        
        conn: Connection = UserDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql)
        rowid = cursor.fetchone()
        
        return rowid[0]


if __name__ == "__main__":
    UserDao.insert(email="nikita.uschakow@icloud.com", username="NikWndup")
    