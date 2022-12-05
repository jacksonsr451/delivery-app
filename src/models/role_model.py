from sqlalchemy import Column, String

from src.core.database import Base


class RoleModel(Base):
    __tablename__ = 'roles'

    id = Column(String, primary_key=True)
    role = Column(String)
