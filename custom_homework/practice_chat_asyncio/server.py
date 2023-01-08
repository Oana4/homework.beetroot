import asyncio

# I declared a constant in py that would indicate when a client wants to disconnect
DISCONNECT_MESSAGE = '!Disconnect'
# I create a set so that we'll store all the clients connected at the same time to our server
all_clients = set()

# write byte data (that's why we use encode() here)
# From documentation: The method attempts to write the data to the underlying socket immediately.
# If that fails, the data is queued in an internal write buffer until it can be sent.
async def write_msg(client, data):
    client.write(data)
    await client.drain()

async def handle_echo(reader, writer):
    # each time a client connects to the specific server, we add it to the set:
    all_clients.add(writer)
    # I wrote a try-finally block just to be sure that, if smth unexpected occurs,
    # then the connection would be closed automatically
    try:
        connected = True
        while connected:
            # read byte data, that's why we use decode() here
            data = await reader.read(100)
            message = data.decode()
            if not message:
                break
            if message == DISCONNECT_MESSAGE:
                connected = False

            # on transports, for socket, we could ask for:
            # 'peername': the remote address to which the socket is connected,
            addr = writer.get_extra_info('peername')
            # Simple print to underline the address that just sent a message to the server
            print(f"Received {message!r} from {addr!r}")

            # we want to send the message that the server has just received
            # to all the connected clients
            print(f"Send: {message!r}")
            # I want to store the write functions destined to each client (writer) connected:
            list_of_calls_to_be_sent = []
            for client in all_clients:
                list_of_calls_to_be_sent.append(write_msg(client, data))
            # The reason for which I did that was to be able to gather them
            # because we may use the asyncio.gather() function in situations where
            # we may create coroutines up-front and
            # then wish to execute them all at once and
            # wait for them all to complete before continuing on.
            await asyncio.gather(*list_of_calls_to_be_sent)
            # I don't know why isn't working as I expected it to??

        all_clients.remove(writer)

    finally:
        print("Close the connection")
        writer.close()
        # Wait until the stream is closed. Should be called after close()
        # to wait until the underlying connection is closed.
        await writer.wait_closed()

async def main():
    # start a tcp server
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())