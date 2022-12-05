from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.contact_exception import ContactException
from src.models.contact_model import ContactModel
from src.requests.contact_request import ContactRequest
from src.response.contact_response import ContactResponse

from . import ContactRepositoryInterface


class ContactRepository(ContactRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, request: ContactRequest) -> NoneType:
        try:
            self.__session.add(ContactModel(request))
            self.__session.commit()
        except Exception:
            raise ContactException('Erro ao adcionar dados')

    def update(self, request: ContactRequest) -> NoneType:
        data = (
            self.__session.query(ContactModel)
            .filter(ContactModel.id == request.id)
            .one()
        )
        try:
            data.id = request.id
            data.phone = request.phone
            data.whattsapp = request.whattsapp
            data.telegram = request.telegram
            data.email = request.email
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
        _list: list[ContactResponse] = list()
        for value in self.__session.query(ContactModel).all():
            _list.append(ContactResponse(value))
        return _list

    def view(self, id: str) -> ContactResponse:
        return (
            self.__session.query(ContactModel)
            .filter(ContactModel.id == id)
            .first()
        )
