import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DATABASE_URL")
if database_url is None:
    raise ValueError("DATABASE_URL environment variable is not set")
engine = create_engine(database_url)
    
class Base(DeclarativeBase):
    pass

class Link(Base):
    __tablename__ = 'link'
    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str]
    short_code: Mapped[str] = mapped_column(unique=True)
    clicks: Mapped[int] = mapped_column(default = 0)
    condition: Mapped[bool] = mapped_column(default = True)


