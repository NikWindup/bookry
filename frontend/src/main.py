import flet as ft
import time

from django.db.models import TextField


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def check_credentials(e: ft.ControlEvent):
        if username.value and password.value:
            print(username.value, password.value)

    #  Login Page
    username = ft.TextField(width=250, multiline=False)
    password = ft.TextField(width=250, password=True, multiline=False)
    sign_up_button = ft.ElevatedButton(text="Sign Up")
    login_button = ft.ElevatedButton(text="Log In")

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
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )



if __name__ == "__main__":

    ft.app(target=main)
