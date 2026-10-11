# chat_client.py

import socket # communicate via internet (TCP/IP)
import threading # send message and receive message at the same time for all users

HOST = "192.168.1.229"   # must match the server's IP
PORT = 5555          # must match the server's port

username = input("Choose your username: ")

# TODO 1: Create a TCP socket (same as in the server).
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = IPv4
# SOCK_STREAM = TCP/IP

# TODO 2: Connect to the server using HOST and PORT.
# Hint: client.connect((HOST, PORT))
client.connect((HOST, PORT))


def receive_messages():
    """Listens for incoming messages from the server."""
    while True:
        try:
            # TODO 3: Receive a message from the server and decode it to text.
            message = client.recv(1024).decode("utf-8")

            # Handle the username handshake.
            if message == "USERNAME":
                # TODO 4: Send our username back to the server, encoded to bytes.
                client.send(username.encode("utf-8")) #sending client username back to the server
            else:
                print(message)

        except:
            print("Connection closed.")
            client.close() # close the socket
            break


def write_messages():
    """Waits for the user to type a message and sends it to the server."""
    while True:
        msg = input("") # wait for the user to type in the message
        message = f"{username}: {msg}"
        # TODO 5: Send the message to the server, encoded to bytes.
        client.send(message.encode("utf-8")) # translating from text to bytes (0's and 1's)

# TODO 6: Start receive_messages() and write_messages() in two separate threads.

threading.Thread(target=receive_messages).start()
threading.Thread(target=write_messages).start()