from types import NoneType

from flask import Request

from src.repositories.user import UserRepositoryInterface
from src.requests.user_request import UserRequest
from src.response.user_response import UserReponse

from . import UserServicesInterface


class UserServices(UserServicesInterface):
    __repository: UserRepositoryInterface

    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, request: Request) -> NoneType:
        self.__repository.create(request=UserRequest(request))

    def update(self, request: Request) -> NoneType:
        self.__repository.update(request=UserRequest(request))

    def delete(self, id: str) -> NoneType:
        self.__repository.delete(id=id)

    def show(self) -> list[UserReponse]:
        return self.__repository.show()

    def view(self, id: str) -> UserReponse:
        return self.__repository.view(id=id)
