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

    def create(self, address: AddressRequest) -> NoneType:
        try:
            self.__session.add(AddressModel(address))
            self.__session.commit()
        except Exception:
            raise AddressException('Erro ao adcionar dados')

    def update(self, address: AddressRequest) -> NoneType:
        data = (
            self.__session.query(AddressModel)
            .filter(AddressModel.id == address.id)
            .one()
        )
        try:
            data.id = address.id
            data.country = address.country
            data.state = address.state
            data.neigborhod = address.neigborhod
            data.street = address.street
            data.number = address.number
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
        addresses_list: list[AddressResponse] = list()
        for address in self.__session.query(AddressModel).all():
            addresses_list.append(AddressResponse(address))
        return addresses_list

    def view(self, id: str) -> AddressResponse:
        return (
            self.__session.query(AddressModel)
            .filter(AddressModel.id == id)
            .first()
        )
