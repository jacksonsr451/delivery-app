from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Base


class ProfileModel(Base):
    __tablename__ = 'profiles'

    id = Column(String, primary_key=True)
    name = Column(String)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship('UserModel', foreign_keys=[user_id])
