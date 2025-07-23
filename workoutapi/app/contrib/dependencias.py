from typing import Annotated
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.configs.database import get_session


DataBaseDependency = Annotated[AsyncSession, Depends(get_session)]