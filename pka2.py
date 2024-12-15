import socket
import threading
from rsa import RSACUY

class PublicKeyAuthorityCuy:
    def __init__(self, host, port):
        self.public_keys = {}  # Menyimpan kunci publik klien
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"PKA Server running on {self.host}:{self.port}")

    def register_client(self, client_id):
        rsa = RSACUY()
        rsa.generate_rsa_keys()
        self.public_keys[client_id] = rsa.public_key
        print(f"Client {client_id} registered with public key: {rsa.public_key}")
        return rsa.public_key

    def get_public_key(self, client_id):
        if client_id in self.public_keys:
            return self.public_keys[client_id]
        else:
            return None

    def handle_client(self, conn, addr):
        print(f"Connected by {addr}")
        try:
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break

                command, client_id = data.split("|")

                if command == "REGISTER":
                    public_key = self.register_client(client_id)
                    # Kirimkan kunci publik dengan format yang lebih mudah diproses oleh klien
                    public_key_str = f"{public_key[0]},{public_key[1]}"
                    conn.send(f"REGISTERED|{public_key_str}".encode('utf-8'))
                elif command == "GET_KEY":
                    public_key = self.get_public_key(client_id)
                    if public_key:
                        public_key_str = f"{public_key[0]},{public_key[1]}"  # Format: e,n
                        conn.send(f"PUBLIC_KEY|{public_key_str}".encode('utf-8'))
                    else:
                        conn.send(f"ERROR|Public key for {client_id} not found.".encode('utf-8'))
        except Exception as e:
            print(f"Error handling client {addr}: {e}")
        finally:
            conn.close()

    def start(self):
        print("PKA Server is listening for connections...")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 54321
    pka = PublicKeyAuthorityCuy(HOST, PORT)
    pka.start()
