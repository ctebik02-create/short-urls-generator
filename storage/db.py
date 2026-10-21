from sqlalchemy.orm import Session
from storage.orm import engine, Link
from sqlalchemy import select, delete

with engine.connect() as conn:
    print("Database connection successful")



def add_link_data(original_url, short_code):
    link = Link(original_url=original_url, short_code=short_code)

    with Session(engine) as session:
        session.add(link)
        session.commit()
        session.refresh(link)
        return link

def get_link_by_shortcode(short_code):
    statement = select(Link).where(Link.short_code == short_code)
    with Session(engine) as session:
       link = session.scalar(statement)
    if link is None:
        return None
    return link

def get_all_links():
    statement = select(Link)
    with Session(engine) as session:
        return session.scalars(statement).all()

def clicks_count(short_code):
    statement = select(Link).where(Link.short_code == short_code)
    with Session(engine) as session:
        link = session.scalar(statement)
        if link is None:
            return None
        link.clicks += 1
        session.commit()
        session.refresh(link)
    return link

def delete_link_from_db(short_code):
    statement = delete(Link).where(Link.short_code == short_code)
    with Session(engine) as session:
        result = session.execute(statement)
        session.commit()
        return result.rowcount > 0

def update_origin_link(short_code, new_url):
    statement = select(Link).where(Link.short_code == short_code)
    with Session(engine) as session:
        link = session.scalar(statement)
        if link is None:
            return None
        link.original_url = new_url
        session.commit()
        session.refresh(link)
        return link


