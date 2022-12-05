from typing import Any

from .role_request import RoleRequest
from .address_request import AddressRequest
from .contact_request import ContactRequest

from .profile_request import ProfileRequest

class UserRequest:
    id: str
    username: str
    password: str
    role: RoleRequest
    profile: ProfileRequest
    contact: ContactRequest
    address: AddressRequest

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.get('id')
        self.username = schema.get('username')
        self.password = schema.get('password')
        self.role = RoleRequest(schema.get('role'))
        self.profile = ProfileRequest(schema.get('profile'))
        self.contact = ContactRequest(schema.get('contact'))
        self.address = AddressRequest(schema.get('address'))
