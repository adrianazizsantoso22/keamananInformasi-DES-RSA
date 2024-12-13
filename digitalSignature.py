import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

def sign_message(private_key, message):
    message_hash = hashlib.sha256(message.encode()).digest()
    signature = pkcs1_15.new(private_key).sign(message_hash)
    return signature

def verify_signature(public_key, message, signature):
    message_hash = hashlib.sha256(message.encode()).digest()
    try:
        pkcs1_15.new(public_key).verify(message_hash, signature)
        return True
    except (ValueError, TypeError):
        return False