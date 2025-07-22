from fastapi import APIRouter, Body, status

from workoutapi.app.atleta.schemas import AtletaIn
from workoutapi.app.contrib.dependencias import DataBaseDependecy

router = APIRouter()

@router.post(
    '/', 
    summary='Criar novo atleta',
    status_code=status.HTTP_201_CREATED
)
async def post(
    db_sessinon: DataBaseDependecy, 
    atleta_in: AtletaIn = Body(...)
):
    pass