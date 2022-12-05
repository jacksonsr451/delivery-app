class ProfileResponse:
    id: str
    name: str

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.name = data.name
