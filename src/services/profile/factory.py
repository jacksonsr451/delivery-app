from sqlalchemy.orm import Session

from src.repositories.profile import (
    ProfileRepository,
    ProfileRepositoryInterface,
)

from .profile_services import ProfileServices
from .profile_services_interface import ProfileServicesInterface


def profile_services_factory(session: Session) -> ProfileServicesInterface:
    repository: ProfileRepositoryInterface = ProfileRepository(session=session)
    return ProfileServices(repository=repository)
