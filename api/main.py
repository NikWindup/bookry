"""
Tutorial: https://fastapi.tiangolo.com/tutorial

This FastAPI application provides endpoints for user registration, login, and book management.

Endpoints:
1. User:
   - POST /register: Register a new user with email, username, and password.
   - POST /login: Log in a user using email and password. Supports cookie-based authentication.

2. Books:
   - GET /books/{book_id}: Retrieve details of a book, including its author and genres.
   - POST /books/: Add a new book with associated genres.
   - PUT /books/{book_id}/rating: Add or update a rating for a book.
   - PUT /books/{book_id}/finished: Mark a book as finished with a completion date.
   - PUT /books/{book_id}/status: Update the reading status of a book.

Middleware:
- CORS: Configured to allow requests from http://localhost and http://localhost:7777.

Dependencies:
- DAO modules for database operations (e.g., UserDao, BookDao, etc.).
- Schema modules for data validation (e.g., Book, User, Genre).

For more details, visit the FastAPI tutorial: https://fastapi.tiangolo.com/tutorial


"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dao.BookDao import BookDao
from dao.GenreDao import GenreDao
from dao.BookGenreDao import BookGenreDao
from dao.AuthorDao import AuthorDao
from dao.UserDao import UserDao
from dao.HashDao import HashDao
from dao.SaltDao import SaltDao
from schemas.Book import Book
from schemas.User import User
from schemas.Genre import Genre
from typing import List

app = FastAPI()


origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""User"""

@app.post("/register")
async def post_user(email: str, username: str, password: str):
    try:
        if not UserDao.select_by_email(email=email):
            user = UserDao.insert(email, username)
            salt = SaltDao.insert(user_id=user.id)
            HashDao.insert(user_id=user.id, password=password, salt=salt)
            return {"message" : "Successful"}
        else:
            return {"error" : "Email already taken."}
    except Exception as e:
        return {"error" : str(e)}

@app.post("/login")
async def get_user(email: str, password):
    try:
        requesting_user = UserDao.select_by_email(email=email)
        hash = HashDao.select_by_user_id(user_id=requesting_user.id)
        salt = SaltDao.select_by_user_id(user_id=requesting_user.id)
        
        if requesting_user and HashDao.hash(password=password, salt=salt) == hash:
            return {"message" : "Succesfully logged in"}
    except Exception as e:
        return {"error" : str(e)}

"""Books"""

@app.get("/books/{book_id}")
async def get_book(book_id):
    try:    
        book = BookDao.select_by_id(book_id)
        author = AuthorDao.select_by_author_id(author_id=book.author_id)
        genre_ids = BookGenreDao.select_by_book_id(book_id=book_id)
        
        genres = []
        for id in genre_ids:
            genres.append(GenreDao.select_by_genre_id(genre_id=id))
        
        return {"book" : book, "author" : author, "genres" : genres}
    except Exception as e:
        return {"error" : str(e)}

@app.post("/books/")
async def post_book(book: Book, genres: List[Genre]):
    try:
        book_id = BookDao.insert(book)
        for genre in genres:
            BookGenreDao.insert(
                book_id=book_id,
                genre_id=GenreDao.insert(genre_name=genre)
            )
        return {"message": "Succesfully added book", "book": dict(book), "genres" : genres}
    except Exception as e:
        return {"error" : str(e)}

@app.put("/books/{book_id}/rating")
async def put_rating(book_id: int, rating: int):
    try:
        if not BookDao.select_by_id(book_id=book_id).rating:
            BookDao.update_rating(book_id=book_id, rating=rating)
            return {"message" : "Succesfully added the rating"}
        else:
            return {"message" : "You already put a rating"}
    except Exception as e:
        return {"error" : str(e)}

@app.put("/books/{book_id}/finished")
async def put_finished(book_id):
    try:
        if not BookDao.select_by_id(book_id=book_id).finished:
            BookDao.update_finished(book_id=book_id)
            return {"message" : "Succesfully added the finished date"}
        else:
            return {"message" : "You already finished the book"}
    except Exception as e:
        return {"error" : str(e)}

@app.put("/books/{book_id}/status")
async def put_reading_status(book_id):
    try:
        BookDao.update_reading_status(book_id=book_id)
        return {"message" : "Succesfully changed the reading_status"}
    except Exception as e:
        return {"error" : str(e)}
