import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Receive data from the server
data = client_socket.recv(1024)

print(f"Received from server: {data.decode()}")

# Close the connection
client_socket.close()
