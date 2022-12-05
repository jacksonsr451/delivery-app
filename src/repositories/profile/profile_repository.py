from types import NoneType

from sqlalchemy.orm import Session

from src.exceptions.profile_exception import ProfileException
from src.models.profile_model import ProfileModel
from src.requests.profile_request import ProfileRequest
from src.response.profile_response import ProfileResponse

from . import ProfileRepositoryInterface


class ProfileRepository(ProfileRepositoryInterface):
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, request: ProfileRequest) -> NoneType:
        try:
            self.__session.add(ProfileModel(request))
            self.__session.commit()
        except Exception:
            raise ProfileException('Erro ao adcionar dados')

    def update(self, request: ProfileRequest) -> NoneType:
        data = (
            self.__session.query(ProfileModel)
            .filter(ProfileModel.id == request.id)
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
            raise ProfileException('Erro ao atualizar dados')

    def delete(self, id: str) -> NoneType:
        try:
            self.__session.query(ProfileModel).filter_by(id == id).delete()
            self.__session.commit()
        except Exception:
            raise ProfileException('Erro ao deletar dados')

    def show(self) -> list[ProfileResponse]:
        _list: list[ProfileResponse] = list()
        for value in self.__session.query(ProfileModel).all():
            _list.append(ProfileResponse(value))
        return _list

    def view(self, id: str) -> ProfileResponse:
        return (
            self.__session.query(ProfileModel)
            .filter(ProfileModel.id == id)
            .first()
        )
