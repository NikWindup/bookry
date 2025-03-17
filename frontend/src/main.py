import flet as ft
from flet.core.control_event import ControlEvent
from flet.core.page import RouteChangeEvent


class AppLayout:

    def __init__(self, page: ft.Page):



class MainMenu(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__()



class LoginPage(ft.Column):

    def __init__(self):
        super().__init__()

        self.page = page

        header = ft.Text(value="Sign In", text_align=ft.TextAlign.CENTER, size=30)
        username = ft.TextField(width=250, multiline=False)
        password = ft.TextField(width=250, password=True, multiline=False)
        sign_up_button = ft.FilledButton(text="Sign Up", width=150, height=30, on_click=lambda  _: self.page.go("/signup"))
        login_button = ft.FilledButton(text="Sign In", on_click=lambda  _: self.page.go("/home"), width=150, height=30)

        page.add(
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    controls=[
                        header,
                        username,
                        password,
                        ft.Row(
                            controls=[
                                sign_up_button,
                                login_button
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
        )

        self.page.update()


def main(page: ft.Page):
    def main_menu(e: ControlEvent):
        if username.value and password.value:
            page.window.resizable = True
            page.clean()
            page.appbar = ft.AppBar(
                leading=ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, width=50, height=50, on_click=login_menu),
                actions=[
                    ft.IconButton(icon=ft.Icons.SETTINGS, width=50, height=50)
                ]

            )
        page.add(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.FilledButton(text="Join", width=250, height=50),
                        ft.FilledButton(text="Create Game", width=250, height=50),
                        ft.FilledButton(text="Create Tournament", width=250, height=50)
                    ]
                ),
                alignment=ft.alignment.center
            )
        )

        page.update()

    page.window.width = 400
    page.window.height = 450
    page.window.resizable = False
    page.window.center()
    page.window.bgcolor = "SYSTEM"

    LoginMenu()

if __name__ == "__main__":
    ft.app(target=main)
