from fastapi import APIRouter, applications
from apis.version1 import route_users

api_router = APIRouter()

api_router.include_router(route_users.router,prefix="/user",tags=["user"])