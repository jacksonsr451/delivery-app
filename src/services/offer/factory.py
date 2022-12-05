from sqlalchemy.orm import Session

from src.repositories.offer import OfferRepository, OfferRepositoryInterface

from .offer_services import OfferServices
from .offer_services_interface import OfferServicesInterface


def offer_services_factory(session: Session) -> OfferServicesInterface:
    repository: OfferRepositoryInterface = OfferRepository(session=session)
    return OfferServices(repository=repository)
