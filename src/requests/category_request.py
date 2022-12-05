from typing import Any


class CategoryRequest:
    id: str
    slug: str
    title: str
    description: str

    def __init__(self, schema: dict[str, Any]) -> None:
        self.id = schema.form['id']
        self.slug = schema.form['slug']
        self.title = schema.form['title']
        self.description = schema.form['descripion']
