from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from workoutapi.app.categorias.schemas import CategoriaIn, CategoriaOut
from workoutapi.app.categorias.models import CategoriaModel

from workoutapi.app.contrib.dependencias import DataBaseDependency
from sqlalchemy.future import select

router = APIRouter()

@router.post(
    '/', 
    summary='Criar uma nova Categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    db_sessinon: DataBaseDependency, 
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_sessinon.add(categoria_model)
    await db_sessinon.commit()
    
    return categoria_out
    
@router.get(
    '/', 
    summary='Consultar todas as Categorias',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(db_sessinon: DataBaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_sessinon.execute(select(CategoriaModel))).scalars().all()
    
    return categorias

@router.get(
    '/{id}', 
    summary='Consulta Categoria pelo ID',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def query(id: UUID4, db_sessinon: DataBaseDependency) -> CategoriaOut:
    categoria: CategoriaOut = (
        await db_sessinon.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()

    if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Categoria não encontrada no ID: {id}'
            )

    return categoria