from pydantic import BaseModel
from enum import Enum
from typing import List, Optional
from .Genre import Genre
from .ReadingStatus import ReadingStatus


class Book(BaseModel):
    user_id: int
    id: int
    title: str
    author_id: int
    language: Optional[str] = None
    started: Optional[str] = None
    finished: Optional[str] = None
    rating: Optional[int] = None
    isbn: str
    reading_status: Optional[ReadingStatus] = ReadingStatus.wishlist
