from sqlalchemy.orm import Session

from src.repositories.auth import AuthRepository, AuthRepositoryInterface

from .auth_services import AuthServices
from .auth_services_interface import AuthServicesInterface


def auth_services_factory(session: Session) -> AuthServicesInterface:
    repository: AuthRepositoryInterface = AuthRepository(session=session)
    return AuthServices(repository=repository)
