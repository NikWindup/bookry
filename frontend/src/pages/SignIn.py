import flet as ft 
from config import Routes


class SignIn(ft.View):
    
    def __init__(self, page: ft.Page):
        super().__init__(route=Routes.SIGN_IN)