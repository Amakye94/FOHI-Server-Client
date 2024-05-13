import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'
port = 12345

# Bind the socket to the address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening...")

# Accept incoming connections
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established.")

# Send data to the client
client_socket.send(b"Hello, client! Thank you for connecting.")

# Close the connection
client_socket.close()
