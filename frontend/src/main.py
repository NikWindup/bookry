import flet as ft
from config import Routes
from pages.Landing import LandingPage
from pages.SignUp import SignUp
from pages.SignIn import SignIn


def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def route_change(e: ft.RouteChangeEvent):
        page.clean()
        if page.route == Routes.LANDING:
            page.views.append(LandingPage(page=page))
        if page.route == Routes.SIGN_UP:
            page.views.append(SignUp(page=page))
        if page.route == Routes.SIGN_IN:
            page.views.append(SignIn(page=page))
        page.update()
    
    page.on_route_change = route_change
    
    page.go(Routes.LANDING)


if __name__ == "__main__":
    ft.app(target=main)
