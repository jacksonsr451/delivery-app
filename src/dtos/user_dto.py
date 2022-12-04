from typing import Any


UserDTO: dict[str, Any] = {
    'id': '',
    'username': '',
    'password': '',
    'role_id': '',
    'role': {
        'id': '',
        'role': ''
    },
    'profile_id': '',
    'profile': {
        'id': '',
        'name': '',
    },
    'contact_id': '',
    'contact': {
        'id': '',
        'phone': '',
        'whattsapp': '',
        'telegran': '',
        'email': ''
    },
    'address_id': '',
    'address': {
        'id': '',
        'country': '',
        'state': '',
        'neigborhod': '',
        'street': '',
        'number': ''
    }
}
