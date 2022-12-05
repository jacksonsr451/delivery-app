from sqlalchemy.orm import Session

from src.repositories.address.address_repository import AddressRepository
from src.repositories.address.address_repository_interface import (
    AddressRepositoryInterface,
)

from . import AddressServicesInterface
from .address_services import AddressServices


def address_service_factory(session: Session) -> AddressServicesInterface:
    repository: AddressRepositoryInterface = AddressRepository(session=session)
    return AddressServices(repository=repository)
