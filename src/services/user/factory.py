from sqlalchemy.orm import Session

from src.repositories.user import UserRepository, UserRepositoryInterface

from . import UserServicesInterface
from .user_services import UserServices


def user_services_factory(session: Session) -> UserServicesInterface:
    repository: UserRepositoryInterface = UserRepository(session=session)
    return UserServices(repository=repository)
