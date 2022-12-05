from types import NoneType

from flask import Request

from src.repositories.role import RoleRepositoryInterface
from src.requests.role_request import RoleRequest
from src.response.role_response import RoleResponse

from . import RoleServicesInterface


class RoleServices(RoleServicesInterface):
    __repository: RoleRepositoryInterface

    def __init__(self, repository: RoleRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, request: Request) -> NoneType:
        self.__repository.create(request=RoleRequest(request))

    def update(self, request: Request) -> NoneType:
        self.__repository.update(request=RoleRequest(request))

    def delete(self, id: str) -> NoneType:
        self.__repository.delete(id=id)

    def show(self) -> list[RoleResponse]:
        return self.__repository.show()

    def view(self, id: str) -> RoleResponse:
        return self.__repository.view(id=id)
