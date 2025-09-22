import asyncio
import websockets
import json


async def handler(websocket):
    # This loop handles incoming messages from a single client

    print("Client connected")

    # Periodically send "Ack" messages to the client every 5 seconds
    async def send_ack():
        try:
            for i in range(1000):
                ack = {"status": "ok", "message": f"Ack {i}"}
                await websocket.send(json.dumps(ack))
                await asyncio.sleep(5)
        except websockets.exceptions.ConnectionClosedOK:
            print("Client disconnected. send_ack()")

    async def reply():
        async for message in websocket:
            print(f"Received: {message}")

            # Parse the JSON message
            try:
                data = json.loads(message)
                response = {
                    "status": "ok",
                    "message": f"Server received: {data['content']}",
                }
            except json.JSONDecodeError:
                response = {"status": "error", "message": "Invalid JSON format"}

            # Send a JSON-formatted response back to the client
            await websocket.send(json.dumps(response))

    # Run both tasks concurrently and terminate both if one finishes
    ack_task = asyncio.create_task(send_ack())
    reply_task = asyncio.create_task(reply())
    done, pending = await asyncio.wait(
        [ack_task, reply_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()

    print("Client disconnected")


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
