import asyncio
from aiohttp import web

async def echo_handler(req):
    responce = web.Response(text=req.match_info['what'])
    await responce.prepare(req)
    return responce

async def start_server(runner):
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

app = web.Application()
app.add_routes(web.get('/echo/{what}', echo_handler))
runner = web.AppRunner(app)

loop = asyncio.get_event_loop()
loop.create_task(start_server(runner))
loop.run_forever()
loop.close()
