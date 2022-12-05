from sqlalchemy.orm import Session

from src.repositories.category import CategoryRepository, CategoryRepositoryInterface


from . import CategoryServicesInterface
from .category_services import CategoryServices


def category_service_factory(session: Session) -> CategoryServicesInterface:
    repository: CategoryRepositoryInterface = CategoryRepository(session=session)
    return CategoryServices(repository=repository)
