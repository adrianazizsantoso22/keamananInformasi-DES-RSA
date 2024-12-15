def gcd(a, b):
    """Menghitung Greatest Common Divisor (GCD)"""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Menghitung Modular Inverse dari e"""
    d = 0
    x1, x2, y1, y2 = 0, 1, 1, 0
    while e > 0:
        q = phi // e
        e, phi = phi % e, e
        x1, x2 = x2 - q * x1, x1
        y1, y2 = y2 - q * y1, y1
    return x2 + phi if phi < 0 else x2

def generate_keys(p, q):
    """Menghasilkan kunci publik dan privat"""
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Umumnya digunakan sebagai nilai e
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(message, pub_key):
    """Enkripsi pesan menggunakan kunci publik"""
    e, n = pub_key
    message_int = int.from_bytes(message.encode(), 'big')
    cipher_int = pow(message_int, e, n)
    return cipher_int

def decrypt(cipher_int, priv_key):
    """Dekripsi pesan menggunakan kunci privat"""
    d, n = priv_key
    message_int = pow(cipher_int, d, n)
    return message_int.to_bytes((message_int.bit_length() + 7) // 8, 'big').decode()

if __name__ == "__main__":
    p = 61
    q = 53
    public_key, private_key = generate_keys(p, q)
    message = "Hello"
    cipher = encrypt(message, public_key)
    print(f"Encrypted: {cipher}")
    decrypted_message = decrypt(cipher, private_key)
    print(f"Decrypted: {decrypted_message}")
