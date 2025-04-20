import sqlite3
from sqlite3 import Connection, Cursor
from Dao import Dao
from model.User import User


class UserDao(Dao):
    
    def insert(user: User) -> User:
        sql = """
        
        """
    
    def select_user_by_id(user_id: int) -> User:
        sql = """
        
        """
        
    def delete(user_id: int) -> bool:
        sql = """
        
        """