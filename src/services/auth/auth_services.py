from types import NoneType

from flask import Request

from src.repositories.auth import AuthRepositoryInterface
from src.requests.auth_request import AuthRequest
from src.response.auth_response import AuthReponse

from .auth_services_interface import AuthServicesInterface


class AuthServices(AuthServicesInterface):
    __repository: AuthRepositoryInterface

    def __init__(self, repository: AuthRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, request: Request) -> NoneType:
        self.__repository.create(request=AuthRequest(request))

    def update(self, request: Request) -> NoneType:
        self.__repository.update(request=AuthRequest(request))

    def delete(self, id: str) -> NoneType:
        self.__repository.delete(id=id)

    def login(self, request: Request) -> AuthReponse:
        return self.__repository.login(
            username=request.form['username'],
            password=request.form['password'],
        )
