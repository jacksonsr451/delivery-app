from types import NoneType

from flask import Request

from src.repositories.contact import ContactRepositoryInterface
from src.requests.contact_request import ContactRequest
from src.response.contact_response import ContactResponse

from . import ContactServicesInterface


class ContactServices(ContactServicesInterface):
    __repository: ContactRepositoryInterface

    def __init__(self, repository: ContactRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, request: Request) -> NoneType:
        self.__repository.create(request=ContactRequest(request))

    def update(self, request: Request) -> NoneType:
        self.__repository.update(request=ContactRequest(request))

    def delete(self, id: str) -> NoneType:
        self.__repository.delete(id=id)

    def show(self) -> list[ContactResponse]:
        return self.__repository.show()

    def view(self, id: str) -> ContactResponse:
        return self.__repository.view(id=id)
