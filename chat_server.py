# chat_server.py

import socket # allow user to access the internet
import threading # allow multiple clients to communicate

# HOST: The IP address the server will listen on.
# "127.0.0.1" means only the local computer can connect.
HOST = "192.168.1.229"
PORT = 5555

# TODO 1: Create a TCP/IP socket.
# Hint: use socket.socket() with socket.AF_INET and socket.SOCK_STREAM
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET = IPv4
#SOCKET_STREAM = TCP
# TODO 2: Bind the socket to HOST and PORT, then start listening.
# Hint: server.bind(...) and server.listen()
# chat_server.py
server.bind((HOST, PORT))
server.listen()

#clients: list of all connected client sockets
#usernames: list of usernames, parallel to clients (clients[i] <-> usernames[i]
clients = []
usernames = []


def broadcast(message):
    """Send message to all connected clients."""
    # TODO 3: Loop through every socket in `clients` and send it `message`.
    for client in clients:
        client.send(message)


def handle_client(client):
    """Handles communication with ONE client, running in its own thread."""
    while True:
        try:
            # TODO 4: Receive up to 1024 bytes from `client`.
            message = client.recv(1024)



            # TODO 5: Broadcast the received message to everyone.
            broadcast(message)

        except:
            # A client has disconnected — clean up after them.
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} left the chat.".encode("utf-8"))
            usernames.remove(username)
            break


def receive_connections():
    """Continuously waits for and accepts new client connections."""
    print("Server running...")

    while True:
        # TODO 6: Accept a new connection.
        # Hint: server.accept() returns (client_socket, address)
        client, address = server.accept()
        print(f"Connected with {address}")

        # Ask the new client for their username (handshake).
        client.send("USERNAME".encode("utf-8"))
        username = client.recv(1024).decode("utf-8")

        # TODO 7: Add the new username and client socket to the tracking lists.

        print(f"Username is {username}")
        broadcast(f"{username} joined the chat!".encode("utf-8"))

        # TODO 8: Start a new thread running handle_client for this client.
        # Hint: threading.Thread(target=..., args=(...,))
        thread = threading.Thread(target=handle_client, args=(client,))


receive_connections()




