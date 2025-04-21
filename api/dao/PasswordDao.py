import sqlite3
from sqlite3 import Connection, Cursor
from api.dao.Dao import Dao
from api.model.User import User


class PasswordDao(Dao):
    
    @staticmethod
    def insert(user: User, hash: str):
        pass