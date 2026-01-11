from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import init_db
from app.routes import products, users, cart, orders

# Define app lifespan events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup tasks
    print("Starting up, initializing database...")
    init_db()  # Initialize the database
    yield # App runs here
    
    # Shutdown tasks
    print("Shutting down, cleaning up resources...")

# Create FastAPI app with lifespan
app = FastAPI(
    title="Matcha Market API",
    lifespan=lifespan
)

# Include routers
app.include_router(products.router, tags=["products"])
app.include_router(users.router, tags=["users"])
app.include_router(cart.router, tags=["cart"])
app.include_router(orders.router, tags=["orders"])