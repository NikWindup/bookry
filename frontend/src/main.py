import flet as ft


class GameCodePage(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__("/main-menu")

        self.page = page

        self.page.appbar = ft.AppBar(
            leading=ft.IconButton(icon=ft.Icons.KEYBOARD_RETURN, width=50, height=50, on_click=lambda  _: self.page.go("/main-menu")))

        self.controls = [
            self.page.appbar,
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.TextField(hint_text="Game Code"),
                        ft.FilledButton(text="Join", width=250, height=50)
                    ]
                ),
                alignment=ft.alignment.center
            )
        ]


class SettingsMenu(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/settings")

        self.page = page

        self.language_dropdown = ft.Dropdown(
            width=250,
            options=[
                ft.dropdown.Option("German"),
                ft.dropdown.Option("English"),
            ]
        )

        self.page.appbar = ft.AppBar(
            leading=ft.IconButton(icon=ft.Icons.KEYBOARD_RETURN, width=50, height=50, on_click=lambda  _: self.page.go("/main-menu")),
        )

        self.controls = [
            self.page.appbar,
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.FilledButton(text="Change Username", width=250, height=50),
                        self.language_dropdown,
                        ft.FilledButton(text="Change Password", width=250, height=50)
                    ],
                    spacing=50
                ),
                alignment=ft.alignment.center,
            )
        ]


class MainMenu(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__("/main-menu")
        self.page = page
        self.page.appbar = ft.AppBar(
            leading=ft.IconButton(icon=ft.Icons.KEYBOARD_RETURN, width=50, height=50, on_click=lambda  _: self.page.go("/sign-in")),
            actions=[
                ft.IconButton(icon=ft.Icons.SETTINGS, width=50, height=50, on_click=lambda _: self.page.go("/settings"))
            ]
        )

        self.controls = [
            self.page.appbar,
            ft.Container(
                content=
                    ft.Column(
                        controls=[
                            ft.FilledButton(text="Join", width=250, height=50, on_click=lambda _: self.page.go("/game-code")),
                            ft.FilledButton(text="Create Match", width=250, height=50),
                            ft.FilledButton(text="Create Tournament", width=250, height=50)
                        ]
                    ),
                alignment=ft.alignment.center
            )
        ]


class SignInPage(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__("/sign-in")
        self.page = page
        header = ft.Text(value="Sign In", text_align=ft.TextAlign.CENTER, size=30)
        username = ft.TextField(width=250, multiline=False)
        password = ft.TextField(width=250, password=True, multiline=False)
        sign_up_button = ft.FilledButton(text="Sign Up", width=150, height=40, on_click=lambda  _: self.page.go("/main-menu"))
        sign_in_button = ft.FilledButton(text="Sign In", width=150, height=40, on_click=lambda  _: self.page.go("/main-menu"))

        self.controls = [
            ft.Container(
                content=ft.Column(
                    controls=[
                        header,
                        username,
                        password,
                        ft.Row(
                            controls=[
                                sign_up_button,
                                sign_in_button,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        )
                    ],
                    alignment=ft.alignment.center
                ),
                alignment=ft.alignment.center,
            )
        ]
        self.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

def main(page: ft.Page):

    def route_change(e):
        page.views.clear()
        if page.route == "/sign-in":
            page.views.append(SignInPage(page))
        elif page.route == "/game-code":
            page.views.append(GameCodePage(page))
        elif page.route == "/main-menu":
            page.views.append(MainMenu(page))
        elif page.route == "/settings":
            page.views.append(SettingsMenu(page))

        page.update()

    page.window.width = 400
    page.window.height = 450
    page.window.center()
    page.window.bgcolor = "SYSTEM"

    page.on_route_change = route_change
    page.go("/sign-in")


if __name__ == "__main__":
    ft.app(target=main)
