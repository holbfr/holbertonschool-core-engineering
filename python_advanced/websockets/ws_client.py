#!/usr/bin/env python3

import asyncio
from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    async with connect(uri) as websocket:
        user_msg = "Hello WebSocket"
        server_resp = await websocket.send(user_msg)
        await websocket.recv()
        print(text, end="")
    return text.strip()


if __name__ == "__main__":
    uri = "ws://localhost:8765"
    asyncio.run(connect_and_send(uri=uri, text="demo"))
