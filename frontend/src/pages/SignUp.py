import flet as ft
from config import Routes
from components.InputField import InputField
from components.Button import Button


class SignUp(ft.View):
    
    def __init__(self, page: ft.Page):
        super().__init__(route=Routes.SIGN_UP)
        
        self.page = page
        
        self.page.bgcolor = ft.Colors.WHITE
        
        self.wrapper = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="bookry", weight=ft.FontWeight.W_700, size=30, text_align=ft.TextAlign.CENTER),
                    InputField(hint_text="E-Mail", bgcolor=ft.Colors.GREY_100),
                    InputField(hint_text="Username", bgcolor=ft.Colors.GREY_100),
                    InputField(hint_text="Password", password=True, can_reveal_password=True, bgcolor=ft.Colors.GREY_100),
                    Button(page=self.page, text="Continue", bgcolor=ft.Colors.BLACK, color=ft.Colors.WHITE)
                ]
            ),
            alignment=ft.alignment.bottom_center,
            height=self.page.height,
            bgcolor=ft.Colors.RED
        )
        
        
        self.controls = [
            self.wrapper,
        ]