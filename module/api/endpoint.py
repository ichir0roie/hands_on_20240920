from module.db import *
from module.api import schema, query
import fastapi


app = fastapi.FastAPI()


@app.get("users")
def list_users() -> list[schema.User]:
    users = query.list_users()
    return users
