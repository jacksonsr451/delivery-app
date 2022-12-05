from abc import ABC, abstractmethod
from types import NoneType

from src.requests.address_request import AddressRequest
from src.response.address_response import AddressResponse


class AddressRepositoryInterface(ABC):
    @abstractmethod
    def create(self, address: AddressRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, address: AddressRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""

    @abstractmethod
    def show(self) -> list[AddressResponse]:
        """This method is required"""

    @abstractmethod
    def view(self) -> AddressResponse:
        """This method is required"""
