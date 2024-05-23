from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings


engine = create_engine(url=settings.data_base_url, echo=True)
Session = sessionmaker(engine)
Base = declarative_base()


class Database:
    @staticmethod
    def create_tables():
        with Session():
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
