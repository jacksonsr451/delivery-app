from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.category_exception import CategoryException
from src.models.category_model import CategoryModel
from src.requests.category_request import CategoryRequest
from src.response.category_response import CategoryResponse

from . import CategoryRepositoryInterface


class CategoryRepository(CategoryRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, address: CategoryRequest) -> NoneType:
        try:
            self.__session.add(CategoryModel(address))
            self.__session.commit()
        except Exception:
            raise CategoryException('Erro ao adcionar dados')

    def update(self, address: CategoryRequest) -> NoneType:
        data = (
            self.__session.query(CategoryModel)
            .filter(CategoryModel.id == address.id)
            .one()
        )
        try:
            data.id = address.id
            data.slug = address.slug
            data.title = address.title
            data.description = address.descripion
            self.__session.commit()
        except Exception:
            raise CategoryException('Erro ao atualizar dados')

    def delete(self, id: str) -> NoneType:
        try:
            self.__session.query(CategoryModel).filter_by(id == id).delete()
            self.__session.commit()
        except Exception:
            raise CategoryException('Erro ao deletar dados')

    def show(self) -> list[CategoryResponse]:
        addresses_list: list[CategoryResponse] = list()
        for address in self.__session.query(CategoryModel).all():
            addresses_list.append(CategoryResponse(address))
        return addresses_list

    def view(self, id: str) -> CategoryResponse:
        return (
            self.__session.query(CategoryModel)
            .filter(CategoryModel.id == id)
            .first()
        )
