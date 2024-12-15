import socket
import threading
from rsa import RSACUY

class ClientCuy:
    def __init__(self, cli_id, server_host, server_port, pka_host, pka_port):
        self.server_host = server_host
        self.server_port = server_port
        self.pka_host = pka_host
        self.pka_port = pka_port
        self.cli_id = cli_id
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.server_host, self.server_port))
        print(f"Connected to chat server at {self.server_host}:{self.server_port}")
        
        # Connect to PKA to register and get the public key
        self.pka_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pka_client.connect((self.pka_host, self.pka_port))
        
        # Register client to PKA first
        self.register_client()

        # Request public key after registration
        self.public_key = None
        self.get_public_key()

        self.rsa = RSACUY()

    def register_client(self):
        try:
            # Send REGISTER request to PKA to register the client
            self.pka_client.send(f"REGISTER|{self.cli_id}".encode('utf-8'))
            response = self.pka_client.recv(1024).decode('utf-8')
            
            if response.startswith("REGISTERED"):
                print(f"Client {self.cli_id} registered successfully.")
            else:
                print(f"Error registering client: {response}")
        except Exception as e:
            print(f"Error registering client: {e}")

    def get_public_key(self):
        try:
            # Send GET_KEY request to PKA to fetch the public key
            self.pka_client.send(f"GET_KEY|{self.cli_id}".encode('utf-8'))
            response = self.pka_client.recv(1024).decode('utf-8')
            
            if response.startswith("PUBLIC_KEY"):
                # Extract the public key from the response
                _, public_key_str = response.split('|')
                public_key_tuple = tuple(map(int, public_key_str.strip('()').split(',')))
                self.public_key = public_key_tuple
                print(f"Received public key: {self.public_key}")
            else:
                print(f"Error getting public key: {response}")
        except Exception as e:
            print(f"Error getting public key: {e}")

    def write(self):
        while True:
            try:
                message = input("msg: ")
                
                # Ensure public key is available before encrypting
                if self.public_key:
                    encrypted_message = self.encrypt_message(message)
                    self.client.send(encrypted_message)
                else:
                    print("Public key is not available, unable to encrypt message.")
            except Exception as e:
                print(f"Error writing message: {e}")
                break

    def read(self):
        while True:
            try:
                encrypted_message = self.client.recv(4096)
                if encrypted_message:
                    # Decrypt the received message if encrypted
                    decrypted_message = self.decrypt_message(encrypted_message)
                    if decrypted_message:
                        print(f"Received (decrypted): {decrypted_message}")  # Display decrypted message
                    else:
                        print("Error decrypting message.")
            except Exception as e:
                print(f"Error reading message: {e}")
                break

    def encrypt_message(self, message):
        # Encrypt the message with the public key using RSACUY encrypt method
        if self.public_key:
            encrypted_message = self.rsa.encrypt(message, self.public_key)
            return str(encrypted_message).encode('utf-8')
        return None

    def decrypt_message(self, encrypted_message):
        # Decrypt the message using the private key
        if self.rsa.private_key:
            # Convert the encrypted message from string format to list of integers
            encrypted_message = eval(encrypted_message.decode('utf-8'))  # Decode and convert to list
            decrypted_message = self.rsa.decrypt(encrypted_message)
            return decrypted_message
        return None

    def start(self):
        write_thread = threading.Thread(target=self.write)
        read_thread = threading.Thread(target=self.read)
        write_thread.start()
        read_thread.start()


if __name__ == "__main__":
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 12345
    PKA_HOST = '127.0.0.1'
    PKA_PORT = 54321
    CLI_ID = input("Enter your client ID: ")
    client = ClientCuy(CLI_ID, SERVER_HOST, SERVER_PORT, PKA_HOST, PKA_PORT)
    client.start()
