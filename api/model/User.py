class User:
    
    def __init__(self, id: int, email: str, username: str):
        
        self.__id = id
        self.__email = email
        self.__username = username
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value
