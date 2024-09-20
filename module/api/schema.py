from pydantic import BaseModel


class Address(BaseModel):
    id: int
    email_address: str
    # user_id:int


class User(BaseModel):
    id: int
    name: str
    fullname: str

    addresses: list[Address]
