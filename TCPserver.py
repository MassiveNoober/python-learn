# docs on socket: https://docs.python.org/3/library/socket.html#module-socket
import socket

# Start a TCP server on localhost:8080
with socket.create_server(("localhost", 8080), reuse_port=True) as server_socket:

    # Block until we receive an incoming connection
    connection, address = server_socket.accept()

    print(f"accepted connection from {address}")
    
    # Read data
    data = connection.recv(1024)

    # Write the same data back
    connection.sendall(data)