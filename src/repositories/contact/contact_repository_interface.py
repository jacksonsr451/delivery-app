from abc import ABC, abstractmethod
from types import NoneType

from src.requests.contact_request import ContactRequest
from src.response.contact_response import ContactResponse


class ContactRepositoryInterface(ABC):
    @abstractmethod
    def create(self, request: ContactRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, request: ContactRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""

    @abstractmethod
    def show(self) -> list[ContactResponse]:
        """This method is required"""

    @abstractmethod
    def view(self) -> ContactResponse:
        """This method is required"""
