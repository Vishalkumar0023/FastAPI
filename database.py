from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://vishalmahto@localhost:5432/telusko"
engine=create_engine(db_url)
session=sessionmaker(autoflush=False,autocommit=False,bind=engine)