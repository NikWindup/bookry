import sqlite3
from sqlite3 import Connection, Cursor
from dao.Dao import Dao
from schemas.Book import Book

class BookDao(Dao):
    
    @staticmethod
    def insert(book: Book):
        sql = """
        
        """