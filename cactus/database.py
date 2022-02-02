import datetime
import sys
import os
from sqlalchemy import Column, BigInteger, String, Integer, DateTime
from tornado_sqlalchemy import SQLAlchemy

if os.getenv("CACTUS") == "docker":
    database_url = "sqlite:////db/sql.db?check_same_thread=False"
else:
    if sys.platform.startswith("win32"):
        database_url = "sqlite:///db/sql.db"

    else:
        database_url = "sqlite:////root/cactus/db/sql.db"

db = SQLAlchemy(database_url)

class File(db.Model):
    __tablename__ = "file"
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, autoincrement=True)
    password = Column(String(255), nullable=False)
    filename = Column(String(255), unique=True)
    created_on = Column(DateTime, default=datetime.datetime.now)
