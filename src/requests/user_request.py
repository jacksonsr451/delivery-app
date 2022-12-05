from flask import Request

from .address_request import AddressRequest
from .contact_request import ContactRequest
from .profile_request import ProfileRequest
from .role_request import RoleRequest


class UserRequest:
    id: str
    username: str
    password: str
    role: RoleRequest
    profile: ProfileRequest
    contact: ContactRequest
    address: AddressRequest

    def __init__(self, schema: Request) -> None:
        self.id = schema.form['id']
        self.username = schema.form['username']
        self.password = schema.form['password']
        self.role = RoleRequest(schema.form['role'])
        self.profile = ProfileRequest(schema.form['profile'])
        self.contact = ContactRequest(schema.form['contact'])
        self.address = AddressRequest(schema.form['address'])
