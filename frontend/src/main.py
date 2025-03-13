import flet as ft
from flet.core.control_event import ControlEvent
from flet.core.page import RouteChangeEvent


def main(page: ft.Page):

    def main_menu(e: ControlEvent):
        if username.value and password.value:
            print(username.value, password.value)
            print(page.route)
            page.window.resizable = True
            page.clean()
            page.add(
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS),
                        ft.IconButton(icon=ft.Icons.SETTINGS)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                ),
                ft.Column(
                    controls=[
                        ft.ElevatedButton(text="Join"),
                        ft.ElevatedButton(text="Create Game"),
                        ft.ElevatedButton(text="Create Tournament")
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                )
            )
            page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 450
    page.window.resizable = False


    #  Login Page
    username = ft.TextField(width=250, multiline=False)
    password = ft.TextField(width=250, password=True, multiline=False)
    sign_up_button = ft.Button(text="Sign Up", width=100)
    login_button = ft.ElevatedButton(text="Sign In", on_click=main_menu, width=100)

    page.add(
        ft.Column(
            controls=[
                ft.Text(value="Sign In", text_align=ft.TextAlign.CENTER, size=30),
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
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )
    )



if __name__ == "__main__":

    ft.app(target=main)
