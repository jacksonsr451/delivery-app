from typing import Any


class ProductRequest:
    id: str
    slug: str
    price: float
    resume: str
    description: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.get('id')
        self.slug = schema.get('slug')
        self.price = schema.get('price')
        self.resume = schema.get('resume')
        self.description = schema.get('description')
