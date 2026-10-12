from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engin = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}, #Not know why
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)

class Base(DeclarativeBase): #Not know why
    pass

def get_db():
    with SessionLocal() as db:
        yield db