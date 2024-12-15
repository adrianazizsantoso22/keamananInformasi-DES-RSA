import socket
import threading

class ServerCuy:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []  # List of connected clients
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

        print(f"Server is running on {self.host}:{self.port}...")

    def handle_client(self, client, address):
        while True:
            try:
                message = client.recv(4096).decode('utf-8')
                if message:
                    print(f"Received from {address}: {message}")
                    self.broadcast(message, client)
                else:
                    # Remove client if connection is lost
                    self.remove_client(client)
                    break
            except Exception as e:
                print(f"Error handling client {address}: {e}")
                self.remove_client(client)
                break

    def broadcast(self, message, sender_client):
        for client in self.clients:
            if client != sender_client:
                try:
                    client.send(message.encode('utf-8'))
                except Exception as e:
                    print(f"Error sending message: {e}")
                    self.remove_client(client)

    def remove_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            client.close()
            print(f"Client {client} removed.")

    def start(self):
        while True:
            client, address = self.server.accept()
            self.clients.append(client)
            print(f"Connected with {address}")

            thread = threading.Thread(target=self.handle_client, args=(client, address))
            thread.start()


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    server = ServerCuy(HOST, PORT)
    server.start()
