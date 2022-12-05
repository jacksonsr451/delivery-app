from types import NoneType

from flask import Request

from src.repositories.product import ProductRepositoryInterface
from src.requests.product_request import ProductRequest
from src.response.profile_response import ProfileResponse

from .profile_services_interface import ProfileServicesInterface


class ProfileServices(ProfileServicesInterface):
    __repository: ProductRepositoryInterface

    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, request: Request) -> NoneType:
        self.__repository.create(request=ProductRequest(request))

    def update(self, request: Request) -> NoneType:
        self.__repository.update(request=ProductRequest(request))

    def delete(self, id: str) -> NoneType:
        self.__repository.delete(id=id)

    def show(self) -> list[ProfileResponse]:
        return self.__repository.show()

    def view(self, id: str) -> ProfileResponse:
        return self.__repository.view(id=id)
