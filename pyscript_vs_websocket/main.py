from pyscript import document, when, WebSocket
import json

# Define the WebSocket server URL
ws_url = "ws://localhost:8765"
ws = None

@when("click", "#send-btn")
def send_message():
    """Sends a message from the input field to the server."""
    global ws
    if ws is None or ws.readyState != WebSocket.OPEN:
        output_div = document.getElementById("output")
        output_div.innerText = "Connection is not open."
        return

    message_input = document.getElementById("message-input")
    message = message_input.value

    if message == "":
        print(f"Why do we enter twice into 'sendmessage()?'. {message=}")
        return
    
    message_data = {"content": message}
   
    # Send the JSON string
    ws.send(json.dumps(message_data))
    message_input.value = ""

async def on_message(event):
    """Handles incoming messages from the server."""
    output_div = document.getElementById("output")
    output_div.innerText += f"\nServer: {event.data}"

async def on_open(event):
    """Fired when the connection is open."""
    print("Connection opened!")
    output_div = document.getElementById("output")
    output_div.innerText = "Connected to server!"

async def on_close(event):
    """Fired when the connection is closed."""
    print("Connection closed!")

def connect():
    """Initializes the WebSocket connection."""
    global ws
    ws = WebSocket(url=ws_url)
    ws.onmessage = on_message
    ws.onopen = on_open
    ws.onclose = on_close

connect()
