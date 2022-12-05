from abc import ABC, abstractmethod
from types import NoneType

from flask import Request

from src.response.profile_response import ProfileResponse


class ProfileServicesInterface(ABC):
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
    def show(self) -> list[ProfileResponse]:
        """This method is required"""

    @abstractmethod
    def view(self, id: str) -> ProfileResponse:
        """This method is required"""
