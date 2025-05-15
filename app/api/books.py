# app/api/books.py
from fastapi import APIRouter, Query
import requests

router = APIRouter()

@router.get("/search")
def search_books(title: str = Query(..., description="Book title to search")):
    url = f"https://openlibrary.org/search.json"
    response = requests.get(url, params={"title": title})
    
    if response.status_code != 200:
        return {"error": "Failed to fetch data from Open Library"}

    data = response.json()
    books = [
        {
            "title": book.get("title"),
            "author": book.get("author_name", ["Unknown"])[0],
            "year": book.get("first_publish_year", "N/A")
        }
        for book in data.get("docs", [])[:5]
    ]
    return {"results": books}
