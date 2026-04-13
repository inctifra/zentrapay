from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from zentrapay.config.settings.production import settings
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(settings.DATABASE_URL, echo=True, poolclass=NullPool)


AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
