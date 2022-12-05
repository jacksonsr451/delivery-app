from sqlalchemy import Column, String

from src.core.database import Base


class ProfileModel(Base):
    __tablename__ = 'profiles'

    id = Column(String, primary_key=True)
    name = Column(String)
