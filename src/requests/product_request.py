from typing import Any


class ProductRequest:
    id: str
    slug: str
    price: float
    resume: str
    description: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.form['id']
        self.slug = schema.form['slug']
        self.price = schema.form['price']
        self.resume = schema.form['resume']
        self.description = schema.form['description']
