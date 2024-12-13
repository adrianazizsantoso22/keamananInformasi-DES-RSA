from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_aes(message, key):
    """Fungsi ini mengenkripsi pesan menggunakan AES dengan mode GCM.
    
    Args:
        message (str): Pesan yang akan dienkripsi.
        key (bytes): Kunci rahasia untuk enkripsi (harus 16, 24, atau 32 byte).
    
    Returns:
        str: Pesan terenkripsi dalam format base64.
    """
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def decrypt_aes(encrypted_message, key):
    """Fungsi ini mendekripsi pesan yang terenkripsi menggunakan AES.
    
    Args:
        encrypted_message (str): Pesan terenkripsi dalam format base64.
        key (bytes): Kunci rahasia untuk dekripsi (harus sama dengan saat enkripsi).
    
    Returns:
        str: Pesan asli yang telah didekripsi.
    """
    data = base64.b64decode(encrypted_message)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()
