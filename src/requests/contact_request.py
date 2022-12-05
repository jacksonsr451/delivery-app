from typing import Any


class ContactRequest:
    id: str
    phone: str
    whattsapp: str
    telegram: str
    email: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.form['id']
        self.phone = schema.form['phone']
        self.whattsapp = schema.form['whattsapp']
        self.telegram = schema.form['telegram']
        self.email = schema.form['email']
