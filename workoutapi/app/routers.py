from fastapi import APIRouter
from workoutapi.app.atleta.controller import router as atleta
from workoutapi.app.categorias.controller import router as categoria
from workoutapi.app.centro_treinamento.controller import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria, prefix='/categoria', tags=['categoria'])
api_router.include_router(centro_treinamento, prefix='/centro_treinamento', tags=['centro_treinamento'])