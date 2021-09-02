from sqlmodel import SQLModel, Session, create_engine

from app.core import local_database_settings


database_url = local_database_settings.URL
engine       = create_engine(url=database_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as db:
        yield db