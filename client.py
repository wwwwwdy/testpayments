from typing import ClassVar

from aiohttp import TCPConnector

from abstract_client import AbstractInteractionClient
from schema import Charge
from validator import SchemaValidator


class CloudPaymentClient(AbstractInteractionClient):
    BASE_URL: ClassVar[str] = "https://api.cloudpayments.ru"

    def __init__(self, base_url=None, timeout=None, loop=None) -> None:
        self.BASE_URL = base_url if not base_url else self.BASE_URL
        self.CONNECTOR = TCPConnector()
        self.SERVICE = "service"
        self.REQUEST_TIMEOUT = timeout
        self._loop = loop
        super().__init__()

    @SchemaValidator(Charge)
    async def charge(self, data=None):
        response = await self._request(
            "POST",
            self.endpoint_url("payments/charge"),
            data=data,
        )

        return response
