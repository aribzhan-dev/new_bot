from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import DATABASE_URL

engine = None
AsyncSessionLocal: async_sessionmaker[AsyncSession] | None = None

async def init_engine():
    global engine, AsyncSessionLocal
    engine = create_async_engine(DATABASE_URL, echo=False, future=True)
    AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Helper: get session
def get_session() -> AsyncSession:
    if AsyncSessionLocal is None:
        raise RuntimeError("DB not initialized. Call init_engine() first.")
    return AsyncSessionLocal()

