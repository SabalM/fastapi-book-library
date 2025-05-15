from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def root():
    return {"message": "Welcome to the Book Library API!"}

@app.get("/ui")
def book_search_ui(request: Request, title: str = None):
    results = []
    if title:
        url = "https://openlibrary.org/search.json"
        response = requests.get(url, params={"title": title})
        if response.status_code == 200:
            data = response.json()
            results = [
                {
                    "title": book.get("title"),
                    "author": book.get("author_name", ["Unknown"])[0],
                    "year": book.get("first_publish_year", "N/A")
                }
                for book in data.get("docs", [])[:5]
            ]
    return templates.TemplateResponse("search.html", {"request": request, "results": results, "title": title})
