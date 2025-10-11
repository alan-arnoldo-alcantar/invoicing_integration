from app.core.config import settings
import logging
import httpx

logging.basicConfig(
    level=logging.DEBUG, format="[%(asctime)s] - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def read_companies():
    try:
        headers = {"Authorization": f"Bearer {settings.FACTURAPI_USER_SECRET_KEY}"}
        response = httpx.get(
            url=f"{settings.FACTURAPI_URL}/organizations", headers=headers
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        logger.warning(f"Status error: {exc}")
    except httpx.RequestError as exc:
        logger.warning(f"Request error: {exc}")
    except Exception as e:
        logger.warning(f"Unexpected error: {e}")
