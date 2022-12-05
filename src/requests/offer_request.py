from datetime import date
from typing import Any

from .category_request import CategoryRequest
from .product_request import ProductRequest

class OfferRequest:
    id: str
    slug: str
    category: CategoryRequest
    product: ProductRequest
    discount: str
    created_at: date
    valid_until: date

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.get('id')
        self.slug = schema.get('slug')
        self.category = CategoryRequest(schema.get('category'))
        self.product = ProductRequest(schema.get('producty'))
        self.discount = schema.get('discount')
        self.created_at = schema.get('created_at')
        self.valid_until = schema.get('valid_until')
