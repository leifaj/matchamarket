import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session
from app.models import *

# Load variables from .env file
load_dotenv()

def get_database_url():
    DB_USER = os.getenv("DB_USER", "postgres_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "matchamarket")
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def get_session():
    """
    Returns a SQLAlchemy/SQLModel session.
    """
    with Session(engine) as session:
        yield session

def init_db():
    """
    Initializes the database by creating all tables.
    """
    SQLModel.metadata.create_all(engine)   

# Construct database URL fron env vars
DATABASE_URL = get_database_url()

# Create database engine
engine = create_engine(DATABASE_URL, echo=True)
