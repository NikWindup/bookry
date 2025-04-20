import requests
import flet as ft
from config import Routes



class LandingPage(ft.View):
    
    def __init__(self, page: ft.Page):
        super().__init__(Routes.LANDING)
        
        
        
        self.page = page
        
        self.wrapper = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src="")
                ]
            )
        )
        
        self.controls = [
            self.page.appbar,
        ]
