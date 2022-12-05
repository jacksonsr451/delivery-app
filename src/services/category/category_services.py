from types import NoneType

from flask import Request

from src.repositories.category import CategoryRepositoryInterface
from src.requests.category_request import CategoryRequest
from src.response.category_response import CategoryResponse

from .category_services_interface import CategoryServicesInterface


class CategoryServices(CategoryServicesInterface):
    __repository: CategoryRepositoryInterface

    def __init__(self, repository: CategoryRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, request: Request) -> NoneType:
        self.__repository.create(request=CategoryRequest(request))

    def update(self, request: Request) -> NoneType:
        self.__repository.update(request=CategoryRequest(request))

    def delete(self, id: str) -> NoneType:
        self.__repository.delete(id=id)

    def show(self) -> list[CategoryResponse]:
        return self.__repository.show()

    def view(self, id: str) -> CategoryResponse:
        return self.__repository.view(id=id)
