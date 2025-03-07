from datetime import datetime
from logging import getLogger

from fastapi import Path, Query
from pydantic import Field, BaseModel, field_validator

logger = getLogger("uvicorn.error")

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
