import sqlite3
from sqlite3 import Connection
import os.path


class Dao:

    __path = os.path.join("api", "db.sqlite3")
    
    @staticmethod
    def connect() -> Connection:
        conn: Connection = sqlite3.connect(Dao.__path)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
