from enum import Enum


class ReadingStatus(str, Enum):
    
    wishlist = "wishlist"
    reading = "reading"
    finished = "finished"
