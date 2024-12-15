import socket
import threading

class PublicKeyAuthority:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.public_keys = {}
        print(f"PKA is running on {self.host}:{self.port}...")

    def handle_client(self, client):
        try:
            data = client.recv(4096).decode('utf-8')
            print(f"Received data: {data}")

            if data.startswith("STORE::"):
                cli_id, public_key = data.split("::", 1)[1].split("::", 1)
                self.public_keys[cli_id] = public_key
                print(f"Stored public key for {cli_id}.")
                client.send(f"Public key for {cli_id} stored successfully.".encode('utf-8'))

            elif data.startswith("REQUEST::"):
                cli_id = data.split("::")[1]
                if cli_id in self.public_keys:
                    client.send(self.public_keys[cli_id].encode('utf-8'))
                else:
                    client.send(f"Public key for {cli_id} not found.".encode('utf-8'))

        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client.close()

    def start(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {address}")
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65432
    pka = PublicKeyAuthority(HOST, PORT)
    pka.start()
