from abc import ABC, abstractmethod
from types import NoneType

from src.requests.auth_request import AuthRequest
from src.response.auth_response import AuthReponse


class AuthRepositoryInterface(ABC):
    @abstractmethod
    def create(self, request: AuthRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, request: AuthRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""
