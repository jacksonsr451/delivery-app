from abc import ABC, abstractmethod
from types import NoneType

from flask import Request

from src.response.offer_response import OfferResponse


class OfferServicesInterface(ABC):
    @abstractmethod
    def create(self, request: Request) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, request: Request) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""

    @abstractmethod
    def show(self) -> list[OfferResponse]:
        """This method is required"""

    @abstractmethod
    def view(self, id: str) -> OfferResponse:
        """This method is required"""
