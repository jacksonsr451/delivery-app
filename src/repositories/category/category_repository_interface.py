from abc import ABC, abstractmethod
from types import NoneType

from src.requests.category_request import CategoryRequest
from src.response.category_response import CategoryResponse


class CategoryRepositoryInterface(ABC):
    @abstractmethod
    def create(self, address: CategoryRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, address: CategoryRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""

    @abstractmethod
    def show(self) -> list[CategoryResponse]:
        """This method is required"""

    @abstractmethod
    def view(self) -> CategoryResponse:
        """This method is required"""
