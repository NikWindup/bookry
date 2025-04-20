"""
Tutorial: https://fastapi.tiangolo.com/tutorial
"""

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import List


class Genre(str, Enum):
    """Where I found the genres: https://blog.reedsy.com/book-genres/"""
    
    """Fiction genres"""
    fantasy = "fantasy"
    science_fiction = "science-fiction"
    romance = "romance"
    action = "action"
    adventure = "adventure"
    mystery = "mystery"
    horror = "horror"
    thriller = "thriller"
    suspense = "suspense"
    dystopian = "dystopian"
    big_brain = "Big Brain 🧠"
    
    """Nonfiction genres"""
    biography = "biography"
    history = "history"
    travel = "travel"
    humor = "humor"
    essay = "essay"
    how_to = "how-to"
    science_technology = "science-&-technology"


class Book(BaseModel):
    title: str
    author: str
    language: str
    genres: List[Genre]
    started: str
    finished: str
    rating: int
    

app = FastAPI()

@app.get("/genres/{genre}")
async def get_genre(genre: Genre):
    if genre is Genre.fantasy:
        return {"genre" : genre, "message" : "You are reading Fantasy"}
    
    if genre is Genre.romance:
        print(genre)
        return {"genre" : genre, "message" : f"You are reading {genre}"}
    
    if genre is Genre.action:
        return {"genre" : genre, "message" : f"You are reading {genre}"}
    
    if genre is Genre.adventure:
        return {"genre" : genre, "message" : f"You are reading {genre}"}
    
    if genre is Genre.biography:
        return {"genre" : genre, "message" : f"You are reading {genre}"}
    
    return {"genre" : genre, "message" : "what happened"}

@app.post("/genres/")
async def post_genre(genre: Genre):
    return genre
