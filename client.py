from typing import ClassVar, Dict, Any

from aiohttp import TCPConnector

from abstract_client import AbstractInteractionClient
from schema import Charge
from validator import SchemaValidator


class CloudPaymentClient(AbstractInteractionClient):
    BASE_URL: ClassVar[str] = "https://api.cloudpayments.ru"

    def __init__(self, base_url=BASE_URL, timeout=None, loop=None) -> None:
        self.BASE_URL = base_url
        self.CONNECTOR = TCPConnector()
        self.SERVICE = "service"
        self.REQUEST_TIMEOUT = timeout
        self._loop = loop
        super().__init__()

    @SchemaValidator(Charge)
    async def charge(self, data=None) -> Dict[str, Any]:
        response = await self._request(
            "POST",
            self.endpoint_url("payments/charge"),
            data=data,
        )

        return response
