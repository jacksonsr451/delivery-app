from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.core.database import Base


class ContactModel(Base):
    __tablename__ = 'contacts'

    id = Column(String, primary_key=True)
    phone = Column(String)
    whattsapp = Column(String)
    telegram = Column(String)
    email = Column(String)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship('UserModel', foreign_keys=[user_id])
