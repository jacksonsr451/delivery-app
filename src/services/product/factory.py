from sqlalchemy.orm import Session

from src.repositories.product import ProductRepository, ProductRepositoryInterface

from .product_services_interface import ProductServicesInterface
from .product_services import ProductServices


def product_services_factory(session: Session) -> ProductServicesInterface:
    repository: ProductRepositoryInterface = ProductRepository(session=session)
    return ProductServices(repository=repository)
