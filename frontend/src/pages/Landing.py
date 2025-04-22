import flet as ft
from config import Routes
from components.Button import Button



class LandingPage(ft.View):
    
    def __init__(self, page: ft.Page):
        super().__init__(Routes.LANDING)
        
        self.page = page
        
        self.wrapper = ft.Container(
            content=ft.Column(
                controls=[
                    Button(page=self.page, text="Sign Up", bgcolor=ft.Colors.GREY_900, color=ft.Colors.WHITE, on_click=lambda _: self.page.go(Routes.SIGN_UP)),
                    Button(page=self.page, text="Sign In", bgcolor=ft.Colors.BLACK, color=ft.Colors.WHITE, on_click=lambda _: self.page.go(Routes.SIGN_IN))
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            alignment=ft.alignment.bottom_center
        )
        
        self.controls = [
            self.wrapper,
        ]
