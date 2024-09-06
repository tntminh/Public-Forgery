import socket

def nc_server(host, port):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set socket options to reuse the address
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Bind to the specified host and port without DNS resolution (raw IP)
            s.bind((host, port))
            print(f"Listening on {host}:{port}...")

            # Listen for incoming connections (1 = backlog size)
            s.listen(1)

            # Verbose mode: print connection info
            conn, addr = s.accept()
            with conn:
                print(f"Connection received from {addr[0]}:{addr[1]}")

                # Receive and send data back to the client
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")  # Verbose output
                    # conn.sendall(data)  # Echo the data back to the client

    except Exception as e:
        print(f"Error: {e}")

# Example usage (raw IP, no DNS resolution)
nc_server('0.0.0.0', 8080)
