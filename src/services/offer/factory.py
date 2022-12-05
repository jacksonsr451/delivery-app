from sqlalchemy.orm import Session

from src.repositories.offer.offer_repository import OfferRepository
from src.repositories.offer.offer_repository_interface import (
    OfferRepositoryInterface,
)

from . import OfferServicesInterface
from .offer_services import OfferServices


def offer_services_factory(session: Session) -> OfferServicesInterface:
    repository: OfferRepositoryInterface = OfferRepository(session=session)
    return OfferServices(repository=repository)
