"""
Tutorial: https://fastapi.tiangolo.com/tutorial
"""

from fastapi import FastAPI
from fastapi.C
from SetupDB import SetupDB
from dao.BookDao import BookDao
from dao.GenreDao import GenreDao
from dao.BookGenreDao import BookGenreDao
from dao.AuthorDao import AuthorDao
from dao.UserDao import UserDao
from schemas.Book import Book
from schemas.User import User


app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/users")
async def post_user(user: User):
    UserDao.insert(user.email, user.username)

@app.get("/books/{book_id}")
async def get_book(book_id):
    book = BookDao.select_by_id(book_id)
    return book

@app.post("/books/")
async def post_book(book: Book):
    BookDao.insert(book)
    return {"message": "Succesfully added book","book": dict(book)}
