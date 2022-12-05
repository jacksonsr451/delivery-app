from .address_response import AddressResponse
from .contact_response import ContactResponse
from .profile_response import ProfileResponse


class UserReponse:
    id: str
    username: str
    profile: ProfileResponse
    contact: ContactResponse
    address: AddressResponse

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.username = data.username
        self.profile = ProfileResponse(data.profile)
        self.contact = ContactResponse(data.contact)
        self.address = AddressResponse(data.address)
