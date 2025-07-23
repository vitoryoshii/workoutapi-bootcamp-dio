from typing import Annotated

from workoutapi.app.contrib.schema import BaseSchema
from pydantic import UUID4, Field


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT Bravos Box', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do Centro de Treinamento', example='Rua x, Q03', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do Centro de Treinamento', example='João Ferreira Silva', max_length=30)]
    
class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de Treinamento', example='CT Bravos Box', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]