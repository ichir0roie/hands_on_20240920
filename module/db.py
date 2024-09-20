# 型ヒントの改善
from __future__ import annotations
# 基礎インポート
import os
from sqlalchemy import (
    create_engine,
    select,
    delete,
    insert,
    MetaData,
    ForeignKey,
    INTEGER,
    String,
    TIMESTAMP,
)
from sqlalchemy.orm import (
    Query,
    DeclarativeBase,
    Session,
    Mapped,
    mapped_column,
    relationship,
)

# 接続設定
# https://docs.sqlalchemy.org/en/20/core/engines.html#sqlite


# sqlite://<nohostname>/<path>
# where <path> is relative:
db_relative_path = "data/sqlite.db"
os.makedirs(os.path.dirname(db_relative_path), exist_ok=True)
engine = create_engine(f"sqlite:///{db_relative_path}")


# 定義
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String(30), nullable=False)
    fullname: Mapped[String] = mapped_column(String(30), nullable=False)

    addresses: Mapped[list[Address]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email_address: Mapped[String] = mapped_column(String(30), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), nullable=False)

    user: Mapped[User] = relationship(back_populates="addresses")
