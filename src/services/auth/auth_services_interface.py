from abc import ABC, abstractmethod
from types import NoneType

from flask import Request

from src.response.auth_response import AuthReponse


class AuthServicesInterface(ABC):
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
    def login(self, request: Request) -> AuthReponse:
        """This method is required"""
