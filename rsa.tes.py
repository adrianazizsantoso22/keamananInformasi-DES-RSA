from rsa import RSA

def main():
    """Fungsi utama untuk menguji fungsionalitas RSA.
    
    Menghasilkan kunci RSA, mengenkripsi, dan mendekripsi pesan
    untuk memastikan bahwa semuanya berfungsi dengan baik.
    """
    rsa = RSA()

    rsa.generate_rsa_keys()

    print("Public Key:", rsa.public_key)
    print("Private Key:", rsa.private_key)

    message = "Hello, World!"

    encrypted_message = rsa.encrypt(message, rsa.public_key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = rsa.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message)
    
if __name__ == "__main__":
    main()