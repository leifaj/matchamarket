from sqlmodel import SQLModel, Session
from sqlalchemy import text
from pathlib import Path
import json
from datetime import datetime

from app.db.database import engine
from app.models.product import Product
from app.models.user import User
from app.models.order import Order, OrderItem, OrderStatus
from app.models.cart import Cart, CartItem

# Path to JSON data
DATA_DIR = Path(__file__).parent / "data"
USERS_FILE = DATA_DIR / "users.json"
PRODUCTS_FILE = DATA_DIR / "products.json"
CARTS_FILE = DATA_DIR / "carts.json"
CART_ITEMS_FILE = DATA_DIR / "cart_items.json"
ORDERS_FILE = DATA_DIR / "orders.json"
ORDER_ITEMS_FILE = DATA_DIR / "order_items.json"


def reset_database():
    """Drops all tables and recreates them (dev only)."""
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE;"))
        conn.execute(text("CREATE SCHEMA public;"))
    SQLModel.metadata.create_all(engine)
    print("Database reset and tables created.")


def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def seed_data():
    """Seed database from JSON files."""
    with Session(engine) as session:
        # Users
        users_data = load_json(USERS_FILE)
        users = []
        for u in users_data:
            user = User(
                username=u.get("username"),
                email=u["email"],
                password_hash=u["password_hash"],
                first_name=u.get("first_name", ""),
                last_name=u.get("last_name", ""),
                role=u.get("role", "customer"),
            )
            users.append(user)
        session.add_all(users)
        session.commit()
        print(f"Inserted {len(users)} users")

        # Products
        products_data = load_json(PRODUCTS_FILE)
        products = [Product(**p) for p in products_data]
        session.add_all(products)
        session.commit()
        print(f"Inserted {len(products)} products")

        # Carts
        carts_data = load_json(CARTS_FILE)
        carts = [Cart(**c) for c in carts_data]
        session.add_all(carts)
        session.commit()
        print(f"Inserted {len(carts)} carts")

        # Cart Items
        cart_items_data = load_json(CART_ITEMS_FILE)
        cart_items = [CartItem(**ci) for ci in cart_items_data]
        session.add_all(cart_items)
        session.commit()
        print(f"Inserted {len(cart_items)} cart items")

        # Orders
        orders_data = load_json(ORDERS_FILE)
        orders = []
        for o in orders_data:
            o["created_at"] = datetime.fromisoformat(o["created_at"].replace("Z", "+00:00"))
            o["status"] = OrderStatus[o["status"]]
            orders.append(Order(**o))
        session.add_all(orders)
        session.commit()
        print(f"Inserted {len(orders)} orders")

        # Order Items
        order_items_data = load_json(ORDER_ITEMS_FILE)
        order_items = [OrderItem(**oi) for oi in order_items_data]
        session.add_all(order_items)
        session.commit()
        print(f"Inserted {len(order_items)} order items")

        print("Seed data inserted.")


def create_db_and_seed():
    reset_database()
    seed_data()


if __name__ == "__main__":
    create_db_and_seed()
