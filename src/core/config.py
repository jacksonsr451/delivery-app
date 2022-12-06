import os
from dotenv import load_dotenv
from typing import Any

from src.services.address import address_service_factory
from src.services.auth.factory import auth_services_factory
from src.services.category import category_service_factory
from src.services.contact import contact_services_factory
from src.services.offer import offer_services_factory
from src.services.product import product_services_factory
from src.services.profile import profile_services_factory
from src.services.role import role_services_factory
from src.services.user import user_services_factory

from .database import session

load_dotenv()

config: dict[str, Any] = {
    'secret_key': os.getenv('APP_SECRET_KEY'),
    'services': {
        'AddressServices': address_service_factory(session=session),
        'CategoryServices': category_service_factory(session=session),
        'ContactServices': contact_services_factory(session=session),
        'OfferServices': offer_services_factory(session=session),
        'ProductServices': product_services_factory(session=session),
        'ProfileServices': profile_services_factory(session=session),
        'RoleServices': role_services_factory(session=session),
        'UserServices': user_services_factory(session=session),
        'AuthServices': auth_services_factory(session=session),
    }
}
