from typing import Any


class CategoryRequest:
    id: str
    slug: str
    title: str
    description: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.get('id')
        self.slug = schema.get('slug')
        self.title = schema.get('title')
        self.description = schema.get('descripion')
