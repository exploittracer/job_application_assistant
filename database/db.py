from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "data" / "jobs.db"

DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(
    f"sqlite:///{DATABASE_PATH}",
    echo=False
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def init_db():
    from database.models import Job, Assessment, Application

    Base.metadata.create_all(bind=engine)


def get_session():
    return SessionLocal()