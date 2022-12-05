from abc import ABC, abstractmethod
from types import NoneType

from src.requests.user_request import UserRequest
from src.response.user_response import UserReponse


class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, request: UserRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, request: UserRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""

    @abstractmethod
    def show(self) -> list[UserReponse]:
        """This method is required"""

    @abstractmethod
    def view(self) -> UserReponse:
        """This method is required"""
