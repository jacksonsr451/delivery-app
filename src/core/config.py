from typing import Any

from src.services.address import address_service_factory

from .database import session

config: dict[str, Any] = {
    'services': {'AddressServices': address_service_factory(session=session)}
}
