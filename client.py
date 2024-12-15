import socket
from des_algorithm import generate_keys, encrypt

def send_message(message, pub_key):
    """Mengirim pesan terenkripsi ke server."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    
    cipher = encrypt(message, pub_key)
    
    client.send(str(cipher).encode())
    print(f"Sent encrypted message: {cipher}")
    client.close()

if __name__ == "__main__":
    p = 61  # Bilangan prima
    q = 53  # Bilangan prima
    public_key = generate_keys(p, q)[0]
    
    message = input("Enter message to encrypt and send: ")
    send_message(message, public_key)
