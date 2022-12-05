from typing import Any


class AddressRequest:
    id: str
    country: str
    state: str
    neigborhod: str
    street: str
    number: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.form['id']
        self.country = schema.form['country']
        self.state = schema.form['state']
        self.neigborhod = schema.form['neigborhod']
        self.street = schema.form['street']
        self.number = schema.form['number']
