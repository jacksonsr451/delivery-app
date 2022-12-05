from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.role_exception import RoleException
from src.models.role_model import RoleModel
from src.requests.role_request import RoleRequest
from src.response.role_response import RoleResponse

from .role_repository_interface import RoleRepositoryInterface


class RoleRepository(RoleRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, request: RoleRequest) -> NoneType:
        try:
            self.__session.add(RoleModel(request))
            self.__session.commit()
        except Exception:
            raise RoleException('Erro ao adcionar dados')

    def update(self, request: RoleRequest) -> NoneType:
        data = (
            self.__session.query(RoleModel)
            .filter(RoleModel.id == request.id)
            .one()
        )
        try:
            data.id = request.id
            data.role = request.role
            self.__session.commit()
        except Exception:
            raise RoleException('Erro ao atualizar dados')

    def delete(self, id: str) -> NoneType:
        try:
            self.__session.query(RoleModel).filter_by(id == id).delete()
            self.__session.commit()
        except Exception:
            raise RoleException('Erro ao deletar dados')

    def show(self) -> list[RoleResponse]:
        _list: list[RoleResponse] = list()
        for value in self.__session.query(RoleModel).all():
            _list.append(RoleResponse(value))
        return _list

    def view(self, id: str) -> RoleResponse:
        return (
            self.__session.query(RoleModel).filter(RoleModel.id == id).first()
        )
