from abc import ABC, abstractmethod
from types import NoneType

from flask import Request

from src.response.role_response import RoleResponse


class RoleServicesInterface(ABC):
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
    def show(self) -> list[RoleResponse]:
        """This method is required"""

    @abstractmethod
    def view(self, id: str) -> RoleResponse:
        """This method is required"""
