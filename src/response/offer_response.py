from datetime import date

from .category_response import CategoryResponse
from .product_response import ProductResponse

class OfferResponse:
    id: str
    slug: str
    category: CategoryResponse
    product: ProductResponse
    discount: float
    created_at: date
    valid_until: date

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.slug = data.slug
        self.category = CategoryResponse(data.category)
        self.product = ProductResponse(data.producty)
        self.discount = data.discount
        self.created_at = data.created_at
        self.valid_until = data.valid_until
