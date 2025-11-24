import socket

# Hardcoded prime p and generator g
p = 23
g = 5

# Hardcoded SERVER PRIVATE KEY
server_private_key = 6

# Compute server public key
server_public_key = pow(g, server_private_key, p)


def main():
    print("Server started...")
    s = socket.socket()
    s.bind(("localhost", 9999))
    s.listen(1)

    print("Waiting for client...")
    conn, addr = s.accept()
    print("Client connected:", addr)

    # Step 1: Send p, g, and server's public key
    conn.send(f"{p},{g},{server_public_key}".encode())

    # Step 2: Receive client's public key
    client_public_key = int(conn.recv(1024).decode())
    print("Client public key =", client_public_key)

    # Step 3: Compute shared secret
    shared_secret = pow(client_public_key, server_private_key, p)
    print("Shared secret (server) =", shared_secret)

    conn.close()
    s.close()


if __name__ == "__main__":
    main()
