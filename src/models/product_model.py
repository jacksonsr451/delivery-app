from sqlalchemy import Column, String, Float, Text

from src.core.database import Base


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(String, primary_key=True)
    slug = Column(String)
    price = Column(Float)
    resume = Column(Text)
    description = Column(Text)
