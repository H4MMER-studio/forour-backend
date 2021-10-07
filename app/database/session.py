from sqlmodel import SQLModel, Session, create_engine

from app.core import database_settings


engine = create_engine(url=database_settings.URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as db:
        yield db