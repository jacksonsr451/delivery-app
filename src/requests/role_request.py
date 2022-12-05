from typing import Any


class RoleRequest:
    id: str
    role: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.form['id']
        self.role = schema.form['role']
