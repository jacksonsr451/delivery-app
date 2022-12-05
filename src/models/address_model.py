from uuid import uuid4
from sqlalchemy import Column, String

from src.core.database import Base
from src.requests.address_request import AddressRequest


class AddressModel(Base):
    __tablename__ = 'addresses'

    id = Column(String, primary_key=True)
    country = Column(String)
    state = Column(String)
    neigborhod = Column(String)
    street = Column(String)
    number = Column(String)

    def __init__(self, request: AddressRequest) -> None:
        self.id = request.id if request.id else uuid4()
        self.country = request.country
        self.state = request.state
        self.neigborhod = request.neigborhod
        self.street = request.street
        self.number = request.number
