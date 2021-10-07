import sys

from sqlalchemy import Column, BigInteger, String, Integer
from tornado_sqlalchemy import SQLAlchemy


if sys.platform.startswith("win32"):
    database_url = "sqlite:///sql.db"

else:
    database_url = "sqlite:////root/cactus/sql.db"

db = SQLAlchemy(database_url)

class File(db.Model):
    __tablename__ = "file"
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, autoincrement=True)
    password = Column(String(255), nullable=False)
    filename = Column(String(255), unique=True)
