import json
import logging
from datetime import datetime

from fastapi import FastAPI, Path, Query, Body, status
from pydantic import BaseModel, Field, field_validator
from pydantic_core import ValidationError
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from starlette.responses import JSONResponse

from dummygen import Dummygen

# todo async functions, motor db driver

logger = logging.getLogger("uvicorn.error")
no_id = {"_id": 0}

try:
    uri = "mongodb://127.0.0.1/fastapi"
    logger.error("DBCON?")
    client = MongoClient(uri, connectTimeoutMS=2000, timeoutMS=2000)
    client.server_info()
    db = client.get_database()
    booksdb = db.get_collection("books")

    # populate collection if empty
    if booksdb.find_one({}, no_id) is None:
        books_to_insert = Dummygen.gen_db_books(20)
        booksdb.insert_many(books_to_insert)

except ServerSelectionTimeoutError:
    logger.error("DATABASE IS NOT RUNNING!")
    raise Exception("NO DB!")
except Exception as e:
    raise Exception("DB ERROR", e)
else:
    logger.error("CONNECTED")

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
        "field": Field(..., ge=1800)
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

    @field_validator("YearOfPublish")
    @classmethod
    def validate_year(cls, value):
        logger.error(value)
        if value > datetime.now().year:
            raise ValueError("Year of publish cannot be from the future")
        return value


app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
def home():
    return "HOMEPAGE FOR BOOKS API."


@app.get("/books", status_code=status.HTTP_200_OK)
def get_books():
    logger.error("BOOKS")
    # this works
    found = booksdb.find({}, no_id).to_list()
    # this works as well
    # logger.error(list(booksdb.find()))
    return found


@app.get("/book/{ISBN}", status_code=status.HTTP_200_OK)
def get_book_by_isbn(ISBN: str = types["ISBN"]["path"]):
    found = booksdb.find_one({"ISBN": ISBN}, no_id)
    return {"msg": f"No book with ISBN {ISBN}"} if not found else found


# list of books even if only one found
@app.get("/book", status_code=status.HTTP_200_OK)
def get_books_by_author(author: str = types["Author"]["query"]):
    found = booksdb.find({"Author": author}, no_id).to_list()
    return {"msg": f"No books for author {author}"} if not found else found


@app.post("/book", status_code=status.HTTP_201_CREATED)
def create_book(book: dict = Body(...)):
    if len(book.keys()) == 0:
        return JSONResponse({"error": "Model cannot be empty"}, 400)
    try:
        b = Book(**book)
        booksdb.insert_one(b.model_dump())
    except ValidationError as e:
        return JSONResponse({"error": "Validation error", "details": json.loads(e.json(include_url=False))}, 400)
    except Exception as e:
        raise Exception(f"Couldn't add a book to a db {type(e)}", e)
    return {"msg": "Added", "book": b}


#for now, it requires full model to be present, partial updates not supported yet
@app.put("/book/{ISBN}", status_code=status.HTTP_200_OK)
def update_book_by_isbn(ISBN: str = types["ISBN"]["path"], book: dict = Body(...)):
    if len(book.keys()) == 0:
        return JSONResponse({"error": "Update model cannot be empty"}, 400)
    try:
        b = Book(**book)
        before = booksdb.find_one_and_update({"ISBN": ISBN}, {"$set": b.model_dump()}, no_id)
        return {"msg": "Nothing to update"} if (before is None or before == b) else {"msg": f"Book with ISBN {ISBN} updated"}
    except ValidationError as e:
        return JSONResponse({"error": "Validation error", "details": json.loads(e.json(include_url=False))}, 400)
    except Exception as e:
        raise Exception(f"Couldn't update a book to a db {type(e)}", e)


# todo consider .patch for partial update


@app.delete("/book/{ISBN}", status_code=status.HTTP_200_OK)
def delete_book_by_isbn(ISBN: str = types["ISBN"]["path"]):
    returned = booksdb.find_one_and_delete({"ISBN": ISBN}, no_id)
    return {"msg": "Nothing to delete"} if not returned else {"msg": f"Book with ISBN {ISBN} deleted", "book": returned}
