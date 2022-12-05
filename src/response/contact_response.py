class ContactResponse:
    id: str
    phone: str
    whattsapp: str
    telegram: str
    email: str

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.phone = data.phone
        self.whattsapp = data.whattsapp
        self.telegram = data.telegram
        self.email = data.email
