from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.product import Product
from app.db.database import engine

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/")
def get_products():
    """Get all products."""
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
        return products


@router.get("/{product_id}")
def get_product(product_id: int):
    """Get a product by ID."""
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
