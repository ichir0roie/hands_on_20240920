from module.api import schema, query
import fastapi
from module.db import engine, Session

app = fastapi.FastAPI()


@app.get("/users")
def list_users() -> list[schema.User]:
    with Session(engine) as s:
        users = query.list_users(s)
        return users
