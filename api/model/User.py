class User:
    
    def __init__(self, id: int, email: str, username: str):
        
        self.__id = id
        self.__email = email
        self.username = username
    
    @property
    def id(self):
        return self.__id
    
    @property
    def email(self):
        return self.__email

    @property
    def username(self):
        return self.username
