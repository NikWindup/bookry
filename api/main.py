"""
Tutorial: https://fastapi.tiangolo.com/tutorial
"""

from fastapi import FastAPI
from SetupDB import SetupDB
from dao.BookDao import BookDao
from dao.GenreDao import GenreDao
from dao.BookGenreDao import BookGenreDao
from dao.AuthorDao import AuthorDao
from schemas.Book import Book


app = FastAPI()

@app.get("/books/{book_id}")
async def get_book(book_id):
    book = BookDao.select_by_id(book_id)
    return book

@app.post("/books/")
async def post_book(book: Book):
    return {"message": "Succesfully added book","book": dict(book)}
