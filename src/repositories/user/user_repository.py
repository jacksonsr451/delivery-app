from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.user_exception import UserException
from src.models.user_model import UserModel
from src.requests.user_request import UserRequest
from src.response.user_response import UserReponse

from .user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, request: UserRequest) -> NoneType:
        try:
            self.__session.add(UserModel(request))
            self.__session.commit()
        except Exception:
            raise UserException('Erro ao adcionar dados')

    def update(self, request: UserRequest) -> NoneType:
        data = (
            self.__session.query(UserModel)
            .filter(UserModel.id == request.id)
            .one()
        )
        try:
            data.id = request.id
            data.username = request.username
            data.profile_id = request.profile.id
            data.contact_id = request.contact.id
            data.address_id = request.address.id
            self.__session.commit()
        except Exception:
            raise UserException('Erro ao atualizar dados')

    def delete(self, id: str) -> NoneType:
        try:
            self.__session.query(UserModel).filter_by(id == id).delete()
            self.__session.commit()
        except Exception:
            raise UserException('Erro ao deletar dados')

    def show(self) -> list[UserReponse]:
        _list: list[UserReponse] = list()
        for value in self.__session.query(UserModel).all():
            _list.append(UserReponse(value))
        return _list

    def view(self, id: str) -> UserReponse:
        return (
            self.__session.query(UserModel).filter(UserModel.id == id).first()
        )
