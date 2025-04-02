import asyncio
import websockets

async def connect_to_websocket(uri):
    try:
        # Connect to the WebSocket server
        print("Connecting to {}".format(uri))
        async with websockets.connect(uri) as websocket:
            print("Connected to {}".format(uri))

            # Send a message to the server (UTF-8 encoded)
            message_to_send = "Hello, WebSocket Server!"
            await websocket.send(message_to_send.encode('utf-8'))  # Encoding the message to UTF-8
            print("Sent to {}".format(message_to_send))

            # Wait and receive a message from the server (UTF-8 decoded)
            response = await websocket.recv()
            print("Received: {}".format(response.decode('utf-8')))  # Decoding the response to UTF-8

            # Optionally, you can continue sending and receiving messages in a loop
            while True:
                # Get user input to send to the server
                message_to_send = input("Enter message to send: ")
                await websocket.send(message_to_send.encode('utf-8'))  # Encoding the message to UTF-8
                print("Sent: {}".format(message_to_send))

                # Receive and print the response from the server
                response = await websocket.recv()
                print("Received: {}".format(response.decode('utf-8')))  # Decoding the response to UTF-8

    except websockets.exceptions.InvalidURI as e:
        print("Invalid WebSocket URI: {}".format(e))
    except websockets.exceptions.WebSocketException as e:
        print("WebSocket error: {}".format(e))
    except ConnectionRefusedError as e:
        print("Connection refused. The server might not be running or reachable: {}".format(e))
    except asyncio.TimeoutError as e:
        print("Connection timed out: {}".format(e))
    except Exception as e:
        print("An error occurred: {}".format(e))

# URI of the WebSocket server
uri = "ws://192.168.88.117:5000"  # Replace with the actual URI of the server

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(connect_to_websocket(uri))
