import flet as ft 
import requests


url = "https://silver-winner-5gvpxw4gr6wfpxqp-8000.app.github.dev/books/1"

def main(page: ft.Page):
    
    data = requests.get(url=url)
    
    data = dict(data.content)

    for k, v in data.items():
        ft.Text(value=v)
    
ft.app(target=main)