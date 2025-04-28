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

@app.post("/register")
async def post_user(user: User):
    try:
        if not UserDao.select_by_email(user.email):
            UserDao.insert(user.email, user.username)
            return {"message" : "Succesful"}
        else:
            return {"message" : "User by this credentials already exists. Consider loging in."}
    except Exception as e:
        return {"error" : str(e)}

@app.post("/login")
async def get_user(email: str, password):
    try:
        requesting_user = UserDao.select_by_email(email=email)
        
        if UserDao.select_user_by_id(user_id=requesting_user.id):
            return {}

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
