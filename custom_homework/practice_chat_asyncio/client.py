import asyncio

# I declared a constant in py that would indicate when a client wants to disconnect
DISCONNECT_MESSAGE = '!Disconnect'

async def tcp_echo_client():
    # simply ask the client if he really wants to connect to that server
    answer = input("Would you like to connect? (yes/no): ")
    if answer.lower() != "yes":
        return

    # open a connection, using the host and a port as arguments here
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    # while loop to allow the client to send multiple messages to the server
    # not just only one, as it was doing before
    while True:
        msg = input("Message (q for quit or press enter): ")

        if msg == 'q' or msg == '':
            break

        print(f'Send: {msg!r}')
        # write byte data (that's why we use encode() here)
        # From documentation: The method attempts to write the data to the underlying socket immediately.
        # If that fails, the data is queued in an internal write buffer until it can be sent.
        writer.write(msg.encode())
        # This is a coroutine and will suspend the caller
        # until the bytes have been transmitted and the socket is ready:
        await writer.drain()

        # read byte data, that's why we use decode() here
        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')

    # if the client types the disconnecting message, then that's what the server receives
    writer.write(DISCONNECT_MESSAGE.encode())
    await writer.drain()
    print('Close the connection')
    # of course, this tells the sever that the underlying socket needs to be closed
    writer.close()
    # Wait until the stream is closed. Should be called after close()
    # to wait until the underlying connection is closed.
    await writer.wait_closed()
    print('Successfully disconnected!')

# actually run the main function
asyncio.run(tcp_echo_client())