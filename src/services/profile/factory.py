from sqlalchemy.orm import Session

from src.repositories.profile import ProfileRepository, ProfileRepositoryInterface

from . import ProfileServicesInterface
from .profile_services import ProfileServices


def profile_services_factory(session: Session) -> ProfileServicesInterface:
    repository: ProfileRepositoryInterface = ProfileRepository(session=session)
    return ProfileServices(repository=repository)
