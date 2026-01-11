from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.user import User
from app.db.database import engine

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}")
def get_user(user_id: int):
    """Get a user by ID."""
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
