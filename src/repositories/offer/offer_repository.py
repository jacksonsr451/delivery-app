from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.offer_exception import OfferException
from src.models.offer_model import OfferModel
from src.requests.offer_request import OfferRequest
from src.response.offer_response import OfferResponse

from . import CategoryRepositoryInterface


class OfferRepository(CategoryRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, offer: OfferRequest) -> NoneType:
        try:
            self.__session.add(OfferModel(offer))
            self.__session.commit()
        except Exception:
            raise OfferException('Erro ao adcionar dados')

    def update(self, offer: OfferRequest) -> NoneType:
        data = (
            self.__session.query(OfferModel)
            .filter(OfferModel.id == offer.id)
            .one()
        )
        try:
            data.id = offer.id
            data.slug = offer.slug
            data.category_id = offer.category.id
            data.product_id = offer.producty.id
            data.discount = offer.discount
            data.created_at = offer.created_at
            data.valid_until = offer.valid_until
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
