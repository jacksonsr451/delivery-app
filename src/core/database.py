import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, declarative_base

load_dotenv()

Base = declarative_base()

engine = create_engine(os.getenv('DB_URL'))

session = create_session(engine)
