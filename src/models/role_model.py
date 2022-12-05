from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Base


class RoleModel(Base):
    __tablename__ = 'roles'

    id = Column(String, primary_key=True)
    role = Column(String)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship('UserModel', foreign_keys=[user_id])
