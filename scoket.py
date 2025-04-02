import asyncio
import websockets

async def connect_to_websocket(uri):
    # Connect to the WebSocket server
    async with websockets.connect(uri) as websocket:
        print("Connected to {}".format(uri))
        
        # Send a message to the server
        message_to_send = "Hello, WebSocket Server!"
        await websocket.send(message_to_send)
        print("Sent to {}".format(message_to_send))
        
        # Wait and receive a message from the server
        response = await websocket.recv()
        print("Received: {}".format(response))

        # Optionally, you can continue sending and receiving messages in a loop
        # For example, you can implement a simple chat functionality
        while True:
            # Get user input to send to the server
            message_to_send = input("Enter message to send: ")
            await websocket.send(message_to_send)
            print("Sent: {}".format(message_to_send))

            # Receive and print the response from the server
            response = await websocket.recv()
            print("Received: {}".format(response))

# URI of the WebSocket server
uri = "ws://192.168.88.117:5000"  # Replace with the actual URI of the server

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(connect_to_websocket(uri))
