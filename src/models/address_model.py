from sqlalchemy import Column, String

from src.core.database import Base


class AddressModel(Base):
    __tablename__ = 'addresses'

    id = Column(String, primary_key=True)
    country = Column(String)
    state = Column(String)
    neigborhod = Column(String)
    street = Column(String)
    number = Column(String)
