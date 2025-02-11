from typing import List, Optional, TypeVar, Generic
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete

from repositories.base_repo import AbstractRepository

T = TypeVar("T")

class BaseSQLAlchemyRepository(AbstractRepository, Generic[T]):
    def __init__(self, session: AsyncSession):
        self._session = session
        
    async def get_by_id(self, entity_id: UUID) -> Optional[T]:
            result = await self._session.execute(
                select(T).where(T.id == entity_id)
            )
            return result.scalars().first()
    
    async def get_list(self) -> List[T]:
        result = await self._session.execute(select(T))
        return result.scalars().all()
    
    async def add(self, entity: T) -> T:
        self._session.add(entity)
        await self._session.commit()
        return entity

    async def update(self, entity: T) -> T:
        self._session.merge(entity)
        await self._session.commit()
        return entity
    
    async def delete(self, entity_id: UUID) -> None:
        await self._session.execute(delete(T).where(T.id == entity_id))
        await self._session.commit()
        