from datetime import date
from typing import Any


Offer: dict[str, Any] = {
    'id': '',
    'slug': '',
    'category_id': '',
    'category': {
        'id': '',
        'slug': '',
        'title': '',
        'description': ''
    },
    'product_id': '',
    'product': {
        'id': '',
        'slug': '',
        'price': '',
        'resume': '',
        'description': ''
    },
    'discount': '',
    'created_at': date,
    'valid_until': date
}
