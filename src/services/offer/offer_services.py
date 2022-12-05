from types import NoneType

from flask import Request

from src.repositories.offer import OfferRepositoryInterface
from src.requests.offer_request import OfferRequest
from src.response.offer_response import OfferResponse

from .offer_services_interface import OfferServicesInterface


class OfferServices(OfferServicesInterface):
    __repository: OfferRepositoryInterface

    def __init__(self, repository: OfferRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, request: Request) -> NoneType:
        self.__repository.create(request=OfferRequest(request))

    def update(self, request: Request) -> NoneType:
        self.__repository.update(request=OfferRequest(request))

    def delete(self, id: str) -> NoneType:
        self.__repository.delete(id=id)

    def show(self) -> list[OfferResponse]:
        return self.__repository.show()

    def view(self, id: str) -> OfferResponse:
        return self.__repository.view(id=id)
