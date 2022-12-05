from typing import Any


class RoleRequest:
    id: str
    role: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.get('id')
        self.role = schema.get('role')
