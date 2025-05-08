from fastapi import APIRouter, HTTPException, Depends, status
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from schemas.Book import Book, BookCreate, BookUpdate
from core.auth import get_current_user
from schemas.User import User
from schemas.Genre import Genre
from dao.BookDao import BookDao
from dao.GenreDao import GenreDao
from dao.BookGenreDao import BookGenreDao
from dao.AuthorDao import AuthorDao

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[Book])
async def get_user_books(current_user: User = Depends(get_current_user)):
    try:
        books = BookDao.select_by_user_id(user_id=current_user.id)
        return books
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/", response_model=Book)
async def create_book(
    book: BookCreate,
    current_user: User = Depends(get_current_user)
):
    try:
        book_id = BookDao.insert(
            title=book.title,
            author=book.author,
            status=book.status,
            user_id=current_user.id,
            cover_id=book.cover_id if hasattr(book, 'cover_id') else None,
            publish_year=book.publish_year if hasattr(book, 'publish_year') else None
        )
        return BookDao.select_by_id(book_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/{book_id}", response_model=Book)
async def update_book(
    book_id: int,
    book: BookUpdate,
    current_user: User = Depends(get_current_user)
):
    try:
        # Verify book ownership
        existing_book = BookDao.select_by_id(book_id)
        if not existing_book or existing_book.user_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )

        updated_book = BookDao.update(
            book_id=book_id,
            title=book.title,
            author=book.author,
            status=book.status,
            rating=book.rating,
            finished_date=book.finished_date
        )
        return updated_book
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_id: int,
    current_user: User = Depends(get_current_user)
):
    try:
        # Verify book ownership
        existing_book = BookDao.select_by_id(book_id)
        if not existing_book or existing_book.user_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )

        BookDao.delete(book_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/{book_id}")
async def get_book(book_id: int, current_user: User = Depends(get_current_user)):
    try:    
        book = BookDao.select_by_id(book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
            
        author = AuthorDao.select_by_author_id(author_id=book.author_id)
        genre_ids = BookGenreDao.select_by_book_id(book_id=book_id)
        
        genres = []
        for id in genre_ids:
            genres.append(GenreDao.select_by_genre_id(genre_id=id))
        
        return {"book": book, "author": author, "genres": genres}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/")
async def post_book(
    book: Book,
    genres: List[Genre],
    current_user: User = Depends(get_current_user)
):
    try:
        book_id = BookDao.insert(book)
        for genre in genres:
            BookGenreDao.insert(
                book_id=book_id,
                genre_id=GenreDao.insert(genre_name=genre)
            )
        return {
            "message": "Successfully added book",
            "book": dict(book),
            "genres": genres
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/{book_id}/rating")
async def put_rating(
    book_id: int,
    rating: int,
    current_user: User = Depends(get_current_user)
):
    try:
        book = BookDao.select_by_id(book_id=book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
            
        if book.rating:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Book already has a rating"
            )
            
        BookDao.update_rating(book_id=book_id, rating=rating)
        return {"message": "Successfully added the rating"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/{book_id}/finished")
async def put_finished(
    book_id: int,
    current_user: User = Depends(get_current_user)
):
    try:
        book = BookDao.select_by_id(book_id=book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
            
        if book.finished:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Book is already marked as finished"
            )
            
        BookDao.update_finished(book_id=book_id)
        return {"message": "Successfully added the finished date"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/{book_id}/status")
async def put_reading_status(
    book_id: int,
    current_user: User = Depends(get_current_user)
):
    try:
        book = BookDao.select_by_id(book_id=book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
            
        BookDao.update_reading_status(book_id=book_id)
        return {"message": "Successfully changed the reading status"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        ) 