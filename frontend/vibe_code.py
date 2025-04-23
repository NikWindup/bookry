import flet as ft
import requests

# ---------------------
# Get best cover ID (ISBN or OLID)
# ---------------------
async def search_book_get_cover_id(title, author=None):
    query = f"title={title}"
    if author:
        query += f"&author={author}"

    search_url = f"https://openlibrary.org/search.json?{query.replace(' ', '+')}"
    response = await requests.get(search_url)

    if response.status_code != 200:
        return None

    data = response.json()

    for book in data.get("docs", []):
        if "isbn" in book:
            return book["isbn"][0], book.get("title", "Unknown Title"), "isbn"
        elif "cover_edition_key" in book:
            return book["cover_edition_key"], book.get("title", "Unknown Title"), "olid"

    return None

# ---------------------
# Generate the correct cover URL
# ---------------------
def get_cover_url(id_value, id_type, size="L"):
    return f"https://covers.openlibrary.org/b/{id_type}/{id_value}-{size}.jpg"

# ---------------------
# Flet UI App
# ---------------------
def main(page: ft.Page):
    page.title = "OpenLibrary Book Cover Viewer"
    page.padding = 20
    page.scroll = "auto"

    title_input = ft.TextField(label="Book Title", expand=True)
    author_input = ft.TextField(label="Author (optional)", expand=True)
    result_area = ft.Column()

    def on_search_click(e):
        result_area.controls.clear()

        result = search_book_get_cover_id(title_input.value, author_input.value)
        if result:
            cover_id, book_title, id_type = result
            cover_url = get_cover_url(cover_id, id_type)

            result_area.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(book_title, size=20, weight="bold"),
                            ft.Image(src=cover_url, width=200, height=300, fit=ft.ImageFit.CONTAIN),
                        ]),
                        padding=20
                    )
                )
            )
        else:
            result_area.controls.append(ft.Text("❌ No book found.", color="red"))

        page.update()

    page.add(
        ft.Row([
            title_input,
            author_input,
            ft.ElevatedButton("Search", on_click=on_search_click)
        ]),
        result_area
    )

ft.app(target=main)
