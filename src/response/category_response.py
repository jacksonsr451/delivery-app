class CategoryResponse:
    id: str
    slug: str
    title: str
    description: str

    def __init__(self, data: object) -> None:
        self.id = data.id
        self.slug = data.slug 
        self.title = data.title 
        self.description = data.descripion
