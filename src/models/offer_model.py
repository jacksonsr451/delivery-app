from sqlalchemy import Column, Date, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from src.core.database import Base


class OfferModel(Base):
    __tablename__ = 'offers'

    id = Column(String, primary_key=True)
    slug = Column(String)
    category_id = Column(String, ForeignKey('categories.id'))
    category = relationship('CategoryModel', foreign_keys=[category_id])
    product_id = Column(String, ForeignKey('products.id'))
    product = relationship('ProductModel', foreign_keys=[product_id])
    discount = Column(Float)
    created_at = Column(Date)
    valid_until = Column(Date)
