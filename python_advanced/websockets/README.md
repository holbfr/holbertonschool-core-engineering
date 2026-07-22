# Real-time Communication with WebSockets

This project is about building a real-time communication system using **WebSockets** in Python.  
Unlike regular HTTP requests, WebSockets keep a connection open so the server and client can send messages back and forth instantly.

## Project Goals

By completing this project, I learned how to:

- Create a basic WebSocket server
- Build a WebSocket client
- Handle multiple clients
- Validate incoming messages
- Implement unicast and broadcast communication
- Use ASGI with Starlette and Uvicorn
- Build a browser-based WebSocket client

## Project Structure

The main files in this project are:

- `echo_server.py` — WebSocket echo server
- `ws_client.py` — WebSocket client
- `validation_server.py` — server with message validation
- `unicast_server.py` — sends messages only to the sender
- `broadcast_server.py` — sends messages to all connected clients
- `asgi_server.py` — ASGI WebSocket application
- `index.html` — browser interface
- `chat.js` — JavaScript client logic
- `style.css` — page styling

## Requirements

This project uses:

- Python 3
- `websockets`
- `starlette`
- `uvicorn`

You can install the needed dependencies with:
bash

pip install websockets starlette uvicorn

## Task Summary

### 1. Server
Build a WebSocket server that:

- Listens on `localhost:8765`
- Accepts multiple client connections
- Receives text messages
- Sends back the same message it receives
- Keeps the connection open for more messages

### 2. Client
Build a WebSocket client that:

- Connects to `ws://localhost:8765`
- Sends one message
- Receives the response
- Prints the response exactly as received
- Closes the connection cleanly

### 3. Validation
Update the server so that it:

- Checks if a message is empty after trimming spaces
- Sends `ERR:EMPTY` for empty messages
- Sends `OK:<message>` for valid messages
- Keeps the connection open after validation

### 4. Unicast
Create a server that:

- Tracks connected clients
- Sends each message only to the client that sent it
- Adds the prefix `U:`

### 5. Broadcast
Create a server that:

- Tracks all connected clients
- Sends each message to every connected client
- Adds the prefix `B:`

### 6. ASGI Integration
Build a web application that:

- Serves an HTML page at `http://localhost:8000`
- Exposes a WebSocket endpoint at `ws://localhost:8000/ws`
- Uses Starlette for routing
- Runs with Uvicorn

### 7. Browser Client
Create a browser-based client that:

- Connects to the WebSocket server
- Lets the user send messages
- Displays incoming messages
- Works in real time without reloading the page

## How to Run

### Start the server
```
python3 echo_server.py
```

### Run the client
```
python3 ws_client.py
```

### Start the ASGI app
```
uvicorn asgi_server:app --host 0.0.0.0 --port 8000 --reload
```

Then open: [http://localhost:8000](http://localhost:8000)

## Manual Testing

You can test the server with:

- the `websockets` command-line client
- a Python test script
- a browser WebSocket client
- tools like **websocat**, **Postman**, or **Insomnia**

Example:
```
Hello
```

Expected response:
```
Hello
```

## What I Learned

This project helped me understand:

- Persistent connections vs HTTP requests
- Asynchronous programming with `async` and `await`
- Message flow between client and server
- Real-time communication patterns
- WebSocket routing and validation

## Conclusion

- This project was a great introduction to real-time applications.  
- It showed how WebSockets can be used to build interactive systems like chat apps and live dashboards.


