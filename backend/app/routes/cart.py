from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.cart import Cart, CartItem
from app.models.product import Product
from app.db.database import engine

router = APIRouter(prefix="/cart", tags=["cart"])


@router.get("/{user_id}")
def get_cart(user_id: int):
    """Get the cart for a specific user."""
    with Session(engine) as session:
        cart = session.exec(select(Cart).where(Cart.user_id == user_id)).first()
        if not cart:
            return {"items": []}
        return cart
    
@router.get("/user/{user_id}/items")
def get_cart_items_by_user(user_id: int):
    """
    Get all items in a user's cart, including product details.
    """
    with Session(engine) as session:
        # Fetch the cart for this user
        statement = select(Cart).where(Cart.user_id == user_id)
        cart = session.exec(statement).first()
        
        if not cart:
            raise HTTPException(status_code=404, detail="Cart not found for this user")

        # Build response with product info
        items = []
        for item in cart.items:
            product = session.get(Product, item.product_id)
            items.append({
                "cart_item_id": item.id,
                "product_id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity": item.quantity,
            })

        return {"user_id": user_id, "cart_id": cart.id, "items": items} 


@router.post("/{user_id}/add")
def add_to_cart(user_id: int, product_id: int, quantity: int = 1):
    """Add an item to the user's cart."""
    with Session(engine) as session:
        cart = session.exec(select(Cart).where(Cart.user_id == user_id)).first()
        if not cart:
            cart = Cart(user_id=user_id)
            session.add(cart)
            session.commit()
            session.refresh(cart)

        # Check if item exists
        item = session.exec(
            select(CartItem).where(CartItem.cart_id == cart.id, CartItem.product_id == product_id)
        ).first()

        if item:
            item.quantity += quantity
        else:
            item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
            session.add(item)

        session.commit()
        return {"message": "Item added", "cart_id": cart.id}


@router.delete("/{user_id}/remove/{product_id}")
def remove_from_cart(user_id: int, product_id: int):
    """Remove an item from the user's cart."""
    with Session(engine) as session:
        cart = session.exec(select(Cart).where(Cart.user_id == user_id)).first()
        if not cart:
            raise HTTPException(status_code=404, detail="Cart not found")

        item = session.exec(
            select(CartItem).where(CartItem.cart_id == cart.id, CartItem.product_id == product_id)
        ).first()
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        session.delete(item)
        session.commit()
        return {"message": "Item removed"}
