"""
Tutorial: https://fastapi.tiangolo.com/tutorial
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dao.BookDao import BookDao
from dao.GenreDao import GenreDao
from dao.BookGenreDao import BookGenreDao
from dao.AuthorDao import AuthorDao
from dao.UserDao import UserDao
from schemas.Book import Book
from schemas.User import User
from schemas.Genre import Genre
from typing import List

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:7777"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""User"""

@app.post("/users")
async def post_user(user: User):
    try:
        UserDao.insert(user.email, user.username)
        return {"message" : "Succesful"}
    except Exception as e:
        return {"error" : dict(e)}


"""Books"""

@app.get("/books/{book_id}")
async def get_book(book_id):
    try:    
        book = BookDao.select_by_id(book_id)
        genre_ids = BookGenreDao.select_by_book_id(book_id=book_id)
        genres = []
        for id in genre_ids:
            genres.append(GenreDao.select_by_genre_id(genre_id=id))
        
        return {"book" : book, "genres" : genres}
    except Exception as e:
        return {"error" : str(e)}

@app.post("/books/")
async def post_book(book: Book, genres: List[Genre]):
    try:
        print(book.author_id)
        book_id = BookDao.insert(book)
        for genre in genres:
            BookGenreDao.insert(
                book_id=book_id,
                genre_id=GenreDao.insert(genre_name=genre)
            )
        return {"message": "Succesfully added book", "book": dict(book), "genres" : genres}
    except Exception as e:
        return {"error" : str(e)}
 
@app.post("/genres/")
async def post_genre(genre: Genre):
    try:
        GenreDao.insert(genre_name=genre)
        return {"message" : "success", "genre" : genre}
    except Exception as e:
        return {"error" : str(e)}