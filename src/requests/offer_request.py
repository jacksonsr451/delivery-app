from datetime import date
from typing import Any

from .category_request import CategoryRequest
from .product_request import ProductRequest


class OfferRequest:
    id: str
    slug: str
    category: CategoryRequest
    product: ProductRequest
    discount: float
    created_at: date
    valid_until: date

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.form['id']
        self.slug = schema.form['slug']
        self.category = CategoryRequest(schema.form['category'])
        self.product = ProductRequest(schema.form['producty'])
        self.discount = schema.form['discount']
        self.created_at = schema.form['created_at']
        self.valid_until = schema.form['valid_until']
