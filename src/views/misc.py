import logging
from typing import NoReturn

from fastapi import APIRouter
from sentry_sdk import capture_message
from starlette.responses import Response

logger = logging.getLogger(__name__)


async def health_check() -> Response:
    return Response(status_code=200)


async def sentry_trigger() -> NoReturn:
    capture_message("This is an intentionally triggered message for the sentry")

    return 1 / 0


router = APIRouter()

router.add_api_route(methods=["GET"], path="/healthcheck", status_code=200, endpoint=health_check)
router.add_api_route(
    methods=["GET"], path="/sentry_trigger", status_code=200, endpoint=sentry_trigger, include_in_schema=False, response_model=None
)
