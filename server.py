import asyncio
import json
from typing import Any, Union

import aiohttp_jinja2
import jinja2
from aiohttp import web

from client import CloudPaymentClient


async def handle_post(request) -> web.Response:
    print("POST handle_post request accepted")
    return web.Response(
        text="Оплата почти прошла. Неизвестно как авторизовываться. PublicId тут не работает"
    )


async def handle(request) -> Union[Any, web.Response]:
    loop = asyncio.get_event_loop()
    client = CloudPaymentClient("https://api.cloudpayments.ru", loop=loop)
    print("GET handle request accepted")
    with open("data.json", "r") as file:
        checkout_data = file.read()
        checkout_data = json.loads(checkout_data)
    response = await client.charge(checkout_data)

    if response.get("Success"):
        return web.Response(text="Оплата прошла успешно")

    context = {
        "pa_req": response["Model"].get("PaReq"),
        "transation_id": response["Model"].get("TransactionId")
    }
    response = aiohttp_jinja2.render_template(
        'checkout.html', request, context
    )

    return response


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('.'))
app.add_routes([web.get('/', handle),
                web.post('/checkout/', handle_post)])


if __name__ == '__main__':
    web.run_app(app)
