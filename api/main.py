"""
Tutorial: https://fastapi.tiangolo.com/tutorial

This FastAPI application provides endpoints for user registration, login, and book management.

Endpoints:
1. User:
   - POST /register: Register a new user with email, username, and password.
   - POST /login: Log in a user using email and password. Supports JWT authentication.
   - GET /users/me: Get current user profile.

2. Books:
   - GET /books/{book_id}: Retrieve details of a book, including its author and genres.
   - POST /books/: Add a new book with associated genres.
   - PUT /books/{book_id}/rating: Add or update a rating for a book.
   - PUT /books/{book_id}/finished: Mark a book as finished with a completion date.
   - PUT /books/{book_id}/status: Update the reading status of a book.

Middleware:
- CORS: Configured to allow requests from frontend.
- JWT: For authentication.

Dependencies:
- DAO modules for database operations (e.g., UserDao, BookDao, etc.).
- Schema modules for data validation (e.g., Book, User, Genre).

For more details, visit the FastAPI tutorial: https://fastapi.tiangolo.com/tutorial


"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import auth, books

app = FastAPI(title="Bookry API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(books.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Bookry API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
