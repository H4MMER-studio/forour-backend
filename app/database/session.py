from sqlmodel import SQLModel, create_engine

from app.core import database_settings


database_url = database_settings.POSTGRES_DATABASE_URL
engine       = create_engine(url=database_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)