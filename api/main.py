"""
Tutorial: https://fastapi.tiangolo.com/tutorial
"""

from fastapi import FastAPI

from SetupDB import SetupDB
from dao.BookDao import BookDao
from dao.GenreDao import GenreDao
from dao.BookGenreDao import BookGenreDao
from dao.AuthorDao import AuthorDao




app = FastAPI()

@app.get("/books/{book_name}")
async def get_book(book: Book):
    
    return {"book_id" : book_id,}

@app.post("/books/")
async def post_book(book: Book):
    return {"message": "Succesfully added book","book": book.model_dump()}
