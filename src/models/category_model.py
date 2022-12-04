from sqlalchemy import Column, String, Text

from src.core.database import Base


class CategoryModel(Base):
    __tablename__ = 'categories'

    id = Column(String, primary_key=True)
    slug = Column(String)
    title = Column(String)
    description = Column(Text)
