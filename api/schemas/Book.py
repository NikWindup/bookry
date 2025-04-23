from pydantic import BaseModel
from enum import Enum
from typing import List, Optional
from .Genre import Genre


class Book(BaseModel):
    id: int
    title: str
    author: str
    language: str
    genres: List[Genre]
    started: str
    finished: Optional[str]
    rating: int
