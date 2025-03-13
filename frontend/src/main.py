import flet as ft
from flet.core.control_event import ControlEvent


def main(page: ft.Page):
    def check_credentials(e: ControlEvent):
        if username.value and password.value:
            print(username.value, password.value)
            print(page.route)

    def switch_page(e: ControlEvent):
        if page.route == "/":
            page.clean()
            page.add(
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_BACK_IOS),
                        ft.IconButton(icon=ft.icons.SETTINGS)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                ),
                ft.Column(
                    controls=[]
                )

            )


    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 200
    page.window.height = 250
    page.window.resizable = False
    page.route = "/"


    #  Login Page
    username = ft.TextField(width=250, multiline=False)
    password = ft.TextField(width=250, password=True, multiline=False)
    sign_up_button = ft.Button(text="Sign Up", on_click=check_credentials)
    login_button = ft.ElevatedButton(text="Log In", on_click=check_credentials)

    page.add(
        ft.Column(
            controls=[
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
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )



if __name__ == "__main__":

    ft.app(target=main)
