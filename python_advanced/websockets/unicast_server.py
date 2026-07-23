#!/usr/bin/env python3


"""
The server:
Accepts multiple client connections
Keeps track of connected clients
Receives messages from any client
Sends the response only to the sender
Prefixes responses with: `U:`
"""

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket):
    """
    for each text message received on that connection,
    sends back one outgoing text message whose value is exactly
    the same message string (no extra newline unless the client sent one).
    """
    try:
        # for k,v in websocket.__dict__.items():
        #     print(f"{k}: {v}")
        # print(websocket.__dict__['id'])
        connection_obj = websocket
        connected_clients.add(connection_obj)
        message = await websocket.recv()
        message = message.strip()
        if len(message) == 0:
            response = "ERR:EMPTY"
        else:
            response = f"U:{message}"
        await websocket.send(response)
        print(response)
        connected_clients.remove(connection_obj)
    except (ConnectionClosed, Exception) as e:
        await websocket.send(e)
        print(e)


async def main():
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
