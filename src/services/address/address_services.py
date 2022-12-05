from types import NoneType

from flask import Request

from src.repositories.address import AddressRepositoryInterface
from src.requests.address_request import AddressRequest
from src.response.address_response import AddressResponse

from .address_services_interface import AddressServicesInterface


class AddressServices(AddressServicesInterface):
    __repository: AddressRepositoryInterface

    def __init__(self, repository: AddressRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, request: Request) -> NoneType:
        self.__repository.create(request=AddressRequest(request))

    def update(self, request: Request) -> NoneType:
        self.__repository.update(request=AddressRequest(request))

    def delete(self, id: str) -> NoneType:
        self.__repository.delete(id=id)

    def show(self) -> list[AddressResponse]:
        return self.__repository.show()

    def view(self, id: str) -> AddressResponse:
        return self.__repository.view(id=id)
