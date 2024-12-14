# Importing Modules
import socket

class Reciver:
    def __init__(self):
        # Making an OBJ
        self.Server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect and get data from IP, of the Pi.
        self.Pi_IP = "192.168.254.121"
        self.Port = 5000

        # Bind the socket to the IP address and port.
        self.Server_socket.bind((self.Pi_IP, self.Port))

    def Start(self):
        self.Server_socket.listen(1) # Allow Only One Connection.
        print(f"[Reciver] Listening For Connections on {self.Pi_IP}:{self.Port}")

        while True:
            # Accept a connection from client
            client_socket, client_address = self.Server_socket.accept()
            print(f"[Reciver] Accepted Connection From {client_address}")

            try:
                # Receive Data From The Client.
                data = client_socket.recv(1024).decode() # Receive up to 1024 bytes
                if data:
                    print(f"[Reciver] Received: {data}")
                else:
                    print("[Reciver] No Data Given")
            finally:
                # Close the client socket
                client_socket.close()
                print("Client Socket Closed.")