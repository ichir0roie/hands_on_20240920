from module.db import *


def list_users() -> list[User]:
    q = select(
        User
    )
    with Session(engine) as s:
        users = s.scalars(q).unique().all()
        # users = [u for u in users]  # fetch
    return users
