from typing import Any


class ContactRequest:
    id: str
    phone: str
    whattsapp: str
    telegram: str
    email: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.get('id')
        self.phone = schema.get('phone')
        self.whattsapp = schema.get('whattsapp')
        self.telegram = schema.get('telegram')
        self.email = schema.get('email')
