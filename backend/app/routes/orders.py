from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from datetime import datetime
from app.models.order import Order, OrderItem, OrderStatus
from app.models.cart import Cart, CartItem
from app.db.database import engine

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/{user_id}")
def get_orders(user_id: int):
    """Get all orders for a specific user."""
    with Session(engine) as session:
        orders = session.exec(select(Order).where(Order.user_id == user_id)).all()
        return orders


@router.post("/{user_id}/create")
def create_order_from_cart(user_id: int):
    """Create an order from the user's cart."""
    with Session(engine) as session:
        cart = session.exec(select(Cart).where(Cart.user_id == user_id)).first()
        if not cart or not cart.items:
            raise HTTPException(status_code=400, detail="Cart is empty")

        # Create order
        order = Order(user_id=user_id, created_at=datetime.now(), status=OrderStatus.PENDING)
        session.add(order)
        session.commit()
        session.refresh(order)

        # Add items
        for cart_item in cart.items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=cart_item.product_id,
                quantity=cart_item.quantity,
                price=session.get(cart_item.product.__class__, cart_item.product_id).price
            )
            session.add(order_item)

        # Clear cart
        for cart_item in cart.items:
            session.delete(cart_item)

        session.commit()
        return {"message": "Order created", "order_id": order.id}
