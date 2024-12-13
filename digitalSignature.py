import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

def sign_message(private_key, message):
    """Fungsi ini membuat tanda tangan digital untuk pesan menggunakan kunci privat.
    
    Args:
        private_key (RSA key): Kunci privat untuk menandatangani pesan.
        message (str): Pesan yang akan ditandatangani.
    
    Returns:
        bytes: Tanda tangan digital sebagai byte.
    """
    message_hash = hashlib.sha256(message.encode()).digest()
    signature = pkcs1_15.new(private_key).sign(message_hash)
    return signature

def verify_signature(public_key, message, signature):
    """Fungsi ini memverifikasi tanda tangan digital menggunakan kunci publik.
    
    Args:
        public_key (RSA key): Kunci publik untuk memverifikasi tanda tangan.
        message (str): Pesan yang ditandatangani.
        signature (bytes): Tanda tangan digital yang akan diverifikasi.
    
    Returns:
        bool: True jika tanda tangan valid, False jika tidak valid.
    """
    message_hash = hashlib.sha256(message.encode()).digest()
    try:
        pkcs1_15.new(public_key).verify(message_hash, signature)
        return True
    except (ValueError, TypeError):
        return False
