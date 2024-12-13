def brute_force_attack(ciphertext):
    # Simulasi serangan brute force (contoh sederhana)
    for key in range(1, 256):
        decrypted_message = decrypt_aes(ciphertext, bytes([key] * 16))
        if is_valid_message(decrypted_message):
            return decrypted_message
    return None