from json import loads
from logging import getLogger

from fastapi import APIRouter
from fastapi import Body, status
from pydantic_core import ValidationError
from starlette.responses import JSONResponse

from db import booksdb, no_id
from models.book import Book, types

logger = getLogger("uvicorn.error")

books_router = APIRouter(prefix="/books", tags=["books"])


@books_router.get("/", status_code=status.HTTP_200_OK)
def get_books():
    logger.error("BOOKS")
    # this works
    found = booksdb.find({}, no_id).to_list()
    # this works as well
    # logger.error(list(booksdb.find()))
    return found


@books_router.get("/by_isbn/{ISBN}", status_code=status.HTTP_200_OK)
def get_book_by_isbn(ISBN: str = types["ISBN"]["path"]):
    found = booksdb.find_one({"ISBN": ISBN}, no_id)
    return {"msg": f"No book with ISBN {ISBN}"} if not found else found


# list of books even if only one found
@books_router.get("/by_author", status_code=status.HTTP_200_OK)
def get_books_by_author(author: str = types["Author"]["query"]):
    found = booksdb.find({"Author": author}, no_id).to_list()
    return {"msg": f"No books for author {author}"} if not found else found


@books_router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(book: dict = Body(...)):
    if len(book.keys()) == 0:
        return JSONResponse({"error": "Model cannot be empty"}, 400)
    try:
        b = Book(**book)
        booksdb.insert_one(b.model_dump())
    except ValidationError as e:
        return JSONResponse({"error": "Validation error", "details": loads(e.json(include_url=False))}, 400)
    except Exception as e:
        raise Exception(f"Couldn't add a book to a db {type(e)}", e)
    return {"msg": "Added", "book": b}


# for now, it requires full model to be present, partial updates not supported yet
@books_router.put("/by_isbn/{ISBN}", status_code=status.HTTP_200_OK)
def update_book_by_isbn(ISBN: str = types["ISBN"]["path"], book: dict = Body(...)):
    if len(book.keys()) == 0:
        return JSONResponse({"error": "Update model cannot be empty"}, 400)
    try:
        b = Book(**book)
        before = booksdb.find_one_and_update({"ISBN": ISBN}, {"$set": b.model_dump()}, no_id)
        return {"msg": "Nothing to update"} if (before is None or before == b) else {
            "msg": f"Book with ISBN {ISBN} updated"}
    except ValidationError as e:
        return JSONResponse({"error": "Validation error", "details": loads(e.json(include_url=False))}, 400)
    except Exception as e:
        raise Exception(f"Couldn't update a book to a db {type(e)}", e)


@books_router.patch("/by_isbn/{ISBN}", status_code=status.HTTP_200_OK)
def update_book_by_isbn(ISBN: str = types["ISBN"]["path"], book: dict = Body(...)):
    if len(book.keys()) == 0:
        return JSONResponse({"error": "Update model cannot be empty"}, 400)
    try:
        fromdb = booksdb.find_one({"ISBN": ISBN}, no_id)
        before = dict(fromdb.items())
        for key in book.copy().keys():
            if fromdb.get(key):
                fromdb[key] = book[key]
            else:
                book.pop(key, None)
        b = Book(**fromdb)
        booksdb.update_one({"ISBN": ISBN}, {"$set": book})
        return {"msg": "Nothing to update"} if (fromdb is None or before == fromdb) else {
            "msg": f"Book with ISBN {ISBN} updated"}
    except ValidationError as e:
        return JSONResponse({"error": "Validation error", "details": loads(e.json(include_url=False))}, 400)
    except Exception as e:
        raise Exception(f"Couldn't update a book to a db {type(e)}", e)


@books_router.delete("/by_isbn/{ISBN}", status_code=status.HTTP_200_OK)
def delete_book_by_isbn(ISBN: str = types["ISBN"]["path"]):
    returned = booksdb.find_one_and_delete({"ISBN": ISBN}, no_id)
    return {"msg": "Nothing to delete"} if not returned else {"msg": f"Book with ISBN {ISBN} deleted", "book": returned}
