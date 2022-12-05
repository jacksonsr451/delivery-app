from sqlalchemy.orm import Session

from src.repositories.category.category_repository import CategoryRepository
from src.repositories.category.category_repository_interface import (
    CategoryRepositoryInterface,
)

from . import CategoryServicesInterface
from .category_services import CategoryServices


def category_service_factory(session: Session) -> CategoryServicesInterface:
    repository: CategoryRepositoryInterface = CategoryRepository(session=session)
    return CategoryServices(repository=repository)
