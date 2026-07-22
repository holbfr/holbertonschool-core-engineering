#!/usr/bin/env python3

import asyncio
from websockets.sync.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    with connect(uri) as websocket:
        user_msg = "Hello WebSocket"
        websocket.send(user_msg)
        print(user_msg)
        server_resp = websocket.recv()
        print(server_resp, end="")
    websocket.close()
    return text


async def main():
    uri = "ws://localhost:8765"
    await connect_and_send(uri, "demo")


if __name__ == "__main__":
    asyncio.run(main())
