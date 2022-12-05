from typing import Any

from src.services.address import address_service_factory
from src.services.category import category_service_factory
from src.services.contact import contact_services_factory

from .database import session

config: dict[str, Any] = {
    'services': {
        'AddressServices': address_service_factory(session=session),
        'CategoryServices': category_service_factory(session=session),
        'ContactServices': contact_services_factory(session=session)
    }
}
