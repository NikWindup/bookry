import flet as ft
from config import Routes
from components.InputField import InputField
from components.Button import Button


class SignIn(ft.View):
    
    def __init__(self, page: ft.Page):
        super().__init__(route=Routes.SIGN_IN)
        
        self.page = page
        
        self.page.bgcolor = ft.Colors.WHITE
        
        self.wrapper = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="bookry", weight=ft.FontWeight.W_700, size=30, text_align=ft.TextAlign.CENTER),
                    InputField(hint_text="E-Mail"),
                    InputField(hint_text="Username"),
                    InputField(hint_text="Password", password=True, can_reveal_password=True),
                    Button(page=self.page, text="Continue")
                ]
            ),
            alignment=ft.alignment.center,
        )
        
        
        self.controls = [
            self.wrapper,
        ]