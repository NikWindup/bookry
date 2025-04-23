from pydantic import BaseModel
from enum import Enum
from typing import List, Optional
from .Genre import Genre


class Book(BaseModel):
    id: int
    title: str
    author: int
    language: Optional[str] = None
    started: Optional[str] = None
    finished: Optional[str] = None
    rating: Optional[int] = None
    isbn: str
