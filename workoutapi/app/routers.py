from fastapi import APIRouter
from workoutapi.app.atleta.controller import router

api_router = APIRouter()
api_router.include_router(router, prefix='/atletas', tags=['atletas'])