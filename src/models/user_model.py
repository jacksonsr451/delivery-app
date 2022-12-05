from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.core.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    username = Column(String)
    password = Column(String)
    role_id = Column(String, ForeignKey('roles.id'))
    role = relationship('RoleModel', foreign_keys=[role_id])
    profile_id = Column(String, ForeignKey('profiles.id'))
    profile = relationship('ProfileModel', foreign_keys=[profile_id])
    contact_id = Column(String, ForeignKey('contacts.id'))
    contact = relationship('ContactModel', foreign_keys=[contact_id])
    address_id = Column(String, ForeignKey('addresses.id'))
    address = relationship('AddressModel', foreign_keys=[address_id])
