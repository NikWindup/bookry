from dao.Dao import Dao
from sqlite3 import Connection, Cursor


class SetupDB(Dao):
    
    """
    Setting up the tables for "db.sqlite3"
    
    TODO
    - [x] salt
    - [x] hash
    - [x] user
    - [x] books
    - [x] author
    - [x] genre book
    - [x] genre
    """

    def __init__(self):
        super().__init__()
        
        SetupDB.setup_user_table()
        SetupDB.setup_salt_table()
        SetupDB.setup_hash_table()
        SetupDB.setup_author_table()
        SetupDB.setup_genre_table()
        SetupDB.setup_books_table()
        SetupDB.setup_genre_book_table()
    
    @staticmethod
    def setup_salt_table() -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS salt (
            salt_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            salt TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user (user_id)
        )
        """
        
        conn: Connection = Dao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    
    @staticmethod
    def setup_hash_table() -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS hash (
            hash_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            hash TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user (user_id)
        )
        """
        
        conn: Connection = Dao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    
    @staticmethod
    def setup_user_table() -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            username TEXT NOT NULL
        )
        """
        
        conn: Connection = Dao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    
    @staticmethod
    def setup_books_table() -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS book (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            language TEXT,
            started TEXT,
            finished TEXT, rating INTEGER
            )
        """

        conn: Connection = Dao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    
    @staticmethod
    def setup_genre_book_table() -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS book_genre (
            book_id INTEGER,
            genre_id INTEGER,
            PRIMARY KEY (book_id, genre_id)
            FOREIGN KEY (book_id) REFERENCES book (book_id),
            FOREIGN KEY (genre_id) REFERENCES genre (genre_id)
        )
        """
        
        conn: Connection = Dao.connect()
        cursor: Cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    
    @staticmethod
    def setup_genre_table() -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS genre (
            genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """
        
        conn: Connection = Dao.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    @staticmethod
    def setup_author_table() -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS author (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """
        
        conn: Connection = Dao.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()


if __name__ == "__main__":
    SetupDB()
