from sqlalchemy.orm import Session

from src.repositories.role import RoleRepository, RoleRepositoryInterface

from .role_services_interface import RoleServicesInterface
from .role_services import RoleServices


def role_services_factory(session: Session) -> RoleServicesInterface:
    repository: RoleRepositoryInterface = RoleRepository(session=session)
    return RoleServices(repository=repository)
