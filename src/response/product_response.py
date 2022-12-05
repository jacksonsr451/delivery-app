from typing import Any

ProductDTO: dict[str, Any] = {
    'id': '',
    'slug': '',
    'price': '',
    'resume': '',
    'description': '',
}

class ProductResponse:
    id: str
    slug: str
    price: float
    resume: str
    description: str

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.slug = data.slug
        self.price = data.price
        self.resume = data.resume
        self.description = data.description
