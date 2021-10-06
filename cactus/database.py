import sys

from sqlalchemy import Column, BigInteger, String
from tornado_sqlalchemy import SQLAlchemy


if sys.platform.startswith("win32"):
    database_url = "sqlite:///sql.db"

else:
    database_url = "sqlite:////root/cactus/sql.db"

db = SQLAlchemy(database_url)

class File(db.Model):
    id = Column(BigInteger, primary_key=True)
    password = Column(String(255), nullable=False)
    filename = Column(String(255), unique=True)
