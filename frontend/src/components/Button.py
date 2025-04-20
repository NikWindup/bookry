import flet as ft


class Button(ft.CupertinoButton):
    
    def __init__(
        self,
        page: ft.Page,
        text: str
    ):
        super().__init__()
        
        self.page = page
        
        self.width = self.page.width
        self.height = 30
        
        self.bgcolor = ft.Colors.BLACK
        self.color = ft.Colors.WHITE
        self.border_radius = 5
        
        self.text = 