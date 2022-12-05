from abc import ABC, abstractmethod
from types import NoneType

from src.requests.role_request import RoleRequest
from src.response.role_response import RoleResponse


class RoleRepositoryInterface(ABC):
    @abstractmethod
    def create(self, request: RoleRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, request: RoleRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""

    @abstractmethod
    def show(self) -> list[RoleResponse]:
        """This method is required"""

    @abstractmethod
    def view(self) -> RoleResponse:
        """This method is required"""
