from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field

# todo async
# todo custom validation
books = [
    {
        "ISBN": "0101019292920",
        "Title": "asfds",
        "Author": "asfds",
        "YearOfPublish": 2001,
        "CoverImage": "asfds",
    },
    {
        "ISBN": "0101019292921",
        "Title": "asfds2",
        "Author": "asfds2",
        "YearOfPublish": 2002,
        "CoverImage": "asfds2",
    }
]

types = {
    "ISBN": {
        "field": Field(..., min_length=13, max_length=13),
        "path": Path(..., min_length=13, max_length=13),
    },
    "Title": {
        "field": Field(..., min_length=1, max_length=100)
    },
    "Author": {
        "field": Field(..., min_length=2, max_length=100),
        "query": Query(..., min_length=2, max_length=100)
    },
    "YearOfPublish": {
        "field": Field(..., ge=1800, le=2025)
    },
    "CoverImage": {
        "field": Field(..., min_length=4, max_length=128)
    }
}


class Book(BaseModel):
    ISBN: str = types["ISBN"]["field"]
    Title: str = types["Title"]["field"]
    Author: str = types["Author"]["field"]
    YearOfPublish: int = types["YearOfPublish"]["field"]
    CoverImage: str = types["CoverImage"]["field"]


app = FastAPI()


@app.get('/')
def home():
    return "HOMEPAGE FOR BOOKS API."


@app.get("/books")
def get_books():
    return books


@app.get("/book/{ISBN}")
def get_book_by_isbn(ISBN: str = types["ISBN"]["path"]):
    for b in books:
        if b["ISBN"] == ISBN:
            return b
    return None


@app.get("/book")
def get_books_by_author(author: str = types["Author"]["query"]):
    return [b for b in books if b["Author"] == author]


@app.put("/book/{ISBN}")
def update_book_by_isbn(ISBN: str = types["ISBN"]["path"], book: dict = Body(...)):
    for i, b in enumerate(books):
        if b["ISBN"] == ISBN:
            books[i] = book
            return {"msg": "Updated", "book": book}
    return {"msg": "Nothing to update"}


@app.delete("/book/{ISBN}")
def delete_book_by_isbn(ISBN: str = types["ISBN"]["path"]):
    for i, b in enumerate(books):
        if b["ISBN"] == ISBN:
            deleted = books.pop(i)
            return {"msg": "Deleted", "book": deleted}
    return {"msg": "Nothing to delete"}


@app.post("/book")
def create_book(book: Book):
    books.append(book.model_dump())
    return {"msg": "Added", "book": book}
