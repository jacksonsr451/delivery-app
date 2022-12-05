from abc import ABC, abstractmethod
from types import NoneType

from src.requests.offer_request import OfferRequest
from src.response.offer_response import OfferResponse


class OfferRepositoryInterface(ABC):
    @abstractmethod
    def create(self, request: OfferRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, request: OfferRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""

    @abstractmethod
    def show(self) -> list[OfferResponse]:
        """This method is required"""

    @abstractmethod
    def view(self) -> OfferResponse:
        """This method is required"""
