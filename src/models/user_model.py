from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from src.core.database import Base
from src.models.address_model import AddressModel
from src.models.contact_model import ContactModel
from src.models.profile_model import ProfileModel
from src.models.role_model import RoleModel


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    username = Column(String)
    password = Column(String)
    role = relationship('RoleModel', foreign_keys=[RoleModel.id])
    profile = relationship('ProfileModel', foreign_keys=[ProfileModel.id])
    contact = relationship('ContactModel', foreign_keys=[ContactModel.id])
    address = relationship('AddressModel', foreign_keys=[AddressModel.id])
    status = Column(Boolean)

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.username = data.username
        self.password = data.password
        self.status = data.status
