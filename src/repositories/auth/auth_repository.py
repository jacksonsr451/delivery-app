from bcrypt import checkpw
from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.user_exception import UserException
from src.models.user_model import UserModel
from src.requests.auth_request import AuthRequest
from src.response.auth_response import AuthReponse

from .auth_repository_interface import AuthRepositoryInterface


class AuthRepository(AuthRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, request: AuthRequest) -> NoneType:
        try:
            print(self.__session)
            self.__session.add(UserModel(request))
            self.__session.commit()
        except Exception as error:
            raise UserException(f'Erro ao adcionar dados: {error}')

    def update(self, request: AuthRequest) -> NoneType:
        data = (
            self.__session.query(UserModel)
            .filter(UserModel.id == request.id)
            .one()
        )
        try:
            data.id = request.id
            data.username = request.username
            self.__session.commit()
        except Exception:
            raise UserException('Erro ao atualizar dados')

    def delete(self, id: str) -> NoneType:
        try:
            self.__session.query(UserModel).filter_by(id == id).delete()
            self.__session.commit()
        except Exception:
            raise UserException('Erro ao deletar dados')

    def login(self, username: str, password: str) -> AuthReponse:
        try:
            data = self.__session.query(UserModel).filter(UserModel.username == username).one()
            if checkpw(password.encode('utf8'), data.password.encode('utf8')):
                return AuthReponse(data)
            else: raise UserException('Não há usuario cadastrado com este username!')
        except Exception as error:
            raise UserException('{}'.format(error))
