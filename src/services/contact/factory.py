from sqlalchemy.orm import Session

from src.repositories.contact import (
    ContactRepository,
    ContactRepositoryInterface,
)

from .contact_services import ContactServices
from .contact_services_interface import ContactServicesInterface


def contact_services_factory(session: Session) -> ContactServicesInterface:
    repository: ContactRepositoryInterface = ContactRepository(session=session)
    return ContactServices(repository=repository)
