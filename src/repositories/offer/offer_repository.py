from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.offer_exception import OfferException
from src.models.offer_model import OfferModel
from src.requests.offer_request import OfferRequest
from src.response.offer_response import OfferResponse

from .offer_repository_interface import OfferRepositoryInterface


class OfferRepository(OfferRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, request: OfferRequest) -> NoneType:
        try:
            self.__session.add(OfferModel(request))
            self.__session.commit()
        except Exception:
            raise OfferException('Erro ao adcionar dados')

    def update(self, request: OfferRequest) -> NoneType:
        data = (
            self.__session.query(OfferModel)
            .filter(OfferModel.id == request.id)
            .one()
        )
        try:
            data.id = request.id
            data.slug = request.slug
            data.category_id = request.category.id
            data.product_id = request.producty.id
            data.discount = request.discount
            data.created_at = request.created_at
            data.valid_until = request.valid_until
            self.__session.commit()
        except Exception:
            raise OfferException('Erro ao atualizar dados')

    def delete(self, id: str) -> NoneType:
        try:
            self.__session.query(OfferModel).filter_by(id == id).delete()
            self.__session.commit()
        except Exception:
            raise OfferException('Erro ao deletar dados')

    def show(self) -> list[OfferResponse]:
        _list: list[OfferResponse] = list()
        for value in self.__session.query(OfferModel).all():
            _list.append(OfferResponse(value))
        return _list

    def view(self, id: str) -> OfferResponse:
        return (
            self.__session.query(OfferModel)
            .filter(OfferModel.id == id)
            .first()
        )
