from abc import ABC, abstractmethod
from types import NoneType

from flask import Request

from src.response.user_response import UserReponse


class UserServicesInterface(ABC):
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
    def show(self) -> list[UserReponse]:
        """This method is required"""

    @abstractmethod
    def view(self, id: str) -> UserReponse:
        """This method is required"""
