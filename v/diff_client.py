import socket

# Hardcoded CLIENT PRIVATE KEY
client_private_key = 15


def main():
    s = socket.socket()
    s.connect(("localhost", 9999))

    # Step 1: Receive p, g, server’s public key
    data = s.recv(1024).decode()
    p, g, server_public_key = map(int, data.split(","))

    print("Received from server:")
    print("p =", p)
    print("g =", g)
    print("Server public key =", server_public_key)

    # Compute client public key
    client_public_key = pow(g, client_private_key, p)

    # Step 2: Send client public key
    s.send(str(client_public_key).encode())

    # Step 3: Compute shared secret
    shared_secret = pow(server_public_key, client_private_key, p)
    print("Shared secret (client) =", shared_secret)

    s.close()


if __name__ == "__main__":
    main()
