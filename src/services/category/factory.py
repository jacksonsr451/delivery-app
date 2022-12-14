from sqlalchemy.orm import Session

from src.repositories.category import (
    CategoryRepository,
    CategoryRepositoryInterface,
)

from .category_services import CategoryServices
from .category_services_interface import CategoryServicesInterface


def category_service_factory(session: Session) -> CategoryServicesInterface:
    repository: CategoryRepositoryInterface = CategoryRepository(
        session=session
    )
    return CategoryServices(repository=repository)
