class RoleResponse:
    id: str
    role: str

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.role = data.role
