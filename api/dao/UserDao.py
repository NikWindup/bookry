from sqlite3 import Connection, Cursor
from dao.Dao import Dao
from model.User import User


class UserDao(Dao):
    
    @staticmethod
    def insert(user: User) -> User:
        sql = """
        INSERT INTO user (email, username) VALUES (?, ?)
        """
    
        conn: Connection = UserDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (user.email, user.username))
        conn.commit()

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
    def delete_by_id(user_id: int) -> bool:
        sql = """
        DELETE FROM user WHERE user_id = ?
        """
        
        conn: Connection = UserDao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        conn.commit()


if __name__ == "__main__":
    UserDao.insert(User(-1, "nikita.uschakow@icloud.comi", "Nikita"))
    