from fastapi import APIRouter
from app.api.routes import items
from app.api.routes import users
from app.api.routes import auth


router = APIRouter()

router.include_router(items.router, prefix="/items")
router.include_router(users.router, prefix="/users")
router.include_router(auth.router, tags=["auth"])
