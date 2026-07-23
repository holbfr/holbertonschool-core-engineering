#!/usr/bin/env python3


"""
An async connection_handler(websocket) that, for each text message received
on that connection, sends back one outgoing text message whose value is
exactly the same message string (no extra newline unless the client sent one).

Constraints
Use the websockets library
Use asynchronous programming (async / await)
The server must handle messages continuously (it must not
stop after one message).
Messages must be processed as they arrive (no batching or delays)
Only text messages need to be supported
The server must start when executing:
python3 echo_server.py
After launching your app server you can test the connection between
the server and the client on another terminal using the following command:
websockets ws://localhost:8765/
"""

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """
    for each text message received on that connection,
    sends back one outgoing text message whose value is exactly
    the same message string (no extra newline unless the client sent one).
    """
    try:
        message = await websocket.recv()
        message = message.strip()
        if len(message) == 0:
            response = "ERR:EMPTY"
        else:
            response = f"OK:{message}"
        await websocket.send(response)
        print(response)
    except (ConnectionClosed, Exception) as e:
        await websocket.send(e)
        print(e)


async def main():
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
