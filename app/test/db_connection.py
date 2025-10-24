from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
import asyncio
from sqlalchemy import select
from ..core.db import engine
from tenacity import retry, wait_fixed, before_log, after_log, stop_after_attempt
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
async def init_db(engine: AsyncEngine):
    try:
        async with AsyncSession(engine) as session:
            await session.execute(select(1))
            logger.info("Database responded :D")
    except Exception as e:
        logger.error(e)
        raise e


async def main():
    logger.info("Initializing database connection...")
    await init_db(engine=engine)
    logger.info("Database finished initializing.")


if __name__ == "__main__":
    asyncio.run(main())
    # Run this script as module, python -m app.test.db_connection
