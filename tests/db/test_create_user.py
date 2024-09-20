
from module.db import *
import pytest


def test_create_user():
    with Session(engine)as s:
        u = User()
        u.name = "test"
        u.fullname = "testtest"
        s.add(u)
        s.commit()
