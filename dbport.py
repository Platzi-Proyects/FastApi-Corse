from fastapi import Depends, FastAPI
from typing import Annotated
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
import os
from contextlib import asynccontextmanager

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definido en el archivo .env")
engine = create_engine(DATABASE_URL)

@asynccontextmanager
async def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    
def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]
