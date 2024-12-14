# Importing Modules
import socket

class Sender:
    def __init__(self):
        # Creating a socket object.
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Defineing server address and port
        self.server_address = ("192.168.254.121", 5000)

        # Connecting to server.
        self.client_socket.connect(self.server_address)

    def Send(self, message):
        self.client_socket.send(message.encode())

    def Close(self):
        self.client_socket.close()