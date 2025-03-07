from logging import getLogger

from fastapi import FastAPI

from routes.books import books_router

# todo async functions, motor db driver

logger = getLogger("uvicorn.error")

app = FastAPI()
app.include_router(books_router)

@app.get("/")
def home_page():
    return "HOMEPAGE FOR BOOKS API"