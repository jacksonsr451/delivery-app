from sqlalchemy.orm import Session

from src.repositories.offer import OfferRepository, OfferRepositoryInterface

from . import OfferServicesInterface
from .offer_services import OfferServices


def offer_services_factory(session: Session) -> OfferServicesInterface:
    repository: OfferRepositoryInterface = OfferRepository(session=session)
    return OfferServices(repository=repository)
