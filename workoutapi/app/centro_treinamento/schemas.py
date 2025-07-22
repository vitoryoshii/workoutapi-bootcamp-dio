from typing import Annotated

from workoutapi.app.contrib.schema import BaseSchema
from pydantic import Field


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT Forte', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do Centro de Treinamento', example='Rua x, Q03', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do Centro de Treinamento', example='Vitor Yoshii', max_length=30)]
    
