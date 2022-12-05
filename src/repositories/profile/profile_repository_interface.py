from abc import ABC, abstractmethod
from types import NoneType

from src.requests.profile_request import ProfileRequest
from src.response.profile_response import ProfileResponse


class ProfileRepositoryInterface(ABC):
    @abstractmethod
    def create(self, request: ProfileRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, request: ProfileRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""

    @abstractmethod
    def show(self) -> list[ProfileResponse]:
        """This method is required"""

    @abstractmethod
    def view(self) -> ProfileResponse:
        """This method is required"""
