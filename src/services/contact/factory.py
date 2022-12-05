from sqlalchemy.orm import Session

from src.repositories.contact import ContactRepository, ContactRepositoryInterface

from . import ContactServicesInterface
from .contact_services import ContactServices


def contact_services_factory(session: Session) -> ContactServicesInterface:
    repository: ContactRepositoryInterface = ContactRepository(session=session)
    return ContactServices(repository=repository)
