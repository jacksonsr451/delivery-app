from sqlalchemy import Column, String

from src.core.database import Base


class ContactModel(Base):
    __tablename__ = 'contacts'

    id = Column(String, primary_key=True)
    phone = Column(String)
    whattsapp = Column(String)
    telegram = Column(String)
    email = Column(String)
