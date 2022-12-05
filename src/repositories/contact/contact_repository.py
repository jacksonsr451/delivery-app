from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.contact_exception import ContactException
from src.models.contact_model import ContactModel
from src.requests.contact_request import ContactRequest
from src.response.contact_response import ContactResponse

from . import CategoryRepositoryInterface


class ContactRepository(CategoryRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, address: ContactRequest) -> NoneType:
        try:
            self.__session.add(ContactModel(address))
            self.__session.commit()
        except Exception:
            raise ContactException('Erro ao adcionar dados')

    def update(self, address: ContactRequest) -> NoneType:
        data = (
            self.__session.query(ContactModel)
            .filter(ContactModel.id == address.id)
            .one()
        )
        try:
            data.id = address.id
            data.phone = address.phone
            data.whattsapp = address.whattsapp
            data.telegram = address.telegram
            data.email = address.email
            self.__session.commit()
        except Exception:
            raise ContactException('Erro ao atualizar dados')

    def delete(self, id: str) -> NoneType:
        try:
            self.__session.query(ContactModel).filter_by(id == id).delete()
            self.__session.commit()
        except Exception:
            raise ContactException('Erro ao deletar dados')

    def show(self) -> list[ContactResponse]:
        addresses_list: list[ContactResponse] = list()
        for address in self.__session.query(ContactModel).all():
            addresses_list.append(ContactResponse(address))
        return addresses_list

    def view(self, id: str) -> ContactResponse:
        return (
            self.__session.query(ContactModel)
            .filter(ContactModel.id == id)
            .first()
        )
