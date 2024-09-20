
import random
import string
from module.db import *
import pytest


def test_create_user():
    with Session(engine)as s:
        for i in range(10):
            u = User()
            u.name = random_str()
            u.fullname = random_str()+random_str()
            s.add(u)
        s.commit()


def test_create_address():
    with Session(engine) as s:
        ids = s.scalars(select(User.id)).all()
        for i in range(100):
            id = random.sample(ids, 1)[0]

            address = Address()
            address.user_id = id
            address.email_address = random_str()
            s.add(address)
        s.commit()


def random_str():
    rand_str = random.sample(string.ascii_letters, 10)
    return "".join(rand_str)
