class AddressResponse:
    id: str
    country: str
    state: str
    neigborhod: str
    street: str
    number: str

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.country = data.country
        self.state = data.state
        self.neigborhod = data.neigborhod
        self.street = data.street
        self.number = data.number
