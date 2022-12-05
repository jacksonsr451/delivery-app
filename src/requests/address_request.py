from typing import Any


class AddressRequest:
    id: str
    country: str
    state: str
    neigborhod: str
    street: str
    number: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.get('id')
        self.country = schema.get('country')
        self.state = schema.get('state')
        self.neigborhod = schema.get('neigborhod')
        self.street = schema.get('street')
        self.number = schema.get('number')
