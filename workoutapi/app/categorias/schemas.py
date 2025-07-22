from typing import Annotated
from workoutapi.app.contrib.schema import BaseSchema
from pydantic import Field


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da Categoria', example='Scale', max_length=10)]
    
