import flet as ft


class InputField(ft.TextField):
    
    def __init__(
        self,
        hint_text: str,
        password: bool | None = None,
        can_reveal_password: bool | None = None
    ):
        super().__init__()
        
        self.border_width = 2
        self.border_color = ft.Colors.BLACK
        self.border_radius = 10

        self.hint_text = hint_text
        self.password = password
        self.can_reveal_password = can_reveal_password
