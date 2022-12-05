from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.product_exception import ProductException
from src.models.product_model import ProductModel
from src.requests.product_request import ProductRequest
from src.response.product_response import ProductResponse

from .product_repository_interface import ProductRepositoryInterface


class ProductRepository(ProductRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, request: ProductRequest) -> NoneType:
        try:
            self.__session.add(ProductModel(request))
            self.__session.commit()
        except Exception:
            raise ProductException('Erro ao adcionar dados')

    def update(self, request: ProductRequest) -> NoneType:
        data = (
            self.__session.query(ProductModel)
            .filter(ProductModel.id == request.id)
            .one()
        )
        try:
            data.id = request.id
            data.slug = request.slug
            data.price = request.price
            data.resume = request.resume
            data.description = request.description
            self.__session.commit()
        except Exception:
            raise ProductException('Erro ao atualizar dados')

    def delete(self, id: str) -> NoneType:
        try:
            self.__session.query(ProductModel).filter_by(id == id).delete()
            self.__session.commit()
        except Exception:
            raise ProductException('Erro ao deletar dados')

    def show(self) -> list[ProductResponse]:
        _list: list[ProductResponse] = list()
        for value in self.__session.query(ProductModel).all():
            _list.append(ProductResponse(value))
        return _list

    def view(self, id: str) -> ProductResponse:
        return (
            self.__session.query(ProductModel)
            .filter(ProductModel.id == id)
            .first()
        )
