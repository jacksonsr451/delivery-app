from sqlalchemy import Column, String, Boolean

from src.core.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    username = Column(String)
    password = Column(String)
    status = Column(Boolean)

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.username = data.username
        self.password = data.password
        self.status = data.status
