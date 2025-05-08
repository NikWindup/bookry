from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
from .Genre import Genre
from .ReadingStatus import ReadingStatus
from datetime import datetime


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    status: str = Field(..., pattern='^(reading|finished|want_to_read)$')
    rating: Optional[int] = Field(None, ge=1, le=5)
    finished_date: Optional[datetime] = None
    cover_id: Optional[int] = None
    publish_year: Optional[int] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    author: Optional[str] = Field(None, min_length=1, max_length=255)
    status: Optional[str] = Field(None, pattern='^(reading|finished|want_to_read)$')


class Book(BookBase):
    id: int
    user_id: int
    author_id: int
    language: Optional[str] = None
    started: Optional[str] = None
    finished: Optional[str] = None
    isbn: str

    class Config:
        from_attributes = True
