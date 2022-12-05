from typing import Any


class ProfileRequest:
    id: str
    name: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.get('id')
        self.name = schema.get('name')
