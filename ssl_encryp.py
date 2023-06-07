import socket
import ssl

# Define the host and port for the server
host = 'https://fastapi.tiangolo.com/'
port = 443

# Create a socket object for the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket in an SSL context
context = ssl.create_default_context()
sock = context.wrap_socket(sock, server_hostname=host)

# Connect to the server
sock.connect((host, port))

# Send a message to the server
message = "Hello, server!"
sock.sendall(message.encode())

# Receive a response from the server
response = sock.recv(1024)
print(response.decode())

# Close the connection
sock.close()
