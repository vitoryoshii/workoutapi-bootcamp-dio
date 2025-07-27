from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from workoutapi.app.categorias.schemas import CategoriaIn, CategoriaOut, CategoriaUpdate
from workoutapi.app.categorias.models import CategoriaModel

from workoutapi.app.contrib.dependencias import DataBaseDependency
from sqlalchemy.future import select

router = APIRouter()

# endpoint do post  
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
    
# endpoint do get all
@router.get(
    '/', 
    summary='Consultar todas as Categorias',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(db_sessinon: DataBaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_sessinon.execute(select(CategoriaModel))).scalars().all()
    
    return categorias

# endpoint do get by id
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

# endpoint do patch by id
@router.patch(
    '/{id}', 
    summary='Editar categoria pelo ID',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def query(id: UUID4, db_sessinon: DataBaseDependency, categoria_up: CategoriaUpdate = Body(...)) -> CategoriaOut:
    categoria: CategoriaOut = (
        await db_sessinon.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()

    if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Atleta não encontrado no ID: {id}'
            )

    categoria_update = categoria_up.model_dump(exclude_unset=True)
    for key, value in categoria_update.items():
        setattr(categoria, key, value)

    await db_sessinon.commit()
    await db_sessinon.refresh(categoria)

    return categoria

@router.delete(
    '/{id}', 
    summary='Deleta categoria pelo ID',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def query(id: UUID4, db_sessinon: DataBaseDependency) -> None:
    categoria: CategoriaOut = (
        await db_sessinon.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()

    if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Atleta não encontrado no ID: {id}'
            )
    
    await db_sessinon.delete(categoria)
    await db_sessinon.commit()

    return categoria