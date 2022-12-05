from abc import ABC, abstractmethod
from types import NoneType

from flask import Request

from src.response.product_response import ProductResponse


class ProductServicesInterface(ABC):
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
    def show(self) -> list[ProductResponse]:
        """This method is required"""

    @abstractmethod
    def view(self, id: str) -> ProductResponse:
        """This method is required"""
