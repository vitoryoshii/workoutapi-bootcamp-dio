from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from workoutapi.app.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workoutapi.app.centro_treinamento.models import CentroTreinamentoModel

from workoutapi.app.contrib.dependencias import DataBaseDependency
from sqlalchemy.future import select

router = APIRouter()


@router.post(
    '/', 
    summary='Criar um novo Centro de Treinamento',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut
)
async def post(
    db_sessinon: DataBaseDependency, 
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())

    db_sessinon.add(centro_treinamento_model)
    await db_sessinon.commit()
    
    return centro_treinamento_out


@router.get(
    '/', 
    summary='Consultar todos os Centros de Treinamentos',
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_sessinon: DataBaseDependency) -> list[CentroTreinamentoOut]:
    centros_treinamenos : list[CentroTreinamentoOut] = (
        await db_sessinon.execute(select(CentroTreinamentoModel))
    ).scalars().all()
    
    return centros_treinamenos


@router.get(
    '/{id}', 
    summary='Consulta Centro Treinamento pelo ID',
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id: UUID4, db_sessinon: DataBaseDependency) -> CentroTreinamentoOut:
    centro_treinamento: CentroTreinamentoOut = (
        await db_sessinon.execute(select(CentroTreinamentoModel).filter_by(id=id))
    ).scalars().first()

    if not centro_treinamento:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Centro de Treinamento não encontrado no ID: {id}'
            )

    return centro_treinamento

# endpoint do patch by id
@router.patch(
    '/{id}', 
    summary='Editar Centro de Treinamento pelo ID',
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id: UUID4, db_sessinon: DataBaseDependency, centro_treinamento_up: CentroTreinamentoIn = Body(...)) -> CentroTreinamentoOut:
    centro_treinamento: CentroTreinamentoOut = (
        await db_sessinon.execute(select(CentroTreinamentoModel).filter_by(id=id))
    ).scalars().first()

    if not centro_treinamento:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Centro de treinamento não encontrado no ID: {id}'
            )

    centro_treinamento_update = centro_treinamento_up.model_dump(exclude_unset=True)
    for key, value in centro_treinamento_update.items():
        setattr(centro_treinamento, key, value)

    await db_sessinon.commit()
    await db_sessinon.refresh(centro_treinamento)

    return centro_treinamento

@router.delete(
    '/{id}', 
    summary='Deletar Centro de Treinamento pelo ID',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def query(id: UUID4, db_sessinon: DataBaseDependency) -> None:
    centro_treinamento: CentroTreinamentoOut = (
        await db_sessinon.execute(select(CentroTreinamentoModel).filter_by(id=id))
    ).scalars().first()

    if not centro_treinamento:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Centro de Treinamento não encontrado no ID: {id}'
            )
    
    await db_sessinon.delete(centro_treinamento)
    await db_sessinon.commit()

    return centro_treinamento