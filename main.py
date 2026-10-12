from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from database import Base, engin
from contextlib import asynccontextmanager
from router import posts, users

@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Startup
    async with engin.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown
    await engin.dispose()

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(posts.router, prefix="/api/posts", tags=["posts"])

