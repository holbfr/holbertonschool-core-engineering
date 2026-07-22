#!/usr/bin/env python
import asyncio
from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    async with connect(uri) as websocket:
        await websocket.send(text)
        server_response = await websocket.recv()
        return server_response


async def main():
    uri = "ws://localhost:8765"
    response = await connect_and_send(uri=uri, text="demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
