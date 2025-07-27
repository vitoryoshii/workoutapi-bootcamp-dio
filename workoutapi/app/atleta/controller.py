from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from workoutapi.app.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate, AtletaDB
from workoutapi.app.atleta.models import AtletaModel
from workoutapi.app.categorias.models import CategoriaModel
from workoutapi.app.centro_treinamento.models import CentroTreinamentoModel
from workoutapi.app.contrib.dependencias import DataBaseDependency

router = APIRouter()


@router.post(
    '/', 
    summary='Criar um novo atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut
)
async def post(
    db_session: DataBaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_nome))
    ).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f'A categoria {categoria_nome} não foi encontrada.'
        )
    
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome))
    ).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f'O centro de treinamento {centro_treinamento_nome} não foi encontrado.'
        )
    try:
        atleta_out = AtletaDB(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))

        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
            
        db_session.add(atleta_model)
        await db_session.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Ocorreu um erro ao inserir os dados no banco: {e}'
        )

    return atleta_out


@router.get(
    '/', 
    summary='Consultar todos os Atetlas',
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],
)
async def query(db_sessinon: DataBaseDependency) -> list[AtletaOut]:
    atletas: list[AtletaOut] = (await db_sessinon.execute(select(AtletaModel))).scalars().all()
    
    return atletas

@router.get(
    '/{id}', 
    summary='Consulta Atleta pelo ID',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def query(id: UUID4, db_sessinon: DataBaseDependency) -> AtletaOut:
    atleta: AtletaOut = (
        await db_sessinon.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Atleta não encontrado no ID: {id}'
            )

    return atleta

@router.patch(
    '/{id}', 
    summary='Edita um Atleta pelo ID',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def query(id: UUID4, db_sessinon: DataBaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: AtletaOut = (
        await db_sessinon.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Atleta não encontrado no ID: {id}'
            )

    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_sessinon.commit()
    await db_sessinon.refresh(atleta)

    return atleta


@router.delete(
    '/{id}', 
    summary='Deleta Atleta pelo ID',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def query(id: UUID4, db_sessinon: DataBaseDependency) -> None:
    atleta: AtletaOut = (
        await db_sessinon.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Atleta não encontrado no ID: {id}'
            )
    
    await db_sessinon.delete(atleta)
    await db_sessinon.commit()

    return atleta