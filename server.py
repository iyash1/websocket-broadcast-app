# -------------------------------
#  WebSocket Server for Real-Time Communication
#  This server listens for incoming WebSocket connections and broadcasts
#  messages to all connected clients.
# -------------------------------
import asyncio
import websockets

# Store connected clients in a set to track all active connections
connected_clients = set()

# Handler function called whenever a client connects
async def handler(websocket):
    print("New client connected")
    # Add the new client to our set of connected clients
    connected_clients.add(websocket)

    try:
        # Listen for incoming messages from this client
        async for message in websocket:
            print(f"Received: {message}")

            # Broadcast the message to all other connected clients
            for client in connected_clients:
                # Don't send the message back to the sender
                if client != websocket:
                    await client.send(message)

    # Handle case when client disconnects
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

    finally:
        # Always remove the client from our set when they disconnect
        connected_clients.remove(websocket)

# Main function to start the server
async def main():
    # Create a WebSocket server on localhost:8765
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server running on ws://localhost:8765")
        # Keep the server running indefinitely
        await asyncio.Future()

# Entry point of the program
if __name__ == "__main__":
    asyncio.run(main())