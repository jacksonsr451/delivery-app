from abc import ABC, abstractmethod
from types import NoneType

from flask import Request

from src.response.address_response import AddressResponse


class AddressServicesInterface(ABC):
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
    def show(self) -> list[AddressResponse]:
        """This method is required"""

    @abstractmethod
    def view(self, id: str) -> AddressResponse:
        """This method is required"""
