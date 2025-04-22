from pydantic import BaseModel
from enum import Enum
from typing import List
from schemas.Genre import Genre


class Book(BaseModel):
    title: str
    author: str
    language: str
    genres: List[Genre]
    started: str
    finished: str
    rating: int
