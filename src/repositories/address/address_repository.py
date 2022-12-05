from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.address_exception import AddressException
from src.models.address_model import AddressModel
from src.requests.address_request import AddressRequest
from src.response.address_response import AddressResponse

from . import AddressRepositoryInterface


class AddressRepository(AddressRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, request: AddressRequest) -> NoneType:
        try:
            self.__session.add(AddressModel(request))
            self.__session.commit()
        except Exception:
            raise AddressException('Erro ao adcionar dados')

    def update(self, request: AddressRequest) -> NoneType:
        data = (
            self.__session.query(AddressModel)
            .filter(AddressModel.id == request.id)
            .one()
        )
        try:
            data.id = request.id
            data.country = request.country
            data.state = request.state
            data.neigborhod = request.neigborhod
            data.street = request.street
            data.number = request.number
            self.__session.commit()
        except Exception:
            raise AddressException('Erro ao atualizar dados')

    def delete(self, id: str) -> NoneType:
        try:
            self.__session.query(AddressModel).filter_by(id == id).delete()
            self.__session.commit()
        except Exception:
            raise AddressException('Erro ao deletar dados')

    def show(self) -> list[AddressResponse]:
        _list: list[AddressResponse] = list()
        for value in self.__session.query(AddressModel).all():
            _list.append(AddressResponse(value))
        return _list

    def view(self, id: str) -> AddressResponse:
        return (
            self.__session.query(AddressModel)
            .filter(AddressModel.id == id)
            .first()
        )
