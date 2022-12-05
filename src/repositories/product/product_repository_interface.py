from abc import ABC, abstractmethod
from types import NoneType

from src.requests.product_request import ProductRequest
from src.response.product_response import ProductResponse


class ProductRepositoryInterface(ABC):
    @abstractmethod
    def create(self, request: ProductRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def update(self, request: ProductRequest) -> NoneType:
        """This method is required"""

    @abstractmethod
    def delete(self, id: str) -> NoneType:
        """This method is required"""

    @abstractmethod
    def show(self) -> list[ProductResponse]:
        """This method is required"""

    @abstractmethod
    def view(self) -> ProductResponse:
        """This method is required"""
