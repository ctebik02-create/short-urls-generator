from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



engine = create_engine('sqlite:///database.db')

class Base(DeclarativeBase):
    pass

class Link(Base):
    __tablename__ = 'link'
    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str]
    short_code: Mapped[str] = mapped_column(unique=True)
    clicks: Mapped[int] = mapped_column(default = 0)

def init_db():
    Base.metadata.create_all(engine)

