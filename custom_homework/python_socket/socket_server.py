import socket


my_socket = socket.socket()
print ("Socket successfully created")

# reserve a port on your computer
port = 22344

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
with my_socket as s:
	s.bind(('', port))
	print (f"socket binded to {port}")

	s.listen(5)
	print ("socket is listening")

	while True:

		# Establish connection with client.
		conn, addr = s.accept()
		print ('Got connection from', addr )

		with conn as c:
			c.send('Thank you for connecting'.encode())

		# Breaking once connection closed
		break
