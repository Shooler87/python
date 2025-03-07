import logging

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from dummygen import Dummygen


class Settings(BaseSettings):
    api_name: str = "Default API"
    api_version: str = "0.0"
    db_con_str: SecretStr | str = "ERROR"
    default_collection: str = None
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
logger = logging.getLogger("uvicorn.error")
logger.error(settings)
no_id = {"_id": 0}

try:
    if settings.db_con_str == SecretStr("ERROR"):
        raise Exception("HANDLED", "NO DB CONNECTION STRING IN CONFIG!")

    uri = settings.db_con_str.get_secret_value()
    logger.info("DBCON?")
    client = MongoClient(uri, connectTimeoutMS=2000, timeoutMS=2000)
    client.server_info()
    db = client.get_database()
    booksdb = db.get_collection(settings.default_collection)

    # populate collection if empty
    if booksdb.find_one({}, no_id) is None:
        books_to_insert = Dummygen.gen_db_books(20)
        booksdb.insert_many(books_to_insert)

except ServerSelectionTimeoutError as e:
    logger.critical(f"HANDLED DB ERROR: DATABASE IS NOT RUNNING!! {type(e)}")
except Exception as e:
    if e.args[0] == "HANDLED":
        logger.critical(f"HANDLED DB ERROR: {e.args[1]} {type(e)}")
    else:
        logger.critical("DB ERROR", e)
else:
    logger.error("CONNECTED")
