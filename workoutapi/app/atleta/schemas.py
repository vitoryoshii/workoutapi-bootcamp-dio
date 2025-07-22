from typing import Annotated
from pydantic import Field, PositiveFloat
from workoutapi.app.contrib.schema import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example=22)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=72.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example=1.72)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='M', max_length=1)]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass