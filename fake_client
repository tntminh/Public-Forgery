import socket

SERVER_HOST = '127.0.0.1'  
SERVER_PORT = 8000         

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")

    req = (
            b"GET /hello.txt HTTP/1.1\r\n"
            b"Host: 127.0.0.1:8000\r\n"
            b"Connection: keep-alive\r\n"
            b"\r\n"
        )

    client_socket.sendall(req)

    print(client_socket.recv(1024))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {response}")

finally:
    # Close the connection
    client_socket.close()
    print("Connection closed.")
