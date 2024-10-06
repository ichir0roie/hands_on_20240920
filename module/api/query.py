from module.db import *


def list_users(s: Session) -> list[User]:
    q = select(
        User
    )
    users = s.scalars(q).unique().all()
    # users = [u for u in users]  # fetch
    return users
