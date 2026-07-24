from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute

async def homepage(request):
    return HTMLResponse("<h1>Hello</h1>")

async def websocket_endpoint(websocket):
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(f"Message text was: {message}")
    await websocket.close()


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
