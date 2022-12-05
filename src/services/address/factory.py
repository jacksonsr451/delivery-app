from sqlalchemy.orm import Session

from src.repositories.address import AddressRepository, AddressRepositoryInterface

from .address_services_interface import AddressServicesInterface
from .address_services import AddressServices


def address_service_factory(session: Session) -> AddressServicesInterface:
    repository: AddressRepositoryInterface = AddressRepository(session=session)
    return AddressServices(repository=repository)
