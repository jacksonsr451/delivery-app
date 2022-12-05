class AuthReponse:
    id: str
    username: str

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.username = data.username
