import socket
from des_algorithm import generate_keys, decrypt

def start_server():
    """Memulai server untuk menerima pesan"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(1)
    print("Server listening on port 5000...")
    
    p = 61  # Bilangan prima
    q = 53  # Bilangan prima
    private_key = generate_keys(p, q)[1]

    while True:
        client, address = server.accept()
        print(f"Connection from {address} established")

        encrypted_message = client.recv(1024).decode()
        print(f"Received encrypted message: {encrypted_message}")
        
        decrypted_message = decrypt(int(encrypted_message), private_key)
        print(f"Decrypted message: {decrypted_message}")
        
        client.close()

if __name__ == "__main__":
    start_server()
