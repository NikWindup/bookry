import flet as ft 
import requests


url = "http://127.0.0.1:8000/books/1"

def main(page: ft.Page):
    
    data = requests.get(url=url)
    
    print(data.content)
    
ft.app(target=main)