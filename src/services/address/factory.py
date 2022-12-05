from sqlalchemy.orm import Session

from src.repositories.address import (
    AddressRepository,
    AddressRepositoryInterface,
)

from .address_services import AddressServices
from .address_services_interface import AddressServicesInterface


def address_service_factory(session: Session) -> AddressServicesInterface:
    repository: AddressRepositoryInterface = AddressRepository(session=session)
    return AddressServices(repository=repository)
