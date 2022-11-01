import datetime

import core.database as _database

import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from sqlalchemy import Column
from sqlalchemy import Integer, String, VARCHAR, Boolean

import passlib.hash as _hash


class User(_database.Base):
    __tablename__ = "users"

    id = _sql.Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_idiot = Column(Boolean)

    def verify_password(self, password: str):
        _hash.bcrypt.verify(password, self.hashed_password)


class Socials(_database.Base):
    __tablename__ = "social_networks"

    id = _sql.Column(Integer, primary_key=True, index=True)
    link = Column(String, unique=True, index=True)
    icon = Column(String, unique=True)


