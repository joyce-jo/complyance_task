# backend/app/database.py
from sqlmodel import SQLModel, create_engine, Session
import os

# default for local development (when not running in docker-compose)
DEFAULT_DB = "postgresql+psycopg2://complyuser:complypass@localhost:5432/complydb"

# in docker-compose the DB host is "db"
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB)

# create engine; echo can be set via ENV if desired
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)


def init_db():
    # import models so metadata is registered
    from . import models  # noqa: F401
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
