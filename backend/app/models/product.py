from sqlmodel import JSON, Column, SQLModel, Field
from typing import Optional, List

class Product(SQLModel, table=True):
    __tablename__ = "products"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    inventory: int = Field(default=0)
    image_urls: List[str] = Field(default_factory=list, sa_column=Column(JSON))

    # TODO: add category?