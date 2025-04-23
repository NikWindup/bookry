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
    big_brain = "big-brain-🧠"  # By a request of the lovely client 
    young_adult = "young-adult"
    
    """Nonfiction genres"""
    biography = "biography"
    history = "history"
    travel = "travel"
    humor = "humor"
    essay = "essay"
    how_to = "how-to"
    science_technology = "science-&-technology"
