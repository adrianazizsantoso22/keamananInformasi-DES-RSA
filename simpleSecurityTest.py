def brute_force_attack(ciphertext):
    """Fungsi ini mensimulasikan serangan brute force pada pesan terenkripsi.
    
    Args:
        ciphertext (str): Pesan terenkripsi yang akan diserang.
    
    Returns:
        str or None: Pesan asli jika berhasil didekripsi, None jika gagal.
    """
    for key in range(1, 256):
        decrypted_message = decrypt_aes(ciphertext, bytes([key] * 16))
        if is_valid_message(decrypted_message):
            return decrypted_message
    return None

def is_valid_message(message):
    """Fungsi ini memeriksa apakah pesan yang didekripsi valid.
    
    Args:
        message (str): Pesan yang akan diperiksa.
    
    Returns:
        bool: True jika pesan valid, False jika tidak.
    """
    return isinstance(message, str) and len(message) > 0
