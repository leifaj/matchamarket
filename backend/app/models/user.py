from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from enum import Enum

if TYPE_CHECKING:
    from .order import Order
    from .cart import Cart

class UserRole(str, Enum):
    customer = "customer"
    admin = "admin"

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    password_hash: str
    first_name: str = Field(default="")
    last_name: str = Field(default="")
    role: UserRole = Field(default=UserRole.customer)

    orders: List["Order"] = Relationship(back_populates="user")
    cart: Optional["Cart"] = Relationship(back_populates="user", sa_relationship_kwargs={"uselist": False})
