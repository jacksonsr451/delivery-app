from sqlalchemy.orm import Session

from src.repositories.user import UserRepository, UserRepositoryInterface

from .user_services import UserServices
from .user_services_interface import UserServicesInterface


def user_services_factory(session: Session) -> UserServicesInterface:
    repository: UserRepositoryInterface = UserRepository(session=session)
    return UserServices(repository=repository)
