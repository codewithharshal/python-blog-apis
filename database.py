from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
ACYNC_SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"


engin = create_async_engine(
    ACYNC_SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}, #Not know why
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)
AsyncSessionLocal = async_sessionmaker(engin, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase): #Not know why
    pass

# def get_db():
#     with SessionLocal() as db:
#         yield db

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session