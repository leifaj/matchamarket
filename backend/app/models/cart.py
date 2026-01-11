from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .user import User
    from .cart import Cart, CartItem
    from .product import Product

class Cart(SQLModel, table=True):
    __tablename__ = "carts"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")

    user: Optional["User"] = Relationship(back_populates="cart")
    items: List["CartItem"] = Relationship(back_populates="cart")


class CartItem(SQLModel, table=True):
    __tablename__ = "cart_items"
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="carts.id")
    product_id: int = Field(foreign_key="products.id")
    quantity: int = Field(default=1)
    cart: Optional[Cart] = Relationship(back_populates="items")
